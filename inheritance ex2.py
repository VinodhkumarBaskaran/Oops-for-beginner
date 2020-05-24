
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

    def speak(self):
        print('I dont know what I will speak until I am categoried')



class Dog(Pet):# inheriting the pet class into cat class
    """    def __init__(self,name,age):
        self.name = name
        self.age = age """


    def speak(self):
        print('I am {} and I am {} years old and speak in Bark language'.format(self.name, self.age))



class Cat(Pet): # inheriting the pet class into cat class
    """
        Now what if the cat as other attributes say color rest are similar to parent class.
        In that case just use the attributes from the parent class and add the new attributes using
        __init__ method corresponding to this class.

        Do so we use a keyword/ function called as "Super()"
    """

    def __init__(self,name,age,color):
        super().__init__(name,age)
        """
            Above step will assign value self.name = name and self.age = age w.r.t this class
        """
        self.color = color

        """
            To add the additional information we do the above
        """

    def speak(self):
        print('I am {} and I am {} years old and speak in Meow language and I am {} color'.format(self.name,self.age,self.color))



p = Pet('Jim',25)
p.show()
p.speak()


c = Dog('dog',15)
c.show()
c.speak()

c = Cat('dog',15,'Black')
c.show()
c.speak()


"""
    what happens when the general class or the parent class have the same method name as the child class?
    
    Answer :  when the parent class is initialized and then method is called then it will do the 
               task declared in that method
               
               when the same method is called in the child class then method in the child class override the 
               parent method and execute the task declared in the child method
               
               
    eg : 
    
    p= Pet('Jim',25)
    p.show() ---> I am Jim and I am 25 years old
    p.speak()   ---> I dont know what I will speak until I am categoried
    
    # Parent class method speak is executed 
    
    c= Dog('Dog',15)
    c.show() ---> I am Dog and I am 15 years old
    c.speak() ---> I am Dog and I am 15 years old and speak in Meow language
    
    
    # When same method is called from the child class then parent method gets overridden
"""