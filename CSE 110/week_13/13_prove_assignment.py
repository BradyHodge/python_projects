# Made by Brady Hodge
# CSE 110
# 13 Prove: Assignment - Wind Chill Calculations


def wind_chill_formula(temp, wind_speed):
    # Calculates the wind chill in Fahrenheit
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * wind_speed ** 0.16 + 0.4275 * temp * wind_speed ** 0.16
    return wind_chill

def celsius_to_fahrenheit(temp):
    # Converts Celsius to Fahrenheit
    temp = (temp * 9/5) + 32
    return temp

temp = float(input("What is the temperature? "))
temp_format = input("Fahrenheit of Celsius (F/C)? ").upper()

for x in range(5, 60, 5):
    wind_chill = wind_chill_formula(temp, x)

    if temp_format == "C":
        temp = celsius_to_fahrenheit(temp)
        temp_format = "F"

    if temp_format == "F":
        wind_chill = wind_chill_formula(temp, x)
        print(f"At temperature {temp:.2f}F and wind speed {x} mph, the wind chill is {wind_chill:.2f}F") 