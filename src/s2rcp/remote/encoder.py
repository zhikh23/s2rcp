import s2rcp.core.utils
from s2rcp.core.exceptions import S2rcpEncodeError
from s2rcp.core.commands import (
    StartCommand,
    StopCommand,
    COMMANDS_TYPES
)


def encode(commands):
    """
    Wraps commands in a container and encodes according to S2RCP
    """
    
    # =============== HEADER =================
    # Time
    #   | # # # # # # # # | # # # # _ _ _ _ |
    time = s2rcp.core.utils.get_time_ms_12bits()

    # Commands num
    #   | _ _ _ _ _ _ _ _ | _ _ _ _ # # # # |
    commands_num = len(commands)

    result = bytearray([
        time >> 4,                          # 1st byte
        ((time & 0xF) << 4) + commands_num  # 2st byte
    ])

    # ================= BODY ==================
    for command in commands:
        # Motor id
        #   | # # # # # # _ _ | _ _ _ _ _ _ _ _ |
        motor_id = command.motor_id

        # Command type
        #   | _ _ _ _ _ _ # # | _ _ _ _ _ _ _ _ |
        command_type = command.command_type

        result += bytearray([
            (motor_id << 6) + command_type
        ])

        if command_type == COMMANDS_TYPES[StartCommand]:
            # Inverted
            #   | _ _ _ _ _ _ _ _ | #  _ _ _ _ _ _ _ |
            inverted = command.inverted

            # Speed
            #   | _ _ _ _ _ _ _ _ | _ # # # # # # # |            
            speed = command.speed

            result += bytearray([
                (inverted << 7) + speed
            ])

        elif command_type == COMMANDS_TYPES[StopCommand]:
            # Stop action type
            #   | _ _ _ _ _ _ _ _ | _ _ _ _ _ _ # # |
            stop_action_type = command.stop_action_type

            result += bytearray([
                stop_action_type
            ])

        else:
            raise S2rcpEncodeError(
                "unknow command type: {type}"
                .format(type=bin(command_type))
            )

    return result

