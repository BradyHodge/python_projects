import CoDrone_mini
import time

drone = CoDrone_mini.CoDrone()
drone.pair()

drone.set_trim(0, 70)
time.sleep(1)

drone.takeoff()


drone.land()

print(drone.get_battery_percentage())
drone.close()
