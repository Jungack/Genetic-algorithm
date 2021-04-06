class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName;
        self.lastName = lastName;
        self.age = age;

class IDCard(Person):
    def __init__(self, height, eyeColour):
        self.height = height
        self.eyeColour = eyeColour
    def presentation(self):
        print("Fist Name : ", self.firstName, "\n Last Name : ", self.lastName, "\n Age : ", self.age)

class Tastes(Person):
    def __init__(self, food, sport):
        self.food = food
        self.sport = sport