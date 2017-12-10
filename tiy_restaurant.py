#A class Restaurant

class Restaurant():
    """A class to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() +
         " and has " + self.cuisine_type.title() + " type of cuisine.")

    def open_restaurant(self):
        print( self.restaurant_name + " is now open.")

restaurant = Restaurant('mapango', 'bolognese crusione')
restaurant.open_restaurant()
restaurant.describe_restaurant()

print(restaurant.restaurant_name.title() + " is a new restaurant in Watamu")