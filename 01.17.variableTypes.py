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

# string