#customers classes using class and init method

class Customers:
    greeting = "Welcome to Coffee Palace!"  #--prints Welcome to Coffee Palace!
    
    def __init__ (self, name, beverage, food, total):
        self.name = "Customer name is " + name
        self.beverage = "Ordered beverages are " + beverage 
        self.food = "Ordered food is " + food
        self.total = "The total for that is $" + str(total)

#Customers information
print(Customers.greeting)
c_1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Iced Tea", "Blueberry pancakes", 315)

print("\n")

#Customer no. 2 Elaine
print(c_2.name)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)

# Customer name is Elaine
# Ordered beverages are Strawberry frappuccino
# Ordered food is Tuna wrap
# The total for that is $270

print("\n")

#Customer no. 4 Jerry
print(c_4.name)
print(c_4.beverage)
print(c_4.food)
print(c_4.total)

# Customer name is Jerry
# Ordered beverages are Caramel macchiato
# Ordered food is Glazed doughnut
# The total for that is $230

print("\n")

