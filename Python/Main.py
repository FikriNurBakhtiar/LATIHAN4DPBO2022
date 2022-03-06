from Vehicle import Vehicle
from Person import Person

#First Person
firstP = Person()
firstV = Vehicle()

firstP.setNIK(123761287318)
firstP.setName("Ahmad Juanda")
firstP.setGender("Male")
firstP.setNIP(9871239)
firstP.setCompany("Astoran NET")
firstP.setPosition("Operator")
firstP.setID(123123)
firstP.setExpire("June 2090")
firstP.setType("A")

firstV.setFuel("Premium")
firstV.setPassengers(3)
firstV.setAge(10)
firstV.setTypeS("K012")
firstV.setCountry("Canada")

print("First Person")
firstP.ID()
firstV.ship()
print("")

#Second Person
secondP = Person()

secondP.setNIK(12937129)
secondP.setName("Jamilah")
secondP.setGender("Female")
secondP.setNIP(9871221319)
secondP.setCompany("Astorsi INC")
secondP.setPosition("HRD")
secondP.setID(1231214213)
secondP.setExpire("June 2030")
secondP.setType("B")

print("Second Person")
secondP.ID()
print("")

#Third Person
thirdP = Person()
thirdV = Vehicle()

thirdP.setNIK(12123132)
thirdP.setName("Dzull")
thirdP.setGender("Male")
thirdP.setNIP(9871239)
thirdP.setCompany("IndoChem")
thirdP.setPosition("Security")
thirdP.setID(1812976)
thirdP.setExpire("July 2035")
thirdP.setType("B")

thirdV.setFuel("Avtur")
thirdV.setPassengers(16)
thirdV.setAgeA(3)
thirdV.setTypeS("Boeing 737")
thirdV.setWings(20)

print("Third Person")
thirdP.ID()
thirdV.plane()
print("")

#Fourth Person
fourthP = Person()

fourthP.setNIK(22978123)
fourthP.setName("Annas")
fourthP.setGender("Male")
fourthP.setNIP(241123912)
fourthP.setCompany("Berkah Jaya")
fourthP.setPosition("Owner")
fourthP.setID(1231241111)
fourthP.setExpire("June 2025")
fourthP.setType("C")

print("Fourth Person")
fourthP.ID()
print("")

#Fifth Person
fifthP = Person()
fifthV = Vehicle()

fifthP.setNIK(1249898619)
fifthP.setName("Munisaa")
fifthP.setGender("Female")
fifthP.setNIP(9871239)
fifthP.setCompany("APP Mart")
fifthP.setPosition("Designer")
fifthP.setID(2141242)
fifthP.setExpire("July 2044")
fifthP.setType("C")

fifthV.setFuel("Avtur")
fifthV.setPassengers(21)
fifthV.setAgeA(10)
fifthV.setTypeS("Airbus A320")
fifthV.setWings(18)

print("Fifth Person")
fifthP.ID()
fifthV.plane()
print("")