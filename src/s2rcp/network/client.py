from threading import Thread
from abc import ABCMeta, abstractmethod
from enum import Enum


class ClientEvent(Enum):
    START = 1
    MESSAGE = 2
    STOP = 3


class BaseClient(metaclass=ABCMeta):
    def __init__(self):
        self.__handlers = dict()

    @abstractmethod
    def send(self, data) -> None:
        pass   

    def subscribe(self, event_type, handler) -> None:
        """
        Subscribes a function to a specific event.
        When calling a function, arguments are passed as a dictionary
        """
        if event_type not in self.__handlers.keys():
            self.__handlers[event_type] = list()
        self.__handlers[event_type].append(handler)

    def _call_handlers(self, event_type, *args):
        """
        Calls all handlers subscribed to this event
        When calling a handler, arguments are passed as a dictionary
        """
        if event_type not in self.__handlers.keys():
            return

        for handler in self.__handlers[event_type]:
            Thread(target=handler, args=args, daemon=True).start() 

