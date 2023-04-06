from .start_command import StartCommand
from .stop_command import StopCommand
 

_map_command_to_id = {
    StartCommand: 0b01,
    StopCommand:  0b10,
}


_map_id_to_command = {
    id_: command for command, id_ in _map_command_to_id.items() 
}


def get_command_type_id(command_type):
    return _map_command_to_id.get(command_type, None)


def get_command_by_id(command_type_id):
    return _map_id_to_command.get(command_type_id, None)

