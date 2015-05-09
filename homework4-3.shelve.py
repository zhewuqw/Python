import shelve
from datetime import datetime


s = shelve.open("myqutoes")
s = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
d1 = datetime.now()
print(s["Name"])
d2=datetime.now()
print(d2.microsecond-d1.microsecond)

#--------------simple output
#Zara
#28


