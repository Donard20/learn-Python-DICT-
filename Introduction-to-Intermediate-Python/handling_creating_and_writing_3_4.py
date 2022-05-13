#handling,creating,and writing file challenge

#create file
f = open("why.txt", "x")

#write inside the files
f = open("why.txt", "w")
f.write("What do I like about learning Python")

#append new data
f = open("why.txt", "a")
f.write("\n What do I plan to do after learning Python")

#read my data
f = open("why.txt", "r")
print(f.read)
f.close()





