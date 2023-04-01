from s2rcp.core.utils import check_int_value_is_valid
from .command import Command


class StartCommand(Command):

    MAX_SPEED = 2**7-1

    def __init__(self, motor_id, speed, inverted):
        super().__init__(motor_id)

        check_int_value_is_valid(speed, min=0, max=StartCommand.MAX_SPEED)
        self.speed = speed

        check_int_value_is_valid(inverted, min=0, max=1)
        self.inverted = inverted

    def __str__(self) -> str:
        return super().__str__() + " speed={sp}; inverted={inv};"\
                                    .format(sp=self.speed, inv=self.inverted)

