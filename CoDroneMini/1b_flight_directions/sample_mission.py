import CoDrone_mini
import time

drone = CoDrone_mini.CoDrone()
drone.pair()

drone.set_trim(15, 45)
time.sleep(1)

drone.takeoff()

drone.hover(4)

drone.set_roll(32)
drone.set_pitch(24)
drone.set_yaw(37)
drone.set_throttle(20)
drone.move(1)

drone.set_trim(15, 45)
time.sleep(1)
drone.takeoff()
drone.land()

drone.set_roll(-89)
drone.set_pitch(-82)
drone.set_yaw(-5)
drone.set_throttle(-10)
drone.move(1)

drone.set_trim(15, 45)
time.sleep(1)
drone.takeoff()
drone.land()

for x in range(4):
    drone.set_pitch(-20)
    drone.move(1)
    drone.set_yaw(-50)
    drone.move(1)

drone.land()

print(drone.get_battery_percentage())
drone.close()
