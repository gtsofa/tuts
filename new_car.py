#a Car class
"""A class that can be ussed to represent a car."""


class Car():
    """A simple model to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 12 #0 or an empty string in the body of __init__method

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement to show the car's milege."""
        print("This car has " + str(self.odometer_reading) + " miles on it. ")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Sorry, but you cannot roll back an odometer!")
        #print("The updated value for mileage is " + str(self.odometer_reading) + " .")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        Reject negative increments so no one uses this function to roll back
        """
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Sorry, we don't allow negative miles.")

my_new_car = Car('audi', 'a4', 2016)
your_new_car = Car('subaru', 'outback', 2013)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(8)
my_new_car.read_odometer()

print(your_new_car.get_descriptive_name())
your_new_car.update_odometer(30000)
your_new_car.increment_odometer(-200)
your_new_car.read_odometer()
# my_new_car.odometer_reading = 23 #1-modify attribute value thro an instance.
# my_new_car.read_odometer()