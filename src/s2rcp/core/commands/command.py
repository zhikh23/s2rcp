from abc import ABCMeta, abstractmethod
from s2rcp.core.utils import check_int_value_is_valid


class Command(metaclass=ABCMeta):
    def __init__(self, motor_id):
        check_int_value_is_valid(motor_id, min=0, max=2**6-1)
        self.motor_id = motor_id

    @staticmethod
    @abstractmethod
    def get_encoder():
        raise NotImplementedError(
            """the get_encoder() method of the abstract class Command is not 
            implemented"""
        )

    @staticmethod
    @abstractmethod
    def get_decoder():
        raise NotImplementedError(
            """the get_decoder() method of the abstract class Command is not 
            implemented"""
        ) 


class CommandEncoder(metaclass=ABCMeta):
    @abstractmethod
    def encode(self, command):
        raise NotImplementedError(
            """the encode(command) method of the abstract class CommandEncoder 
            is not implemented"""
        ) 


class CommandDecoder(metaclass=ABCMeta):
    @abstractmethod
    def decode(self, data):
        raise NotImplementedError(
            """the decode(data) method of the abstract class CommandDecoder 
            is not implemented"""
        ) 
