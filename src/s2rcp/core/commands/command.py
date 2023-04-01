from s2rcp.core.utils import check_int_value_is_valid


class Command:
    def __init__(self, motor_id):
        check_int_value_is_valid(motor_id, min=0, max=2**6-1)
        self.motor_id = motor_id

    def __str__(self):
        return "<{cn}> motor_id={id};".format(
                cn=self.__class__, id=self.motor_id 
        )


