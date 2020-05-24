class Person:

    x=0

    def __init__(self,name):
        self.name = name



p=Person('Raven')
p1=Person('Dart')
print(p.x)
print(p1.x)

Person.x=9
print(p1.x)
print(p.x)

"""
Example 2
"""

class Personn:

    x=0

    def __init__(self,name):
        self.name = name
        Personn.x += 1 # Increase as the number of initialization increase


print(' ')
print('Example 2')
print(' ')
p=Personn('Raven')
print(p.x)
p1=Personn('Dart')
print(p1.x)



"""
Class attributes is not much useful but useful when we are using the some constant value across the the project

say light speed,km to m conversion
"""