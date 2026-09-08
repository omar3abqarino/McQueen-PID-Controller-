from main_class import PID_Controller
import time

#creating an instance
target = 50
pid = PID_Controller(1.62, 1.37, 0.12)
pid.recieve_target(target)
current_state = 0.0

step = 1
while True:
    pid.update_current(current_state)
    output, current_error = pid.compute()

    if current_error == 0.0:
        print("Target Reached!!")
        break
    #first time
    if not output:
        print("shit")
        time.sleep(0.1)
        continue

    current_state += (output - current_state) * 0.1
    pid.telemetry(step, current_state)
    time.sleep(0.1)
    step += 1



