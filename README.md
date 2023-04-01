# S2RCP - Simple Remote Robot Control Protocol.

S2RCP is a simple application-level protocol for remote robot control. Allows remote control of robot motors by sending and receiving packets with commands. Due to the small size of the packets and the simplicity of their encoding and decoding, applications implemented on the basis of S2RCP can be launched on devices with weak hardware, for example, on EV3 Mindstorms microcomputers with the [ev3dev](https://www.ev3dev.org/) operating system. Another advantage of S2RCP is its versatility. According to this protocol, you can control any robot where you do not need perfect precision of movements.

This package includes modules:
 - `core` - basic classes and functions needed to work
 - `network` - classes that provide communication between the robot and remote control
 - `robot` - for the software part of the robot
 - `remote` - for the software part responsible for remote controlling the robot

# How to use?

## Installation

Install from [pip](https://test.pypi.org/project/s2rcp/)
```sh
pip install -i https://test.pypi.org/simple/ s2rcp
```

## Code example from the robot side

1. Implement `BaseMotor` interface for _your_ motors
```py
from s2rcp.robot import BaseMotor

class MyMotor(BaseMotor):
    def start(self, speed: int, inverted: bool) -> None:
        # your implmentaion is here...

    def stop(self) -> None:
        # your implmentaion is here...
```

2. Import of required modules
```py
from s2rcp.robot import *
from s2rcp.network import TcpClient
```

3. Create a TCP client to accept connection from remote controller
```py
tcp_client = TcpClient()

# ROBOT_ADDRESS - ipv4 address in the form "xxx.xxx.xxx.xxx", for example "192.168.1.10"
# ROBOT_PORT - the port that will listen to the work, for example 53445
tcp.client.listen((ROBOT_ADDRESS, ROBOT_PORT))
```

4. Create a controller and register your motors
```py
# Create controller for motors
controller = MotorsController(tcp_client)

# Register your motors
LEFT, RIGHT = range(2)      # create constants for id motors
controller.set_motor(
    # your motor class implementing the BaseMotor interface (see above)
    id = LEFT, MyMotor(...)     # any constructor
)
controller.set_motor(
    id = RIGHT, MyMotor(...)
)
```

5. Motors controller can be turned on and off
```py
controller.start()
controller.stop()
```

## Code example from the remote side

2. Import of required modules
```py
from s2rcp.remote import *
from s2rcp.network import TcpClient
```

3. Create a TCP client to connect to the robot
```py
tcp_client = TcpClient()

# ROBOT_ADDRESS - ipv4 address in the form "xxx.xxx.xxx.xxx", for example "192.168.1.10"
# ROBOT_PORT - the port that the robot controller listens to, for example 53445
tcp.client.connect((ROBOT_ADDRESS, ROBOT_PORT))
```

4. Setup basic robot control
```py
# Example of settings axes for "tank" control
axes_config = AxesConfig()
axes_config.add_new_axis("MOVE")
axes_config.add_motor_to_axis("MOVE", motor_id=0, motor_k=1.0)
axes_config.add_motor_to_axis("MOVE", motor_id=1, motor_k=1.0)
axes_config.add_new_axis("ROTATE")
axes_config.add_motor_to_axis("ROTATE", motor_id=0, motor_k=1.0)
axes_config.add_motor_to_axis("ROTATE", motor_id=1, motor_k=-1.0)

# Create controller
controller = RemoteController(tcp_client, axes_config)
```

5. Example of robot control
```py
# "go straight ahead"
controller.set_axis_value("MOVE", +1.0)
controller.update() 
#            ^^^ 
# Controller updates the internal state, generates commands and sends them to the robot

# "turn around on the spot"
controller.set_axis_value("ROTATE", -1.0)
controller.update()

# "stop"
controller.set_axis_value("MOVE", 0)
controller.update()
```
