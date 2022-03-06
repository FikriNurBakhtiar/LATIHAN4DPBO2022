class Airplane:
    __type = ""
    __age = 0
    __wingsLength = 0
    
    def __init__(self, type = "", age = 0, wingsLength = 0):
        self.__type = type
        self.__age = age
        self.__wingsLength = wingsLength
        
    #Setter
    def setTypeA(self, type):
        self.__type = type
    
    def setAgeA(self, age):
        self.__age = age
        
    def setWings(self, wingsLength):
        self.__wingsLength = wingsLength
        
    #Getter
    def getAgeA(self):
        return self.__age
    
    def getTypeA(self):
        return self.__type
    
    def getWings(self):
        return self.__wingsLength
    