# print
print("hello world")

# condition, using indentation
if 5 > 2:
  print("Five is greater than two!")

# create variable, no command for declaring a variable.
# case sensetive
y = "Hello, World!"

''' Multi lines command 
'''
# casting: specify the data type of a variable
x=str(3)
y=int(3)
z=float(3)

# get type
print(type(x))
print(type(y))
print(type(z))

# assign multiple variables
x, y, z = "Orange", "Banana", "Cherry"

# one value for multiple variables
x=y=z="Orange"

# unpack a collections
fruits=["apple","orange","banana"]
x,y,z=fruits

# print multiple variables, like this ('apple', 'orange', 'banana')
print(x,y,z)

# concat, appleorangebanana
# do not support + for different variable type
print(x+y+z)

# global variable and function
x="global variable is a variable outside a function"
def myfunc():
  print("This is a global variable: "+x)
myfunc()

# local changes local, global remains the same
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# use global keyword, make the vairable to global scope
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


# Text Type:	str
x = "Hello World"
# Numeric Types:	int, float, complex
x = 20
x = 20.5	
# "j" as the imaginary part
x = 1j
# Sequence Types:	list, tuple, range
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
# Mapping Type:	dict
x = {"name" : "John", "age" : 36}
# Set Types:	set, frozenset
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
# Boolean Type:	bool
x= True
# Binary Types:	bytes, bytearray, memoryview
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
# None Type:	NoneType
x = None

# Random Number
import random
print(random.randrange(1, 10))

# Strings are Arrays, start from 0
a = "Hello, World!"
print(a[1])
# Loop though Array
for x in a:
  print(x)
# Get length of array
print(len(x))
# check string contains or not
txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)

# from position 2(included) to position 5(not included) 
# include start, not end
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
# Use negative indexes to start the slice from the end of the string
print(b[-5:-2])