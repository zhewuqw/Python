class Animal:
    def __init__(self, name):
        self.name = name

    def guess_who_am_i(self):
        if self.name == "elephant":             #guess elephant
            hint = ["I have exceptional memory", "I am the largest land-living mammal in the world", "I have the longest nose"]
            print("I will give you 3 hints, guess what animal I am?")
            for i in range(len(hint)):          #use loop to guess
                print(hint[i])
                myguess = input("Who I am?")
                if myguess == self.name:        #get the right answer
                    print("you got it! I am", self.name)
                    break
                else:
                    print("Nope, try again")
                    if i == len(hint)-1:        #out of hints, then give the right answer
                        print("I'm out of hints! The answer is:", self.name)
        if self.name == "tiger":                #guess tiger
            hint = ["I am the biggest cat", "I come in black and white or orange and black", "I have long tail"]
            print("I will give you 3 hints, guess what animal I am?")
            for i in range(len(hint)):
                print(hint[i])
                myguess = input("Who I am?")
                if myguess == self.name:
                    print("you got it! I am", self.name)
                    break
                else:
                    print("Nope, try again")
                    if i == len(hint)-1:
                        print("I'm out of hints! The answer is:", self.name)
        if self.name == "bat":                  #guess bat
            hint = ["I use echo-location", "I can fly", "I see well in dark"]
            print("I will give you 3 hints, guess what animal I am?")
            for i in range(len(hint)):
                print(hint[i])
                myguess = input("Who I am?")
                if myguess == self.name:
                    print("you got it! I am", self.name)
                    break
                else:
                    print("Nope, try again")
                    if i == len(hint)-1:
                        print("I'm out of hints! The answer is:", self.name)


e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()


#-------------------------------simple output
#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/QW/Documents/UNH/untitled10/p8-1.py
#I will give you 3 hints, guess what animal I am?
#I have exceptional memory
#Who I am?dolphin
#Nope, try again
#I am the largest land-living mammal in the world
#Who I am?elephant
#you got it! I am elephant
#I will give you 3 hints, guess what animal I am?
#I am the biggest cat
#Who I am?lion
#Nope, try again
#I come in black and white or orange and black
#Who I am?tiger
#you got it! I am tiger
#I will give you 3 hints, guess what animal I am?
#I use echo-location
#Who I am?human
#Nope, try again
#I can fly
#Who I am?butterfly
#Nope, try again
#I see well in dark
#Who I am?cat
#Nope, try again
#I'm out of hints! The answer is: bat

#Process finished with exit code 0
