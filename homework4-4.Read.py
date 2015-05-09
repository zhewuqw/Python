import pickle

f = open("mypickles.txt", "br")
mylist = pickle.load(f)
print(mylist)
f.close()