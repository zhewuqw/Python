def ears_cout(n):
    if n == 0:
        return 0
    elif n % 2 == 0:        #To count even bunnies
        return ears_cout(n - 1) + 3
    else:                   #To count odd bunnies
        return ears_cout(n - 1) + 2

print("How many bunnies in a line?")
n = int ( input() )
m = ears_cout(n)
print("There are total",m,"ears")


#--------------------------simple output1
#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/QW/Documents/classtest/classtest.py
#How many bunnies in a line?
#0
#There are total 0 ears

#Process finished with exit code 0
#--------------------------simple output2
#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/QW/Documents/classtest/classtest.py
#How many bunnies in a line?
#5
#There are total 12 ears

#Process finished with exit code 0

