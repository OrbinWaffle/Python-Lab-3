# Name: Joshua Lai
# Lab 10
# Completed 4/24/2022

# Base class
class Bicycle:
    gear : int
    speed : int
    
    def __init__(self, new_gear : int, new_speed : int) -> None:
        self.gear = new_gear
        self.speed = new_speed
    
    def apply_brake(self, decrement : int):
        self.speed += decrement
    
    def speed_up(self, increment : int):
        speed += increment
    
    def to_string(self) -> str:
        return ("No of gears are " + str(self.gear) + "\n" + "speed of bicycle is " + str(self.speed))

# Inherits from Bicyle
class MountainBike(Bicycle):
    seat_height : int

    def __init__(self, new_gear: int, new_speed: int, start_height: int) -> None:
        super().__init__(new_gear, new_speed)
        self.seat_height = start_height
    
    def set_height(self, new_height : int):
        self.seat_height = new_height
    
    def to_string(self) -> str:
        return super().to_string() + ("\nseat height is " + str(self.seat_height))

class Fraction:
    pass


if __name__ == "__main__":
    mb = MountainBike(3, 100, 25)
    print(mb.to_string())