from .utils import check_int_value_is_valid


class Container:
    def __init__(self, time, commands):
        check_int_value_is_valid(time, min=0, max=2**12-1)
        self.time = time
        self.commands = commands

    def __str__(self):
        return "<cn> time={t}; commands=[".format(cn=self.__class__, t=self.time)\
                + "\n\t".join( [str(command) for command in self.commands] )\
                + "];"

