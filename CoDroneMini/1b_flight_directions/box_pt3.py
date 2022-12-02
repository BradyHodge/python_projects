import CoDrone_mini
import time

drone = CoDrone_mini.CoDrone()
drone.pair()

drone.set_trim(15, 45)
time.sleep(1)

drone.takeoff()

for x in range(4):
    drone.set_pitch(-20)
    drone.move(1)
    drone.set_yaw(-50)
    drone.move(1)

drone.land()

print(drone.get_battery_percentage())
drone.close()
