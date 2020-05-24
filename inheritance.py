
"""

    Do you see __init__ method of both class cat and Dog takes similar arguments
    so instead of writing is twice we can create a class with only __init__ method
    and argument and reuse it whereever we want it.

"""

class Pet: # generalised class

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print('I am {} and I am {} years old'.format(self.name,self.age))




class Cat(Pet): # inheriting the pet class into cat class
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age"""


    def speak(self):
        print('I am {} and I am {} years old and speak in Meow language'.format(self.name,self.age))


class Dog(Pet):# inheriting the pet class into cat class
    """    def __init__(self,name,age):
        self.name = name
        self.age = age """


    def speak(self):
        print('I am {} and I am {} years old and speak in Bark language'.format(self.name, self.age))



P= Pet('Jim',25)
P.show()


c= Cat('Cat',15)
c.show()
c.speak()