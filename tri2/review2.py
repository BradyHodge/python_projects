# A car was moving 20 miles per hour on a straight road.
# Every five minutes, it instantly decelerates by 5 miles per hour
# and keeps that speed for a minute,
# and then instantly accelerates back to 20 miles per hour.
# How many miles will the car cover if it moves like that for an hour?

time = 60
miles_change = 0
miles_normal = 0

for miles in range(time):
    if miles % 5 == 0:
        miles_change += 15/60 * 1
    else:
        miles_normal += 20/60 * 1
    total_miles = miles_change + miles_normal

print(total_miles)
