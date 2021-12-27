class Cat:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def speak(self):
        print(self.name+'speaks')


mycat = Cat('Tom','House cat','Black')

print(mycat.color)
print(mycat.name)
mycat.speak()
mycat2 = Cat('snowball','classic Russian','Black')
print(mycat2.name)
print(mycat2.color)
print(mycat2.speak())


#create a Account Class
#create a contructor which takes acc__no, holder__name, balance,data
#create two methods debits and credit.
# crite altlest three objects.

 