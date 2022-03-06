from Job import Job
from Driver import Driver

class Person(Job, Driver):
    __NIK = ""
    __name = ""
    __gender = ""
    
    def __init__(self, NIK = "", name = "", gender = ""):
        self.__NIK = NIK
        self.__name = name 
        self.__gender = gender 
        
    #Setter
    def setNIK(self, NIK):
        self.__NIK = NIK
        
    def setName(self, name):
        self.__name = name 
        
    def setGender(self, gender):
        self.__gender = gender 
        
    #Getter
    
    def getNIK(self):
        return self.__NIK 
    
    def getName(self):
        return self.__name 
    
    def getGender(self):
        return self.__gender
    
    def ID(self):
        print("Personal Information")
        print("NIK              : "+ str (self.getNIK()))
        print("Name             : "+ str (self.getName()))
        print("Gender           : "+ str (self.getGender()))
        print("")
        print("Dirver License")
        print("Lisence ID       : "+ str (self.getID()))
        print("Active Until     : "+ str (self.getExpire()))
        print("Vehicle Type     : "+ str (self.getType()))
        print("")
        print("Job Informatian")
        print("NIP              : "+ str (self.getNIP()))
        print("Company Name     : "+ str (self.getCompany()))
        print("Position         : "+ str (self.getPosition()))