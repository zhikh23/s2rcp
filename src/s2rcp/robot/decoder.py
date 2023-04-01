from s2rcp.core.exceptions import S2rcpDecodeError
from s2rcp.core.container import Container
from s2rcp.core.commands import (
    StartCommand,
    StopCommand,
    COMMANDS_TYPES
)


LAST_2_BITS = 0x3
LAST_4_BITS = 0xF
LAST_7_BITS = 0x7F


def decode(data):
    """
    Decodes an array of bytes by S2RCP.
    Return:
     - Container object
     - Number of bytes processed
    """

    # =============== HEADER =================

    # Time
    #   | # # # # # # # # | # # # # _ _ _ _ |
    time = (data[0] << 4) + (data[1] >> 4)

    # Commands num
    #   | _ _ _ _ _ _ _ _ | _ _ _ _ # # # # |
    commands_num = data[1] & LAST_4_BITS
    processed = commands_num * 2 + 2

    # ================= BODY ==================
    commands = list()
    for i in range(2, processed, 2):

        # Motor id
        #   | # # # # # # _ _ | _ _ _ _ _ _ _ _ |
        motor_id = data[i] >> 2

        # Command type
        #   | _ _ _ _ _ _ # # | _ _ _ _ _ _ _ _ |
        command_type = data[i] & LAST_2_BITS

        if command_type == COMMANDS_TYPES[StartCommand]:

            # Inverted
            #   | _ _ _ _ _ _ _ _ | #  _ _ _ _ _ _ _ |
            inverted = data[i+1] >> 7

            # Speed
            #   | _ _ _ _ _ _ _ _ | _ # # # # # # # |
            speed = data[i+1] & LAST_7_BITS

            command = StartCommand(motor_id, speed, inverted)

        elif command_type == COMMANDS_TYPES[StopCommand]:
            command = StopCommand(motor_id)

        else:
            raise S2rcpDecodeError(
                "unknow command type: {type}"
                .format(type=bin(command_type))
            )

        commands.append(command)

    container = Container(time, commands)
    return container, processed
