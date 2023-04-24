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
    num : float
    den : float

    def __init__(self, new_num : float, new_den : float) -> None:
        self.num = new_num
        self.den = new_den

    def __add__(self, other):
        return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)
    def __eq__(self, other):
        return (self.num * other.den == self.den * other.num)
    
    def __str__(self):
        return str(self.num) +  "/" + str(self.den)


def main_one():
    mb = MountainBike(3, 100, 25)
    print(mb.to_string())

def main_two():
    f1 = Fraction (3, 7)
    f2 = Fraction (2, 5)
    f3 = Fraction (1, 3)
    f4 = Fraction (2, 6)
    result = f1 + f2 * f3
    print(result)
    if (f1 == f3):
        print("f1 and f3 are the same")
    else:
        print("f1 and f3 not equal")
    if (f3 == f4):
        print("f3 and f4 are the same")
    else:
        print("f3 and f4 not equal")


if __name__ == "__main__":
    selection = int(input("Which task would you like to run? Type 1 or 2: "))
    if (selection == 1):
        main_one()
    elif (selection == 2):
        main_two()