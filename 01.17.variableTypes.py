# String
# from position 2(included) to position 5(not included) 
# include start, not end
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
# Use negative indexes to start the slice from the end of the string
print(b[-5:-2])

# Upper case
a = "Hello, World! "
print(a.upper())
# Lower case
print(a.lower())
# Remove white space at the end
print(a.strip())
# Replace
print(a.replace("H", "J"))
# Splits the string into substrings if it finds instances of the separator
print(a.split(",")) # returns ['Hello', ' World!']

# string format
# cannot concat string and number. need to use format() to insert numver to text
# use {} as placeholder to add the text
age = 36
years="years old"
txt = "My name is John, and I am {} {}"
print(txt.format(age,years))

# use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# special character
print("Single Quote: \'")
print("New Line: \n")
print("Carriage Return: \r")
print("Tab: \t")
print("Backspace: \b")
print("Form Feed: \f")

# string methods
x="hello world"
print(len(x))
print(x.capitalize())
print(x.title())
print(x.lower())
# center: taking up the space of 20 characters, with x in the middle:
print(x.center(20))
print(x.count("o"))
print(x.encode())
print(x.endswith("d"))
# expand the length of tab
x="Hell\to"
print(x.expandtabs(3))
print(x.find("o"))
# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
x = "For only {price:.2f} dollars!"
print(x.format(price = 49))
x="hello world"
print(x.index("e"))
# check is all alphabet and number (white space so no)
print(x.isalnum())
print(x.isnumeric())
print(x.isdigit())
print(x.isascii())
print(x.isspace())
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
# A valid identifier cannot start with a number, or contain any spaces.
print(x.isidentifier())
# join tuple/anything iterable to string with given string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
# Return a 20 characters long, left justified version of the word "banana":
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
x="\t\tbanana\t\t"
print(x.strip())
print(x.lstrip())
print(x.rstrip())
# Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day"
print(txt.partition("bananas"))
print(txt.rfind("bananas"))
# splite with whitespace
print(txt.split())
# Splits the string at line breaks and returns a list
print(txt.splitlines())
print(txt.startswith("I"))

# Boolean
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# (), [], {}, "", the number 0, and the value None

# Arithmetic Operators
x=5
y=3
# Exponentiation
print(x ** y)
# Floor division
print(x // y)

# Assignment Operators
# bitwise XOR operation
x = 5  # binary: 0101
x ^= 3 # binary: 0011
print(x)  # Output: 6  # binary: 0110
# A right shift operation shifts the bits of a binary representation to the right by a specified number of positions
x = 16  # binary: 10000
x >>= 3  # binary: 00010
print(x)  # Output: 2

# Membership Operators
# x in y
# x not in y