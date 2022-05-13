#Coding challenge

#1
try:
    print(y)
except NameError:
    print("Whoops! Don't forget to define your variables.")
#print
# Whoops! Don't forget to define your variables.

# 2
# return the first 5 characters of the file
f = open("Hello.txt", "x")        #--create file
f = open("Hello.txt", "w")          #--add data in the file
f.write("Hello")

f = open("Hello.txt", "r")          #--read the file
print(f.read(5))
f.close()

# print
# Hello

# 3
print(154 + "twenty-one" + 33)          
##--TypeError: unsupported operand type(s) for +: 'int' and 'str

# 4
try:
    print(amount_of_strawberries)
except:
    print("Something's missing")
finally:                                ##--use finally to ignore error and proceed to printing
    print("It's fine, Let's print!")


























