class vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.
    Attributes:
    wheels: An integer representing the number of wheels the vehicle has.
    miles: The integral number of miles driven on the vehicle.
    make: The make of the vehicle as a string.
    model: The model of the vehicle as a string.
    year: The integral year the vehicle was built.
    sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float."""
        if self.sold_on is not None:
            return 0.0 #Already sold
        return 5000 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is not None:
            return 0.0 #Not yet sold
        return self.base_sale_price - (.10 * self.miles)
    @abstractmethod
    def vehicle_type():
        """Return a string representing the type of a vehicle this is."""
        pass
