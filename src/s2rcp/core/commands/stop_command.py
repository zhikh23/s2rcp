from .command import Command


class StopCommand(Command):
    def __init__(self, motor_id):
        super().__init__(motor_id)


