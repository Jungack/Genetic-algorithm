class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName;
        self.lastName = lastName;
        self.age = age;

class IDCard(Person):
    def __init__(self, firstName, lastName, age, height, eyeColour):
        Person.__init__(self, firstName, lastName, age)
        self.height = height
        self.eyeColour = eyeColour

    def presentation(self):
        print("Fist Name : ", self.firstName, "\nLast Name : ", self.lastName, "\nAge : ", self.age)

    def getHeight(self):
        return self.height

    def growUp(self, cms) :
        self.height += cms
        print("The person is now "+str(self.getHeight())+" cms tall.")

class Tastes(Person):
    def __init__(self, food, sport):
        Person.__init__(self, firstName, lastName, age)
        self.food = food
        self.sport = sport

    def getFavouriteFood(self):
        return self.food

    def eatFood(self):
        print("You take a big chunk of tasty"+self.getFavouriteFood())

    def practiceSport(self):
        print("I have well trained today!")
