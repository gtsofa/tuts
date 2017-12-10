#model a dog

"""
a simple attempt to model a dog.
"""
class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in repsonse to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulate a dog rolling over """
        print(self.name.title() + " rolled over!")

my_dog = Dog('borris', 3)
my_dog.sit()
my_dog.roll_over()

print("The name of my dog is " + my_dog.name.title() + " and is "+ str(my_dog.age) + " years old.")
