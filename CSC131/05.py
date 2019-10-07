#########################################################
# Name: Marco Flores
# Date: 2018-1-27
# Description: Implements vehicle, truck and car classes.
# the vehicle class
#########################################################

# a vehicle has a year, make, and model
# a vehicle is instantiated with a make and model
class Vehicle(object):
    # a constructor for the Vehicle class that takes in and sets make and model
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.year = 2000

    # an accessor for the instance variable year
    @property
    def year(self):
        return self._year

    # a mutator for the instance variable year
    @year.setter
    def year(self, year):
        if (year >= 2000 and year <= 2018):
            self._year = year
        else:
            self._year = 2000

    # an accessor for the instance variable make
    @property
    def make(self):
        return self._make

    # a mutator for the instance variable make
    @make.setter
    def make(self, make):
        self._make = make

    # an accessor for the instance variable model
    @property
    def model(self):
        return self._model

    # a mutator for the instance variable model
    @model.setter
    def model(self, model):
        self._model = model

    # defines the print statement
    def __str__(self):
        s = "{} {} {}".format(self.year, self.make, self.model)
        return s

# the truck class
# a truck is a vehicle
# a truck is instantiated with a make and model
class Truck(Vehicle):
    # a constructor for the Truck class that takes in and sets make and model
    def __init__(self, make, model):
        super(Vehicle, self).__init__(make, model)

# the car class
# a car is a vehicle
# a car is instantiated with a make and model
class Car(Vehicle):
    # a constructor for the Car class that takes in and sets make and model
    def __init__(self, make, model):
        super(Vehicle, self).__init__(make, model)

# the Dodge Ram class
# a Dodge Ram is a truck
# a Dodge Ram is instantiated with a year
# all Dodge Rams have the same make and model
class DodgeRam(Truck):
    # a constructor for the DodgeRam class that takes in and sets year as well as sets make, model
    def __init__(self, year):
        super(Truck, self).__init__("Dodge", "Ram")
        self.year = year

# the Honda Civic class
# a Honda Civic is a car
# a Honda Civic is instantiated with a year
# all Honda Civics have the same make and model
class HondaCivic(Car):
    # a constructor for the HondaCivic class that takes in and sets year as well as sets make, model
    def __init__(self, year):
        super(Car, self).__init__("Honda", "Civic")
        self.year = year


# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
ram = DodgeRam(2016)
print ram

civic1 = HondaCivic(2007)
print civic1

civic2 = HondaCivic(1999)
print civic2
