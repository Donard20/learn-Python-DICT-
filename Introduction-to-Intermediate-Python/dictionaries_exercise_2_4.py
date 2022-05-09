# Dictionaries

#list
flavor = ["vanilla", "chocolate", "strawberry", "cookies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]

#combining lists using zip and dict functions to create dictionaries
iced_cream = dict(zip(flavor, toppings))

print(iced_cream)
# print 
# {'vanilla': 'almonds', 'chocolate': 'banana slices', 'strawberry': 'chocolate syrup', "cookies n' cream": 'caramel syrup', 'bubblegum': 'white chocolate chips'}

#overwrite banana to blueberrries
iced_cream["chocolate"] = "blueberries"
print(iced_cream)
#print  -- change the chocolate: banana slices into blueberries
#{'vanilla': 'almonds', 'chocolate': 'blueberries', 'strawberry': 'chocolate syrup', "cookies n' cream": 'caramel syrup', 'bubblegum': 'white chocolate chips'}

#updateing flavors and toppings
iced_cream.update({"mathcha": "pistachios", "ube": "mango slices"})

print(iced_cream)
#print
#{'vanilla': 'almonds', 'chocolate': 'blueberries', 'strawberry': 'chocolate syrup', "cookies n' cream": 'caramel syrup', 'bubblegum': 'white chocolate chips', 'mathcha': 'pistachios', 'ube': 'mango slices'}







