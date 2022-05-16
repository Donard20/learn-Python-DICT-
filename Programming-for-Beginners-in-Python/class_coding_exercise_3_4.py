#your new cafe. "Coffee Palace" is an instant hit. Customers are pouring in and out every minute
#so far, you have two regular customers who seem to love buying from you cafe. They show up to eat breakfast everyday and they always order the same things.
# using classes, lets try to save their orders

#create class called "customers"
#name    | beverage         | food          | total
#Samirah | Iced caffe latte | Cinnamon roll | 225
#Jerry   | Caramel macchiato| Glazed dougnut| 230 

#create class variable name "greeting" with the value "Welcome to the Coffee Palace!"

#Create instance variables for Samirah and Jerry. (ex. c_1)
#Include the attributes listed on the table. (ex. c_1.name)
#Type print(Customers.greeting)
#What does Samirah want to drink? Print her beverage on the console.
#What does Jerry want to eat?Print his food on the console

# greeting = "Welcome to the Coffee Palace!"

class Customers: 
    greeting = "Welcome to the Coffee Palace!"
    pass

#customer 1
c_1 = Customers()
c_1.name = "Samirah"
c_1.beverage = "Iced caffe latte"
c_1.food = "Cinnamon roll"
c_1.total = int(225)

#customer 2
c_2 = Customers()
c_2.name = "Jerry"
c_2.beverage = "Caramel macchiato"
c_2.food = "Glazed dougnut"
c_2.total = int(230)

#print data
print(Customers.greeting)
print("What", c_1.name, "want to drink?", c_1.beverage + "!", "for $" + str(c_1.total))
print("What", c_2.name, "want to drink?", c_1.food + "!", "for $" +  str(c_2.total))

# Welcome to the Coffee Palace!
# What Samirah want to drink? Iced caffe latte! for $225
# What Jerry want to drink? Cinnamon roll! for $230
