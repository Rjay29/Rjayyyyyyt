# STRINGS

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

# STRINGLENGTH
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# SLICING
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])


# MODIFY
# split
a = "Hello, World!"
print(a.split(","))
# replace
a = "Hello, World!"
print(a.replace("H", "J"))
# upper
a = "Hello, World!"
print(a.upper())
# lower
a = "Hello, World!"
print(a.lower())
# strip
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"


# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

##################################################################

# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value


##################################################################

# Boolean Values
print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False

print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x, int))

##################################################################

# Python Arithmetic Operators #

# +	    Addition	    x + y
# -	    Subtraction	    x - y
# *	    Multiplication	x * y
# /	    Division	    x / y
# %	    Modulus	        x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y

##################################################################

# Python Assignment Operators #

# Operator	Example	   Same As
#    =	    x = 5	   x = 5
#   +=      x += 3     x = x + 3
#   -=      x -= 3     x = x - 3
#   *=      x *= 3     x = x * 3
#   /=      x /= 3     x = x / 3
#   %=      x %= 3     x = x % 3
#   //=     x //= 3    x = x // 3
#   **=     x **= 3    x = x ** 3
#   &=      x &= 3     x = x & 3
#   |=      x |= 3     x = x | 3
#   ^=      x ^= 3     x = x ^ 3
#   >>=     x >>= 3    x = x >> 3
#   <<=     x <<= 3    x = x << 3
#   :=      print(x := 3)	x = 3
# print(x)


##################################################################

# Append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#################################################################

# loop list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	    Sorts the list
