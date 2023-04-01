from .start_command import StartCommand
from .stop_command import StopCommand
 

COMMANDS_TYPES = {
    StartCommand: 0b01,
    StopCommand:  0b10,    
}

