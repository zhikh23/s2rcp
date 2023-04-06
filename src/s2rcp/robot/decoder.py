from s2rcp.core.exceptions import S2rcpDecodeError
from s2rcp.core.container import Container
from s2rcp.core.commands import get_command_by_id


def decode(data):
    """
    Decodes an array of bytes by S2RCP.
    Return:
     - Container object
     - Number of bytes processed
    """
    time = (data[0] << 4) + (data[1] >> 4)
    commands_num = data[1] & 0xF 
    processed = commands_num * 2 + 2
    commands = list()
    for i in range(2, processed, 2):
        command_type = data[i] & 0x2
        command_class = get_command_by_id(command_type)
        if not command_class:
            raise S2rcpDecodeError(
                "unknown command type: {t}"
                .format(t=bin(command_type))
            )
        command_decoder = command_class.get_decoder()
        command = command_decoder.decode(data[i:i+2])
        commands.append(command)
    container = Container(time, commands)
    return container, processed
