class S2rcpException(Exception):
    pass


class S2rcpDecodeError(S2rcpException):
    pass


class S2rcpEncodeError(S2rcpException):
    pass
