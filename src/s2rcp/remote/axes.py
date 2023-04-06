import json


class AxesConfig:

    def __init__(self):
        self._axes = dict()

    def setup_from_json(self, json_str):
        self._axes = json.loads(json_str)

    def add_new_axis(self, axis_name):
        self._axes[axis_name] = dict()

    def add_motor_to_axis(self, axis_name, motor_id, motor_k):
        if axis_name not in self._axes.keys():
            self.add_new_axis(axis_name)
        self._axes[axis_name][motor_id] = motor_k

    def get_all_axes(self):
        return list(self._axes.keys())

    def get_motors_from_axis(self, axis_name):
        return self._axes[axis_name]
    
    def get_all_motors(self):
        all_motors = list()
        for axis_name in self._axes:
            all_motors.extend(self._axes[axis_name].keys())
        return all_motors
