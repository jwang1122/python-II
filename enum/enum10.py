from enum import Enum
"""
Enum class is callable
"""

animal = Enum('Animal', 'ANT BEE CAT DOG')
print(type(animal))
print(animal.ANT)
print(animal.ANT.value)
print(list(animal))

animal1 = Enum('Animal', "(Horse,3) (PIG,4) (CHECKEN,5) (SHEEP,6)") # useless
print(list(animal1))
for a in animal:
    print(a)
print(animal.ANT)