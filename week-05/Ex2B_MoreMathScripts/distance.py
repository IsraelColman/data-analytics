# Israel Colman
# distance.py
# 11/10/2026

# distance between (x1,y1) and (x2,y2)
import math

x1 = 3
y1 = 4
x2 = 7
y2 = 1

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between (x1,y1) and (x2,y2) is {distance:.2f}")