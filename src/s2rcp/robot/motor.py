from abc import ABCMeta, abstractmethod


class BaseMotor(metaclass=ABCMeta):
    @abstractmethod
    def start(self, speed, inverted):
        raise NotImplementedError(
            """the start(speed, inverted) method of the abstract class 
            BaseMotor is not implemented"""
        )

    @abstractmethod
    def stop(self):
        raise NotImplementedError(
            "the stop() method of the abstract class BaseMotor is not 
            implemented"
        )
