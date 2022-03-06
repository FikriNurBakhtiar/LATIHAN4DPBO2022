class Job:
    __NIP = ""
    __companyName = ""
    __position = ""
    
    def __init__(self, NIP = "", companyName = "", position = ""):
        self.__NIP = NIP
        self.__companyName = companyName
        self.__position = position
        
    #Setter
    def setNIP(self, NIP):
        self.__NIP = NIP
        
    def setCompany(self, companyName):
        self.__companyName = companyName
        
    def setPosition(self, position):
        self.__position = position
        
    #Getter
    def getNIP(self):
        return self.__NIP

    def getCompany(self):
        return self.__companyName
    
    def getPosition(self):
        return self.__position
    