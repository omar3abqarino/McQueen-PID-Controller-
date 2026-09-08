

class PID_Controller:
    def __init__(self, kp, ki, kd, current_state, target = None):

        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.current_state = current_state
        self.target = target

        self.error = None
        self.last_time = None
        



    def recieve_target(self, target):
        self.target = target
        print("Target Recieved!!")

    