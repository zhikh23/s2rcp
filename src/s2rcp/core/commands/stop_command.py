from s2rcp.core.exceptions import S2rcpEncodeError

from .command import Command, CommandEncoder, CommandDecoder
from .all_commands import get_command_type_id


class StopCommand(Command):
    def __init__(self, motor_id):
        super().__init__(motor_id)
        self.command_type = get_command_type_id(self.__class__)

    @staticmethod
    def get_encoder():
        return StopCommandEncoder()

    @staticmethod
    def get_decoder():
        return StopCommandDecoder() 


class StopCommandEncoder(CommandEncoder):
    def encode(self, command):
        if type(command) is not StopCommand:
            raise S2rcpEncodeError(
                "type of command must be StopCommand; {t} given"
                .format(t=type(command))
            )
        return bytearray([
            (command.motor_id << 2) + command.command_type,
            0       # Empty byte
        ])


class StopCommandDecoder(CommandDecoder):
    def decode(self, data):
        return StopCommand(
            motor_id = data[0] >> 2
        )

