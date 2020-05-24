class High:
    def __init__(self,read,write):
        self.read = read
        self.write = write


    def power(self):
        print('basic power like {} ,{}'.format(self.read,self.write))


class Emp(High):
    pass

class Manager(High):

    def __init__(self,read,write,update,delete):
        super().__init__(read,write)
        self.update = update
        self.delete = delete

    def power(self):
        print('basic and managerical power like {} ,{},{},{}'.format(self.read, self.write,self.update,self.delete))



e=Emp('read','write')
e.power()

m=Manager('read','write','update','delete')
m.power()