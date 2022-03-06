class Ship:
    __age = ""
    __type = ""
    __countryOfManufacture = ""
    
    def __init__(self, age = 0, type = "", countryOfManufacture = ""):
        self.__age = age
        self.__type = type
        self.__countryOfManufacture = countryOfManufacture       
        
    #Setter
    def setAge(self, age):
        self.__age = age
        
    def setTypeS(self, type):
        self.__type = type
        
    def setCountry(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture       
        
    #Getter
    def getAge(self):
        return self.__age
    
    def getTypeS(self):
        return self.__type
    
    def getCountry(self):
        return self.__countryOfManufacture 
    
    
        