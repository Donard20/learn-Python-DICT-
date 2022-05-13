#exceptions exrcises

#1
x = 500

if x > 100:
    raise Exception("Variable is bigger than expected")
print
Exception: Variable is bigger than expected

#2
try:
    print(variable_1)
except:
    print("Variable is not defined")
#print
# Variable is not defined

#3
for i in range(6):                     
    print("I'm so happy!")
# print
# I'm so happy!
# I'm so happy!
# I'm so happy!
# I'm so happy!
# I'm so happy!
# I'm so happy!

#4
try:
    print(12*6)
except:
    print("This operation can't be performed")
else:
    print("This operation can be performed")
#print
#72
# This operation can be performed

#5
best_burger = "Burger King"
number_2_burger = "McDonald's"

assert best_burger == "Burger King"
assert best_burger == "McDonald's"
#print
# AssertionError





