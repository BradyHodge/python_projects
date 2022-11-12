import CoDrone_mini
import time

drone = CoDrone_mini.CoDrone()
drone.pair()

drone.set_trim(15, 45)
time.sleep(1)

for x in range(1):
    drone.takeoff()
    drone.hover(3)
    drone.land()
drone.close()

