import time

class PID_Controller:
    def __init__(self, kp, ki, kd, target = 0.0):

        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.target = target

        self.current_state = 0.0
        self.current_error = 0.0
        self.last_error = 0.0
        self.last_time = 0.0
        self.integral = 0.0
        



    def recieve_target(self, target):
        self.target = target
        print("Target Recieved!!")

    def error_deadzone(self):
        if abs(self.target - self.current_state) > 0.5:
            return self.target - self.current_state
        else:
            return 0.0

    def update_current(self, current_state):
        self.current_state = current_state
        print("Current State Recieved!!")


    def compute(self):
        
        current_time = time.time()

        if not self.last_time:
            self.last_time = current_time
            return False, self.error_deadzone()

        #dt
        dt = current_time - self.last_time

        # e(t)
        self.current_error = self.error_deadzone()

        
        # d e(t)
        delta_e = self.current_error - self.last_error

        #integral
        self.integral += self.current_error * dt

        #pterm
        pterm = self.kp * self.current_error

        #iterm
        iterm = self.ki * self.integral

        #dterm
        dterm = self.kd * (delta_e/dt)

        #final equation
        self.u_t = pterm + iterm + dterm


        #updating for next iteration
        self.last_error = self.current_error
        self.last_time = current_time

        return self.u_t, self.current_error


    def telemetry(self, step_no, real_current_state):
        print(f"Step: {step_no}, Current Error: {self.current_error}, Theoretical Output: {self.u_t}, Robot Current State: {real_current_state}")




