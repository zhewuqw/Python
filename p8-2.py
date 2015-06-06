from random import randrange


while True:
    a = randrange(5)
    b = randrange(1, 5)
    print("INTEGER DIVISIONS")
    try:
        answer = int(input("{}/{}=".format(a, b)))
        if a//b == answer:
            print("CORRECT")
        else:
            print("INCORRECT")
        play = input("Do you want to answer again?")
        if play == "no":
            break
    except ValueError:
        print("Please enter integers only")

    except:
        print("Error Occured")

#--------------------------simple output
#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/QW/Documents/UNH/untitled10/p8-2.py
#INTEGER DIVISIONS
#2/2=1
#CORRECT
#Do you want to answer again?yes
#INTEGER DIVISIONS
#0/4=0
#CORRECT
#Do you want to answer again?yes
#INTEGER DIVISIONS
#3/1=3
#CORRECT
#Do you want to answer again?yes
#INTEGER DIVISIONS
#1/4=w
#Please enter integers only
#INTEGER DIVISIONS
#0/1=0
#CORRECT
#Do you want to answer again?no

#Process finished with exit code 0
