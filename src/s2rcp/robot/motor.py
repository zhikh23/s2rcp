from abc import ABCMeta, abstractmethod


class BaseMotor(metaclass=ABCMeta):
    @abstractmethod
    def start(self, speed: int, inverted: int) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass
