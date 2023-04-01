from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR

from .client import BaseClient, ClientEvent


class TcpClient(BaseClient):
    def __init__(self):
        self._runned = False
        self._socket = socket(AF_INET, SOCK_STREAM)

    def connect(self, server_address):
        if self._runned:
            raise Exception("TcpClient already runned")
        self._runned = True 
        self._socket.connect(server_address)
        self._start_loop()

    def listen(self, address: tuple[str, int]):
        if self._runned:
            raise Exception("TcpClient already runned")
        self._runned = True 
        self._socket.bind(address)
        self._socket, _ = self._socket.accept()
        self._start_loop()

    def send(self, data):
        if not self._runned:
            return
        self._socket.send(data)

    def stop(self):
        if not self._runned:
            return
        self._runned = False
        self._call_handlers(ClientEvent.STOP)
        try:
            self._socket.shutdown(SHUT_RDWR)
        except OSError:
            pass

    def _start_loop(self):
        Thread(
                name = "LISTEN_LOOP",
                target = self._loop,
                daemon = True
        ).start()
        self._call_handlers(ClientEvent.START)

    def _loop(self):
        """
        Listens for a connection to the server. When receiving a message 
        from it, calls handlers subscribed to ON_MESSAGE
        """
        while not self._runned:
            data = self._socket.recv(128)
            # If the data is empty, it's a disconnect signal
            if not data:
                break
            self._call_handlers(ClientEvent.MESSAGE, data)

        self.stop()


