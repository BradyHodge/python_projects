"""
Made by Brady Hodge
CSE 111
02 Checkpoint: Calling Functions
"""

import math

numb_items = int(input(f"Enter the number of items: "))
items_per_box = int(input(f"Enter the number of items per box: "))

numb_boxes = math.ceil(numb_items / items_per_box)

print(f"\nFor {numb_items} items, packing {items_per_box}"
    f" items in each box, you will need {numb_boxes} boxes.")