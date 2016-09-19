import random

print ('Print this line')
print ("Please?")
#print "This won't print"

print ("Now that we can print, let's move on to numbers.")

# For integers...
myInt = 7
print (myInt)

# For floats...
myFloat = 5
print (myFloat)

myFloat = float(5)
print (myFloat)
# Either way works.

myFloat = float(10)
print (myFloat)

# To define strings, you can use either single or double quotes

myString = 'Hello'
print (myString)

myString = "Hi"
print (myString)

print ("Go to Hell, Balloon Boy.")

# On to more numbers
num1 = 1
num2 = 6
num3 = num1 + num2
print (num3)

# How to add strings
str1 = "This is how"
str2 = "to add strings"
str3 = str1 + " " + str2 + "."
print (str3)

# You can assign variables on the same line, similar to initiating a list in C++
a, b = 3, 4

# The same applies to printing
print (a, b)

# You can NOT mix operators between different data types
"print (num1 + num2 + str3)"
print ("If you see the above line of code in the output menu, you're an idiot...")

# Lists
# Lists are VERY simple in Python compared to C++
myList = []
# Viala. The list has been created. Adding things to the list is easy, too.
myList.append(1)
myList.append(5)
myList.append(72)
# Printing lists is also easy. Just remember: COMPUTERS START AT 0!!!
print(myList[0])
print(myList[1])
print(myList[2])
# No more long for loops in C++ to print the entire list! The for loop is MUCH simpler!
for x in myList:
    print (x)

# You can initialize lists when you create them
myColors = ["Blue", "Yellow", "White"]
print (myColors)

print (myColors[0])
print (myColors[2])

# Slicing is a way to print only parts of a list
#slicendice
Z = ['yellow', 'red', 'blue', 'green', 'black']
print (Z[1:4]) # Begin at sub 1, terminate before sub 4
print (Z[2:])  # Begin at sub 2, go through rest of the list
print (Z[:2])  # Start at beginning, stop when it hits sub 2
print (Z[-1])  # Print the last item in the list
print (Z[1:-1])# Start at sub 1, terminate before end of list

# To print the length of the list...
print (len(Z))
print (len(myColors))

# To sort the list...
print (sorted(Z)) # Note: after sorting, it will revert to its previous state!

# To add to the end of the list...
Z.append("pink")
print (Z)

# To insert to list
Z.insert(0, "white")
print (Z)

# To remove from list
Z.remove("white")
print (Z)

# You can also delete something from the list by specifying its index number rather than its value
del(Z[0])
print (Z)

# Other list operations include:
# Pop
#    Z.pop()
#    Z.pop(1)
# Reverse
#    Z.reverse()
# Count - how many instances of the specified variable?
#    Z.count("red")
#    Can be used with keyword "in" to test if it's in the list
#       if 'red' in Z:
#          print ("list contains", 'red')
# for-in can be used to loop through list
#    for item in Z:
#       print (item)
#    L = ['red', 'green', 'blue']
#    for col in L:
#       print col

print ("Ok, enough about lists! Let's get back to numbers PLEASE!!!")

# Math operations, as always (Remember order of operations)
number = 1 + 2 * 3 / 4.0
print (number)

# Modulo % (Dividend % Divisor = Remainder)
rem = 5 % 2
print (rem)

# Using a ** operator acts as the power (num1 ** num2 = Num 1 TO THE POWER OF num2)
square = 4 ** 2
print (square)
cube = 5  ** 3
print (cube)

# Python can not only add strings, but it can also multiply strings
BB = "Ha ha ha! " * 10
print (BB)

print ("BB! I'm going to kick your ass!!!")

# Lists can be joined with operators
even_nums = [2, 4, 6, 8]
odd_nums = [1, 3, 5, 7]
all_nums = even_nums + odd_nums

print (even_nums)
print (odd_nums)
print (all_nums)

# Python can repeat lists the same as it can repeat strings
lotsanumbas = [1, 2, 3, 4, 5] * 5
print (lotsanumbas)

print ("Now we get into some interesting s***! How about we format strings?")

