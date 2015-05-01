def count_frequency( mylist ):
    k = [ None ] * len( mylist )         #To create a new list
    for i in range( len(mylist ) ):
        k[i] = mylist.count( mylist[i] )    #To count word appears times
    mylist = dict( zip(mylist, k ) )        #To create dictionary
    return mylist

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven", ]
print( count_frequency( mylist ) )

#------------------------------------------simple output
#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/QW/Documents/UNH/untitled/homewirk3-2.py
#{'eleven': 3, 'seven': 1, 'two': 2, 'one': 2, 'three': 2}

#Process finished with exit code 0
