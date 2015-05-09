from datetime import datetime

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
d1 = datetime.now()
print(dict['Name'])
d2=datetime.now()
print(d2.microsecond-d1.microsecond)

#------------simple output
#Zara
#21