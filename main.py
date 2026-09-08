from main_class import PID_Controller
import time

n_steps = input("Enter number of steps desired: ")

#creating an instance
pid = PID_Controller(1, 0.3, 1)
pid.recieve_target(100)
current_state = 0.0


for i in range(1, n_steps + 1, 1):
    pid.update_current(current_state)
    output = pid.compute()

    #first time
    if not output:
        time.sleep(0.1)
        continue

    current_state += output * 0.1
    pid.telemetry(i, current_state)



