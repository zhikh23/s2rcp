from s2rcp.core.commands import (
    StartCommand, StopCommand
)

from .robot_model import RobotModel
from . import encoder as s2rcp_encoder


class RemoteController:

    def __init__(self, network_client, axes_config):
        self._axes_config = axes_config
        self._client = network_client

        self._model = RobotModel(axes_config)
        self._buffered_model = RobotModel(axes_config)

    def set_axis_value(self, axis_name, value):
        self._buffered_model.set_axis_value(axis_name, value)

    def update(self):
        commands = list()
        for motor_id in self._model.get_all_motors_id():
            actual_value   = self._model.get_motor_value(motor_id)
            buffered_value = self._buffered_model.get_motor_value(motor_id)
            if actual_value != buffered_value:
                if buffered_value == 0.0:
                    command = self._create_stop_command(motor_id)
                else:
                    command = self._create_start_command(motor_id, buffered_value)
                commands.append(command)

        self._reset_buffer()
        self._send_commands(commands)

    def _reset_buffer(self):
        self._model = self._buffered_model
        self._buffered_model = RobotModel(self._axes_config)

    def _send_commands(self, commands):
        encoded_commands = s2rcp_encoder.encode(commands)
        self._client.send(encoded_commands)

    def _create_start_command(self, motor_id, speed):
        if abs(speed) > 1.0:
            raise ValueError(
                "speed must be in range -1.0 .. +1.0 ({given} given)"
                .format(given=speed)
            )

        speed = abs(int(speed * StartCommand.MAX_SPEED))
        inverted = speed < 0.0
        
        return StartCommand(motor_id, speed, inverted)

    def _create_stop_command(self, motor_id):
        return StopCommand(motor_id)
