# from turtle import color
# from unicodedata import name


# class dog:
#     attr1='mamal'
#     arrt2='dog'
    
#     def fun(self):
#         print('i am a ',self.attr1)
#         print('i am a ',self.arrt2)
# dogname=dog()

# print(dogname.attr1)
# dogname.fun()

# #constructor in python

# class person:
#     def __init__(self,name):
#         self.name=name
#     def say_hi(self):
#         print('hellon my name is ', self.name)

# p= person('khalidahmad')
# p.say_hi()

#class variables and instance variable
class dog:
    #class variable
    animal='dog'

    def __init__(self,breed):
        #instance variable
        self.breed=breed
        #or
        newbreed=breed
    
    def setcolor(self,color):
        self.color=color

    def getcolor(self):
        return self.color


dog1=dog('pug')
dog1.setcolor('red')
print(dog1.getcolor())
#we can also access to class variable by class name
print(dog.animal)

class addition:
    num1=0
    num2=0
    ans=0

    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def calculate(self):
        self.ans=self.num1+self.num2
    
    def desplay(self):
        print("the answer is =  " +str(self.ans))

obj= addition(1000,2000)
obj.calculate()
obj.desplay()


#destructor in python
class employee:

    def __init__(self):
        print('employee creted')

    def __del__(self):
        print('destructor called, employee deleted')

obj=employee()

#inheritence

class animal:

    def sound(self):
        print('the anumals has sound')
class cat(animal):
    def mows(self):
        print('the cats mouws')

obj=cat()
obj.sound()
obj.mows()

#multilevel inheritence
class animal:

    def sound(self):
        print('the anumals has sound')
class cat(animal):
    def mows(self):
        print('the cats mouws')
class catchild(cat):
    def eat(self):
        print('eating breads')

obj=catchild()
obj.sound()
obj.mows()
obj.eat()

#encapsulation in python

class car:
    def __init__(self) -> None:
        self.__maxprice=10000
    def sell(self):
        print("the max price is ",self.__maxprice)
    def setmaxprice(self,max):
        self.__maxprice=max

obj=car()
obj.sell()
#we can not access the private attribute by class object
obj.__maxprice=20000
obj.sell()

obj.setmaxprice(50000)
obj.sell()


#abstruction that hide the internal delails only show the functionality
class car:
    def mileage(self):
        pass
class BMW(car):
    def mileage(self):
        print('the mileage is= 30km')
class Toyota(car):
    def mileage(self):
        print('the mileage is 50km')
class honda(car):
    def mileage(self):
        print('the mileage is 100km')

obj=BMW()
obj.mileage()
obj1=Toyota()
obj1.mileage()
obj2=honda()
obj2.mileage()





class person:
    def __init__(self,name):
        self.name=name
    def desplay(self):
        print(self.name)
class employee(person):
    def __init__(self, name):
        #we can use this to call the parent constractor
        person.__init__(self,name)
        #also this one
        super().__init__(name)
obj=employee('khalidahmad')
obj.desplay()


















































        



        















