
#------------using pop method-------------#

groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milk": 2, "oranges": 4}
print(groceries)
#print  {'chicken': 8, 'apples': 6, 'cucumbers': 3, 'milk': 2, 'oranges': 4}

groceries.pop("oranges")            #--removing the oranges
print(groceries)
#print  {'chicken': 8, 'apples': 6, 'cucumbers': 3, 'milk': 2}

#------------using keys method-------------#

speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}
print(speakers)
# print {'Sir Rafael': 54, 'Ms. Joan': 33, 'Ms. Dana': 67}

name = speakers.keys()      #--getting the keys method
print(name)          
#print dict_keys(['Sir Rafael', 'Ms. Joan', 'Ms. Dana'])

#------------using get method-------------#

swimming_team_tryout = {"Carl": "Passed", "Quentin": "Failed", "John Y.": "Passed",
                        "Peter": "Failed", "Max T.": "Passed", "Joseph": "Passed",
                        "Jone": " Failed", "Jorge": "Failed", "George": "Passed",
                        "Ben": "Passed", "Jerome": "Passed", "Rick": "Failed",
                        "Max G.": "Failed", "John P.": "Failed", "Vince": "Passed",}

best_friend = swimming_team_tryout.get("Jorge")     #-- used .get to get the particular value

print(best_friend)
#print Failed