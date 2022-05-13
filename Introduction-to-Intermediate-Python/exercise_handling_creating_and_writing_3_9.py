
# f = open("Hello.txt", "x")
f = open("Hello.txt", "w")
f.write("First time?")

f = open("Hello.txt", "a")
f.write("\nSecond time?")
f.write("\nThird time?")

f = open("Hello.txt", "r")
for x in f:
    print(x)
f.close()


#removing the file
import os

#checking if the file exist
# if os.path.exists("Hello.txt"):
#     os.remove("Hello.txt")
# else:
#     print("The file 'Hello.txt' does not exist)

os.remove("Hello.txt")





