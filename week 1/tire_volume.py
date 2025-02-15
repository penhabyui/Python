import math
from datetime import datetime

width = int(input("Enter the width of the tire in mm: "))
ratio = int(input("Enter the aspect ratio of the tire: "))
diameter = int(input("Enter the diameter of the wheel in inches: "))

volume1 = math.pi *width**2 * ratio
volume2 = width * ratio + 2540 * diameter
total_volume = (volume1 * volume2)/10000000000 

print(f"The approximate volume is {total_volume:.2f} liters")

current_date_and_time = datetime.now()
with open("volume.txt", mode="at") as days_and_volumes:
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {total_volume:.2f}")