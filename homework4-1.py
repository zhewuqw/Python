import os
import fnmatch

start_dir = input("Please enter the start path:")   #to enter start path
file_name = input("Please enter the file name:")    #to enter file name
for dirpath, dirs, files in os.walk(start_dir):
    for single_file in files:
        if fnmatch.fnmatch(single_file, file_name): #find the match file
            print(os.path.join(dirpath, single_file)) #print full path

#-------------------simple output

#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/QW/Documents/UNH/untitled4/homework4-1.py
#Please enter the start path:/Users/QW/Documents/UNH
#Please enter the file name:test.txt
#/Users/QW/Documents/UNH/untitled4/test.txt

#Process finished with exit code 0
