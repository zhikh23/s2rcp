from abc import ABCMeta, abstractmethod


class BaseMotor(metaclass=ABCMeta):
    @abstractmethod
    def start(self, speed, inverted):
        pass

    @abstractmethod
    def stop(self):
        pass
