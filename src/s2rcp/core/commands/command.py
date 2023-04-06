from abc import ABCMeta, abstractmethod
from s2rcp.core.utils import check_int_value_is_valid


class Command(metaclass=ABCMeta):
    def __init__(self, motor_id):
        check_int_value_is_valid(motor_id, min=0, max=2**6-1)
        self.motor_id = motor_id

    @staticmethod
    @abstractmethod
    def get_encoder():
        pass

    @staticmethod
    @abstractmethod
    def get_decoder():
        pass


class CommandEncoder(metaclass=ABCMeta):
    @abstractmethod
    def encode(self, command):
        pass


class CommandDecoder(metaclass=ABCMeta):
    @abstractmethod
    def decode(self, data):
        pass

