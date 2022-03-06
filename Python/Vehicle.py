from Ship import Ship
from Airplane import Airplane

class Vehicle(Ship, Airplane):
    __fuelType = ""
    __maxPassengers = ""
    
    def __init__(self, fuelType = "", maxPassengers = ""):
        self.__fueType = fuelType
        self.__maxPassengers = maxPassengers
        
    #Setter
    def setFuel(self, fuelType):
        self.__fuelType = fuelType
        
    def setPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers
        
    #Getter
    def getFuel(self):
        return self.__fuelType
    
    def getPassengers(self):
        return self.__maxPassengers
    
    def ship(self):
        print("")
        print("This is My Specification Vehicle")
        print("Ship")
        print("Type                     : "+ str (self.getTypeS()))
        print("Age                      : "+ str (self.getAge()))
        print("Fuel Type                : "+ str (self.getFuel()))
        print("Max Passengers           : "+ str (self.getPassengers()))
        print("Country of Manufacture   : "+ str (self.getCountry()))
        
    def plane(self):
        print("")
        print("This is My Specification Vehicle")
        print("Air Plane")
        print("Type                     : "+ str (self.getTypeS()))
        print("Age                      : "+ str (self.getAgeA()))
        print("Wings Length             : "+ str (self.getWings()) + " M")
        print("Fuel Type                : "+ str (self.getFuel()))
        print("Max Passengers           : "+ str (self.getPassengers()))
    