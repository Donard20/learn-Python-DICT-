


class ClubMembers:           #-- base of the code

    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal
    
    def display1(self):     #--printing method
        print("(parent class/ClubMembers)")
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)
        print("\n")

class ClubOfficers(ClubMembers):            #--subclass of the code

    def __init__(self, name, birthday, age, favorite_food, goal, position):   #--new arguments in parameter 'position' was added
        self.position = position                                              #--this is added to overide the init
        ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)  #--used to overide the old code
    
    def display2(self):                     #--display of the subclass
        print("(SubClass/ClubMembers)")
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)
        print("Position", self.position)                                      #--add in display

m_1 = ClubMembers("Tom", "January 16", str(14), "Ice Cream", "To be happy")  #--information 
o_4 = ClubOfficers("Vera", "June 22", str(16), "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

m_1.display1()          #--printing out the information 
o_4.display2()          #--printing out the information       

#print
# (parent class/ClubMembers)
# Name: Tom
# Birthday: January 16
# Age: 14
# Favorite food: Ice Cream
# Goal: To be happy


# (SubClass/ClubMembers)
# Name: Vera
# Birthday: June 22
# Age: 16
# Favorite food: Beef stroganoff       
# Goal: To be the world's greatest chef
# Position Treasurer









