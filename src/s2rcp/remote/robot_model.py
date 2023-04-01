

class RobotModel():
    def __init__(self, axes_config):
        self._axes_config = axes_config
        self._motors = dict.fromkeys(
                self._axes_config.get_all_motors(), 0.0
        )

    def set_axis_value(self, axis_name, value):
        if abs(value) > 1.0:
            raise ValueError("axis value must be between -1.0 and +1.0")
        
        motors_dict = self._axes_config.get_motors_from_axis(axis_name)
        for motor_id, k in motors_dict.items():
            motor_value = self._motors[motor_id] + k * value
            if motor_value < -1.0:
                self._motors[motor_id] = -1.0
            elif motor_value > 1.0:
                self._motors[motor_id] = 1.0
            else:
                self._motors[motor_id] = motor_value

    def get_all_motors_id(self):
        return list(self._motors.keys())

    def get_motor_value(self, motor):
        return self._motors[motor]
