from enum import Enum, auto


class Planet(Enum):
    MERCURY = (3.303e23, 2.4397e6)
    VENUS = (4.869e24, 6.0518e6)
    EARTH = (5.976e24, 6.37814e6)
    MARS = (6.421e23, 3.3972e6)
    JUPITER = (1.9e27, 7.1492e7)
    SATURN = (5.688e26, 6.0268e7)
    URANUS = (8.686e25, 2.5559e7)
    NEPTUNE = (1.024e26, 2.4746e7)

    def __init__(self, mass, radius):
        self.mass = mass  # in kilograms
        self.radius = radius  # in meters

    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300e-11
        return G * self.mass / (self.radius * self.radius)


if __name__ == "__main__":
    print("Earth Mass:%e, and Radios:%e" % Planet.EARTH.value)
    print(f"{Planet.EARTH.surface_gravity} m/s^2")