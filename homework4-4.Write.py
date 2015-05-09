import pickle

f = open("mypickles.txt", "bw")
mypickle = input("Please enter Name, Age and Country of Origin")
pickle.dump(mypickle, f)
f.close()