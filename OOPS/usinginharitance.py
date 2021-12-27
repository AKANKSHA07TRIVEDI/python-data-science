class Computer:

    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
    def getDetails(self):
        print('from Computer class')
class Laptop(Computer):
    def __init__(self, cpu, storage, screen, touch):
        super().__init__(cpu, ram, storage)
        self.scren =screen
        self.touch = touch 
comp = Computer ("13","8 GB","500 GB")
print(comp.ram)
print(comp.cpu)
comp.getDetails()      
lappy =Laptop('i5','16gb','256','500 GB')