######################################################################################################################
# Name: Marco Flores
# Date: 2018-01-12
# Description: 04 Fraction Enhance
######################################################################################################################
# defines a fraction
class Fraction(object):
    # constructor for the fraction class
    #   by default the fraction is 0/1
    def __init__(self, num = 0, den = 1):
        self.num = num
        if (den == 0):
            den = 1
        self.den = den
        self.reduce
    # getter for the numerator
    @property
    def num(self):
        return self._num

    # setter for the numerator
    @num.setter
    def num(self, val):
        self._num = val

    # getter for the denominator
    @property
    def den(self):
        return self._den

    # setter for the denominator
    @den.setter
    def den(self, val):
        # ignore if attempted denominator value is 0
        if (val != 0):
            self._den = val

    # returns a decimal approximation of the fraction
    def getReal(self):
        return float(self._num) / self._den

    # reduces a fraction to its simplest form
    def reduce(self):
        # assumes that the greatest common factor is 1
        gcf = 1
        # minimum function compares the numerator and denominator and returns the minumum value
        minimum = min(self.num, self.den)

        # find common factors
        for i in range(2, minimum+1):
            if(self.num % i == 0 and self.den % i == 0):
                gcf = i

        # divides the numerator and denominator by the greatest common factor
        self.num /= gcf
        self.den /= gcf

        # if the numerator is 0, the denominator is set to 1
        if (self.num == 0):
            self.den = 1

    # overloads the addition function for the fraction class
    def __add__(self, other):
        # cross multiplies the numerator and denominator of each fraction respectively to find a common denominator and adds each numerator
        num = (self.num * other.den) + (other.num * self.den)
        # sets the common denominator
        den = self.den * other.den

        # creates a new instance of the fraction class that represents the sum  of the two fractions
        sum = Fraction(num, den)
        # reduces the fraction
        sum.reduce()

        # returns sum
        return sum

    # overloads the subtraction function for the fraction class
    def __sub__(self, other):
        # cross multiplies the numerator and denominator of each fraction respectively to find a common denominator and subtracts each numerator
        num = (self.num * other.den) - (other.num * self.den)
        # sets the common denominator
        den = self.den * other.den

        # creates a new instance of the fraction class that represents the difference of the two fractions
        diff = Fraction(num, den)
        # reduces the fraction
        diff.reduce()

        # returns difference
        return diff

    # overloads the multiplication function for the fraction class
    def __mul__(self, other):
        # multiplies the numerators to find the numerator
        num = self.num * other.num
        # multiplies the denominator to find the denominator
        den = self.den * other.den

        # creates a new instance of the fraction class that represents the product of the two fractions
        prod = Fraction(num, den)
        # reduces the fraction
        prod.reduce()

        # returns product
        return prod

    # overloads the division function for the fraction class
    def __div__(self, other):
        # multiplies the first fraction by the reciprocal of the second
        num = self.num * other.den
        den = self.den * other.num

        # creates a new instance of the fraction class that represents the quotient of the two fractions
        quot = Fraction(num, den)
        # reduces the fraction
        quot.reduce()

        # returns the quotient
        return quot

    # returns a fraction's string representation
    def __str__(self):
        s = "{}/{} ({})".format(self.num, self.den, self.getReal())
        return s

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4
