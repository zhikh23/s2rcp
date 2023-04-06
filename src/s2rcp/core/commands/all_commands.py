from s2rcp.core.exceptions import S2rcpException


_map_command_to_id = dict()
_map_id_to_command = dict()


def register_command_type(command_type, command_type_id):
    if command_type_id in _map_id_to_command:
        raise S2rcpException(
            "command with id={id_} has already been registered"
            .format(id_=command_type_id)
        )
    _map_command_to_id[command_type_id] = command_type
    _map_id_to_command[command_type] = command_type_id


def get_command_type_id(command_type):
    return _map_command_to_id.get(command_type, None)


def get_command_by_id(command_type_id):
    return _map_id_to_command.get(command_type_id, None)

