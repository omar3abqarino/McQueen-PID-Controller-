import time

class PID_Controller:
    def __init__(self, kp, ki, kd, current_state, target = 0.0):

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

    def error_deadzone(self):
        if abs(self.error) > 1.0:
            return True
        else:
            return 0.0

    def update(self):
        if not self.error_deadzone():
            current_time = time.time()

            if not self.last_time:
                self.last_time = current_time
                return False

            #dt
            dt = current_time - self.last_time

            # e(t)
            self.error = self.current_state - self.target


            pterm = self.kp * self.error
            
            
