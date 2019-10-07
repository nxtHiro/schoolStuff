######################################################################################################################
# Name: Marco Flores
# Date: 2017-12-13
# Description: 03 A Simple Vehicle Class
######################################################################################################################

# the vehicle class
# a vehicle has a year, make, and model
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

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
v1 = Vehicle("Dodge", "Ram")
v2 = Vehicle("Honda", "Odyssey")
print "v1={} {}".format(v1.make, v1.model)
print "v2={} {}".format(v2.make, v2.model)
print

v1.year = 2016
v2.year = 2016
print "v1={} {} {}".format(v1.year, v1.make, v1.model)
print "v2={} {} {}".format(v2.year, v2.make, v2.model)
print

v1.year = 1999
v2.model = "Civic"
v2.year = 2007
print "v1={} {} {}".format(v1.year, v1.make, v1.model)
print "v2={} {} {}".format(v2.year, v2.make, v2.model)
