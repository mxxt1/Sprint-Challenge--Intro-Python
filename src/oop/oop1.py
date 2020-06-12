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
    #base
    pass

class FlightVehicle(Vehicle):
    #base Vehicle
    pass

class Airplane(FlightVehicle):
    #base Vehicle--> FlightVehicle
    pass

class Starship(FlightVehicle):
    #base Vehicle --> FlightVehicle
    pass

class GroundVehicle(Vehicle):
    #base Vehicle
    pass

class Car(GroundVehicle):
    #base Vehicle --> GroundVehicle
    pass

class Motorcycle(GroundVehicle):
    #base Vehicle--> GroundVehicle
    pass