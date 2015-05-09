import os
import fnmatch

start_dir = input("Please enter the start path:")   #to enter start path
file_name = input("Please enter the file name:")    #to enter file name
for dirpath, dirs, files in os.walk(start_dir):
    for single_file in files:
        if fnmatch.fnmatch(single_file, file_name): #find the match file
            f = open( os.path.join(dirpath, single_file) )
            for line in f:
                if "password=" in line:
                    print("find \"password=\" in the file") #find "passward="


#----------------simple output
#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/QW/Documents/UNH/untitled5/homework4-2.py
#Please enter the start path:/Users/QW/Documents/UNH
#Please enter the file name:test.txt
#find "password=" in the file

#Process finished with exit code 0
