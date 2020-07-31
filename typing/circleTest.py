import circle
from typing import Any

r:int = 2
x = circle.circle_area(r)
print(f"\nThe circle area with radius {r} is {x}.")
print('Dictionary of Annotations for circle_area():', circle.circle_area.__annotations__)