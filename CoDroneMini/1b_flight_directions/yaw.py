import CoDrone_mini
import time

drone = CoDrone_mini.CoDrone()
drone.pair()

drone.set_trim(15, 45)
time.sleep(1)

drone.takeoff()
drone.set_pitch(20)
drone.move(1)
drone.set_pitch(0)
drone.set_roll(-20)
drone.move(2)

drone.land()

print(drone.get_battery_percentage())
drone.close()
