import s2rcp.core.utils
from s2rcp.core.exceptions import S2rcpEncodeError


def encode(commands):
    """
    Wraps commands in a container and encodes according to S2RCP
    """
    if not commands:
        raise S2rcpEncodeError("commands list must be not empty")
    time = s2rcp.core.utils.get_time_ms_12bits()
    commands_num = len(commands)
    encoded = bytearray([
        time >> 4,
        ((time & 0xF) << 4) + commands_num
    ])
    for command in commands:
        encoder = command.get_encoder()
        encoded += encoder.encode(command)
    return encoded

