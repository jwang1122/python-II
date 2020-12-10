from enum import Enum
"""
Enum class is callable
"""

animal = Enum('Animal', 'ANT BEE CAT DOG')
print(type(animal))
print(animal.ANT)
print(animal.ANT.value)
print(list(animal))

animal1 = Enum('Animal', "(Horse,3) (PIG,4), (CHECKEN,5), (SHEEP,6)")
print(list(animal1))

