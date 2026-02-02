#Wendolyn Gatica
#file name: M03_Vehicle_Gatica.py
#This program defines attributes of a Automobile class and prompts user for input

class Vehicle:
    def __init__(self, vType):
        self.vType = vType
class Automobile(Vehicle):
    def __init__(self, vType, year, make, model, doors, roof):
        super().__init__(vType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
carType = input("What type of vehicle? (car, truck, plane, boat, or broomstick)")
carYear = input("What year?")
carMake = input("What is the automible's make?")
carModel = input("What about the model?")
carDoors = input("How many doors?(2 or 4)")
carRoof = input("What kind of roof? (solid or sun roof)")

userCar = Automobile(carType, carYear, carMake, carModel, carDoors, carRoof)

print('\nVehicle type: ',userCar.vType,'\nYear: ',userCar.year,'\nMake: ',
      userCar.make,'\nModel: ',userCar.model,'\nNumber of doors: ',userCar.doors,'\nType of roof: ',userCar.roof)