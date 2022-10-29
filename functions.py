# a simple python function



def fun():
    print('welcome to our new works in python')
fun()

#functuon with parameters and return type and defalt argument
def add(num1:int ,num2:int =10)->int:
    num3=num1+num2
    return num3

num1,num2=5,8
ans=add(num1)
print('the addition of ',num1,'+ ',num2,'=   ',ans)


#keywork argument

def student(firstname,lastname):
    print(firstname,'  ',lastname)

student(firstname='khalidahmad',lastname='mubaraze')

#passing several arg in one variable
def myfunc(*arg):
    for arg1 in arg:
        print(arg1)
myfunc('khalid','khan','ahmadjan')


def evenodd(x):
    """his is the docstring function in python that print first string after function"""
    if (x%2==0):
        print('even')
    else:
        print('odd')
print(evenodd.__doc__)

#if we pass variale name in python it is pass by refrence
def swap(a,b):
    temp=a
    a=b
    b=temp
    print(a,b)

x=2
y=3
swap(x,y)
print(x,y)

#anonymouse function in python (function without def)
def cube(x):return x*x*x

cube2=lambda x: x*x*x
print(cube(7))
print(cube2(7))

#nisted functuons or function inside function
def f1():
    s='i love coding with python'
    def f2():
        print(s)
    f2()
f1()


#we can pass a function as argument in other functions
def f1(text):
    return text.upper()

def f2(text):
    return text.lower()

def great(func):
    greating=func('hi i am khalid ahmad')
    print(greating)

great(f1)
great(f2)































