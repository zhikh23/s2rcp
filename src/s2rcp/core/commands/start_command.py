from s2rcp.core.utils import check_int_value_is_valid
from s2rcp.core.exceptions import S2rcpEncodeError

from .command import Command, CommandEncoder, CommandDecoder
from .all_commands import (
    get_command_type_id, register_command_type
)


class StartCommand(Command):

    MAX_SPEED = 2**7-1

    def __init__(self, motor_id, speed, inverted):
        super().__init__(motor_id)
        self.command_type = get_command_type_id(self.__class__)
        check_int_value_is_valid(speed, min=0, max=StartCommand.MAX_SPEED)
        self.speed = speed
        self.inverted = inverted

    def get_max_speed(self):
        return self.MAX_SPEED

    @staticmethod
    def get_encoder():
        return StartCommandEncoder()

    @staticmethod
    def get_decoder():
        return StartCommandDecoder()


class StartCommandEncoder(CommandEncoder):
    def encode(self, command):
        if type(command) is not StartCommand:
            raise S2rcpEncodeError(
                "type of command must be StartCommand; {t} given"
                .format(t=type(command))
            )
        return bytearray([
            (command.motor_id << 2) + command.command_type,
            (command.inverted << 7) + command.speed
        ])


class StartCommandDecoder(CommandDecoder):
    def decode(self, data):
        return StartCommand(
            motor_id = data[0] >> 2,
            speed    = data[1] & 0x7F,
            inverted = bool(data[1] >> 7)
        )


register_command_type(StartCommand, 0b01)

