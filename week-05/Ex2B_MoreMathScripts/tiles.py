# Israel Colman
# tiles.py
# 11/10/2026

# how many boxes of tiles do i need?
import math

length = 15
width = 10

tiles_needed = length * width

boxes_needed = math.ceil(tiles_needed / 12)

tiles_with_extra = tiles_needed * 1.10

total_boxes = math.ceil(tiles_with_extra / 12)

print(f"Tiles needed: {tiles_needed:.0f}")
print(f"Boxes needed: {boxes_needed}")
print(f"Total boxes with 10% extra: {total_boxes}")