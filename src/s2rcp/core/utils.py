from time import time


def check_int_value_is_valid(value, min, max):
    if not _is_int_value_valid(value, min, max):
        raise ValueError("value must be in range [{min}; {max}] ({value} given)"
                           .format(min=min, max=max, value=value))


def _is_int_value_valid(value, min, max):
    if type(value) is not int:
        return False
    return value >= min and value <= max


def get_time_ms_12bits():
    return int(time() * 1000) & 0xFFF
