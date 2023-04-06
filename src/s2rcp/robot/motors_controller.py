import s2rcp.core.utils
from s2rcp.network import ClientEvent
from s2rcp.core.commands import (
    StartCommand,
    StopCommand
)

from .motor import BaseMotor
from . import decoder as s2rcp_decoder


class MotorsController:
    def __init__(self, network_client):
        self._motors = dict()
        
        self._client = network_client
        self._client.subscribe(ClientEvent.MESSAGE, self._on_message)

        self._runned = False
        self._ignore_latency = True
        self._max_latency = None

    def set_motor(self, id, motor):
        assert issubclass(type(motor), BaseMotor)
        self._motors[id] = motor

    def start(self):
        self._runned = True

    def stop(self):
        self._runned = False
        for motor in self._motors.values():
            motor.stop()

    def _on_message(self, data):
        """
        Receiving a message, decoding and executing commands
        """
        if not self._runned:
            return

        containers = self._decode_recursively(data)
        for container in containers:

            # Get time last 12 bits to calculate latency
            now = s2rcp.core.utils.get_time_ms_12bits()
            
            latency = now - container.time
            if not self._ignore_latency and latency > self._max_latency:
                continue

            for command in container.commands:
                self._execute_command(command)

    def _decode_recursively(self, data):
        """
        It decodes using the S2RCP protocol, and if there is still information
        left after decoding one container, it tries to decode the remaining
        information. I.e. if the server sent two containers in one message
        (this is possible in TCP), the method decodes them both
        """
        containers = list()
        container, processed = s2rcp_decoder.decode(data)
        containers.append(container)

        if len(data) > processed:
            # Continue decoding
            containers.extend(self._decode_recursively(data[processed:]))
        return containers

    def _execute_command(self, command):
        motor = self._motors.get(command.motor_id, None)
        if not motor:
            # This command is addressed to another controller
            return

        if type(command) is StartCommand:
            motor.start(
                command.speed,
                command.inverted
            )
        elif type(command) is StopCommand:
            motor.stop()
