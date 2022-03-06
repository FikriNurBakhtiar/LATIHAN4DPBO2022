class Driver:
    __licenseID = ""
    __expire = ""
    __type = ""
    
    def __init__(self, licenseID = "", expire = "", type = ""):
        self.__licenseID = licenseID
        self.__expire = expire
        self.__type = type
        
    #Setter
    def setID(self, licenseID):
        self.__licenseID = licenseID
        
    def setExpire(self, expire):
        self.__expire = expire
        
    def setType(self, type):
        self.__type = type
        
    #Getter
    def getID(self):
        return self.__licenseID
    
    def getExpire(self):
        return self.__expire
    
    def getType(self):
        return self.__type