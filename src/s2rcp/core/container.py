from .utils import check_int_value_is_valid


class Container:
    def __init__(self, time, commands):
        check_int_value_is_valid(time, min=0, max=2**12-1)
        self.time = time
        self.commands = commands

