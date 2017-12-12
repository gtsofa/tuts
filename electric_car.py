#electric car - to impliment inheritance

#a Car class
"""A class to represent a car model"""

class Car():

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

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then Initialize the attributes specific to electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    #call functions now
my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()