name = "Arbiter1223"
print ("Hello, %s!" % name) # Use %s for string, %d for double, etc.
age = 19
print ("%s is currently %d years old." % (name, age)) # Parameter data types must match, just like in function from C++

# %s can also be used to represent something in the form of a string
newList = [1, 2, 3]
print ("This, is a list: %s" % newList)

# %s - String (or anything to be represented as a string)
# %d - Integers
# %f - Floating point numbers
# %.<number-of-digits>f - Floating point numbers with a fixed amount of digits to the right of the dot; good for using with money
# %x/%X - Integers in HEX representation (lowercase/Capital)

# To create a string...
myString = "Duh..."

# To print a new string...
print (myString)

# THAT'S OLD SCHOOL!!! Now to print the length of a string!
print (len(myString))

print (myString.index("."))
# This prints where the FIRST instance of the character is in the string. Only the first instance is printed
# And again remember: COMPUTERS START WITH 0!!!

# To get how many characters there are, use the count method
print (myString.count("u"))

# Slices work the same way, but I'm not going to do that again... my eyes are tired enough as it is
print ("lol")

# To make all characters in a string capital (Uppercase for weirdos...) or lowercase, use the following respectively
print (myString.upper())
print (myString.lower())

print ("String * String = Rope")
# Ok, we'll get back to String Theory later. For now, let's get to comparisons.

x = 5
print (x == 5)
print (x == 4)
print (x < 0)

# AND and OR comparisons
name1 = "Garrett"
name2 = "Ril"
if name == "Arbiter1223" and age == 19:
    print ("Hello, %s. Welcome to your Desktop." % name)
if name1 == "Garrett" or name1 == "Ril":
    print ("Hello, %s. Welcome to the Squad." % name1)

# The IN operator can be used to see if something is in an object container, like a list
Squad = ["Arbiter1223", "IamthePiratecoveman", "Kris Minerman", "rilstorm4", "Perisquad-Ril"]
if name in Squad:
    print ("%s is part of Ril and the Squad." % name)

# The IS operator compares variables not by their contents but by the instances themselves
is1 = [1, 2, 3]
is2 = [1, 2, 3]
print (is1 == is2)
print (is1 is is2)

# The NOT operator is self-explanatory
print ("If you need help with NOT, you are NOT smart. XD")

# Loops
# Python has two different kinds of loops: for and while

# For loops occur over a certain amount of sequences
primes = [2, 3, 5, 7]
for prime in primes:
    print (prime)

# While loops occur indefinately as long as a certain condition is met
count = 0
while count < 10:
    print (count)
    count += 1

# Break and Continue statements are used in loops
# Break will exit the loop; a good failsafe to avoid infinite loops
count = 0
while True:
    print (count)
    count += 1
    if count >= 63:
        print ("WARNING! Infinite loop detected! Terminating loop.")
        break

# Continue is used to skip the current block and return to the for or while statement
yourList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for g in yourList:
    if g % 2 == 0:
        continue
    print (g)

# Ok, let's move on to dictionaries.
print ("Someone call Mr. Webster!")

# A dictionary is similar to a list but differs in the fact that it uses Keys instead of an Index
# This means that any type of object can be a key
# For example, a dictionary containing phone numbers could be saved like this:
phonebook = {} # Use curly brackets in creation only!
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

# Alternatively, a dictionary can be initializd with the same data
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781,
    "Cory" : 940733795,
    "Ril" : 123456789,
    "Mr. Webster" : 555555585
}

# Here is how to print the dictionary (use <namehere>.items():)
for name, number in phonebook.items():
    print ("Phone number of %s is %d" % (name, number))

# More ways to traverse a dictionary
d = {'x' : 1, 'y' : 2, 'z' : 3}
print (list(d))
print (d.keys())
print (d.items())

# Wednesday, September 14, 2016

# Classes

class point(object):

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x=%d, y=%d" % (self.x,self.y)

    def move(self,x,y):
        self.moveX(x)
        self.moveY(y)
    
class line(point):
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        p1 = point(x1,y1)
        p2 = point(x2,y2)


p = point(2, 6)
print (p)