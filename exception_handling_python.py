
# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# try:
#     print(x)
# except NameError:
#     print('Variable x in not defined')
# except:
#     print('Something else went wrong')

# # when an no error is raised the else block is executing

# try:
#     print('Hello ')
# except:
#     print('somthing went wrong')
# else:
#     print('nothing went wrong')

# # the finally block is executing when exception is raised or not
# try:
#     print(x)
# except:
#     print('something went wrong')
# finally:
#     print('the try except is finished')


# # file 
# try:
#     f=open('file.txt')
#     try:
#         f.write('my name is khalid ahmad')
#     except:
#         print('something went wrong when writing to the file')
#     finally:
#         f.close()
# except:
#     print('something went wrong when opening the file')


# # riased is used to raise an exception
# x='khalid'
# if not type(x) is int:
#     raise TypeError('only integers are allowed')


# email=input('Enter your email address: ')
# if not '@gmail.com' in email:
#     raise exception('your email should be a gmail account')
# else:
#     print('your email address is:   ',email)


x=input('enter first number: ')
y=input('enter second number: ')
try:  
    result=x/y
except:
    print('error is hundeled')



class networkerror(RuntimeError):
    def __init__(self, args):
        self.arg=args
    
try:
    raise networkerror('Bad hostname')
except networkerror :
    print(arg)
        


























