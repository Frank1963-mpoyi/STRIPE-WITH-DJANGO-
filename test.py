x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# is the way to handle our own exceptions


print("\n")
# import sys

# assert ('linux' in sys.platform), "This code runs on Linux only."

print(0/0))# this is syntax error

print("\n")
print(0/0) # Traceback this is an excption error beacuse the syntax was good
#The try and except block in Python is used to catch and handle exceptions. 

'''
As you saw earlier, when syntactically correct code runs into an error, 
Python will throw an exception error. This exception error will crash 
the program if it is unhandled. 

The except clause determines how your program responds to exceptions
'''

print(10 * (1/0))#ZeroDivisionError: division by zero

print( 4 + spam*3)#NameError: name 'spam' is not defined

print('2' + 2)#TypeError: Can't convert 'int' object to str implicitly
#The string printed as the exception type is the name of the built-in exception that occurred

