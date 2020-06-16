# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # This is the base class for all
    pass


class FlightVehicle(Vehicle):
    # This is the parent class for Starship and Airplane
    pass


class Starship(FlightVehicle):
    pass


class Airplane(FlightVehicle):
    pass


class GroundVehicle(Vehicle):
    # This is the parent class for Car and Motorcycle
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass
