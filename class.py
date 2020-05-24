"""
Lets understand class and some attributes of class in python
"""
import datetime
# My commom meth one used use camelcase when writing the class name say Dog, BalanceAfterTransaction...
class Dog():

    def __init__(self,name,year):
        self.name = name
        self.year = year

    """
        __init__ method is like a constructor which gets excluded when the class is initialized
    """

    def bark(self):
        print(self.name + ' is barking')

    """
        Purpose of self as one of the parameter in the method is because we can 
        reuse the things which we store using __init__ method else where in the program
    """

    def love(self,human):
        print(self.name + ' is very affectionate to his owner name ' + human)


    def AgeCal(self):
        age = int(datetime.datetime.now().year) - self.year
        print('Age of '+ self.name + ' is ' + str(age))

"""
    one can initialize n number of object using the class function
"""
d= Dog('jim',2015)

d.bark()
d.love('Peter')

d.love('houn')


d1= Dog('Tim',2018)

d1.bark()
d1.love('bell')

"""
    mathematical operation in class (ref : AgeCal method)
"""

d.AgeCal()