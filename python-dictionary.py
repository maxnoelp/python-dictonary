# import sys

# print(sys.version)

# if 5 > 2:
#   print("Five is greater than two!")

# if "Fynn" != "Fynn":
#   print("2 Personen!")
# else:
#   print("Python ist cool!")

# if 1 > 0:
#   print("Nice Work!")
# else:
#   print("Not a nice Work!")

# x = 5
# y = "Hello!"

# print(y, x)

# x = 5
# y = "John"
# z = 3.0
# print(type(x))
# print(type(y))
# print(type(z))


# e, r, t = "Python", "ist", "flexibel"

# print(e)
# print(r)
# print(t)

# a= b= c= "Python"

# print(a)
# print(b)
# print(c)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x = 5
# y = 10
# print(x * y)

# d = 32
# y = 12
# print(d / y)

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"
#   print("Python is " + x + ", simple")

# myfunc()

# x = 1
# y = 1.2e5
# z = 3+1j

# print(type(x)) #int
# print(type(y)) #float
# print(type(z)) #complex

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# import random
# print(random.randrange(1, 10))

# x=int(3.245)
# print(x)

# z=float(3)
# print(z)

# y=str(4567)
# print(y)
###################################################################################
# a = '''Lorem ipsum dolor sit amet, 
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.''' # 3 singlequotes/doublequotes für mehr zeilige stirngs
# print(a)

# a = "Hello, World!"
# print(a[0]) #um ein bestimmtes zeichen nur auszugeben

# for x in "banana":
#   print(x) #schleife die jeden Buchstaben einzel ausgibt

# a = "Hello, World!"
# print(len(a)) #gibt die länge aus

# txt = "The best things in life are free!"
# print("hallo" in txt) 
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.") #checked ob das Wort free im string enthalten ist!

# txt = "Hallo, Python ist wunderbar!"
# if "Vue" in txt:
#     print("'Python', ist dabei")
# else:
#     print("leider nein")

# txt = "The best things in life are free!"
# if "best" not in txt:
#   print("No, 'expensive' is NOT present.")
# else:
#   print("ausgehebelt")

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[-5:-2])
###################################################################################
# a = " Hello, World!"
# print(a.upper()) #Str in Großbuchstaben
# print(a.lower()) #Str in kleinbuchstaben
# print(a.strip()) #entfernt Whitespace am anfang und ende
# print(a.replace("Hello", "Ciao")) #ersetzt dass "hello" mit "ciao"
# print(a.split(",")) #splittet in ein Array
###############################String Concatenation##################################################

# a = "Hello"
# b = "World"
# c = a + " " + b #zusammenführen von zwei variablen mit einem Whitespace
# print(c)

##############################Format Strings###################################################

# age = 30
# txt = f"My name is Max, I am {age}" #f vor den string und mit Mustache die variable AGE in den String einbetten
# print(txt)

# speed = 200
# y = f"i ride over {speed}Km/h"
# print(y)

# price = 59
# txt = f"The price is {price:.2f} dollars" #.2f steht für 2 stellen nachdem komma, dezimalzahl
# print(txt)

# txt = f"The price is {20 * 59} dollars" #hier ist eine math funktion eingebaut um den Preis zu multiplizieren
# print(txt)

##############################Escape Character###################################################

# txt = "We are the so-called \"Vikings\" from the north." #mit dem backslash kann man double quotes in double quotes verwenden
# print(txt)

# # \'	Single Quote	
# txt = 'It\'s alright.'
# print(txt) 
# # \\	Backslash	
# txt = "This will insert one \\ (backslash)."
# print(txt) 
# # \n	New Line	
# txt = "Hello\nWorld!"
# print(txt) 

# # \r	Carriage Return	
# txt = "Hello\rWorld!"
# print(txt) 
# # \t	Tab	
# txt = "Hello\tWorld!"
# print(txt) 
# # \b	Backspace	
# txt = "Hello \bWorld!"
# print(txt) 
# # \f	Form Feed	
# # \ooo	Octal value	
# txt = "\110\145\154\154\157"
# print(txt) 
# # \xhh	Hex value  
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt)

##############################String Methods##################################################

# capitalize()	#Converts the first character to upper case
# casefold()	#Converts string into lower case
# center()	#Returns a centered string
# count()	#Returns the number of times a specified value occurs in a string
# encode()	#Returns an encoded version of the string
# endswith()	#Returns true if the string ends with the specified value
# expandtabs()	#Sets the tab size of the string
# find()	#Searches the string for a specified value and returns the position of where it was found
# format()	#Formats specified values in a string
# format_map()	#Formats specified values in a string
# index()	#Searches the string for a specified value and returns the position of where it was found
# isalnum()	#Returns True if all characters in the string are alphanumeric
# isalpha()	#Returns True if all characters in the string are in the alphabet
# isascii()	#Returns True if all characters in the string are ascii characters
# isdecimal()	#Returns True if all characters in the string are decimals
# isdigit()	#Returns True if all characters in the string are digits
# isidentifier()	#Returns True if the string is an identifier
# islower()	#Returns True if all characters in the string are lower case
# isnumeric()	#Returns True if all characters in the string are numeric
# isprintable()	#Returns True if all characters in the string are printable
# isspace()	#Returns True if all characters in the string are whitespaces
# istitle()	#Returns True if the string follows the rules of a title
# isupper()	#Returns True if all characters in the string are upper case
# join()	#Joins the elements of an iterable to the end of the string
# ljust()	#Returns a left justified version of the string
# lower()	#Converts a string into lower case
# lstrip()	#Returns a left trim version of the string
# maketrans()	#Returns a translation table to be used in translations
# partition()	#Returns a tuple where the string is parted into three parts
# replace()	#Returns a string where a specified value is replaced with a specified value
# rfind()	#Searches the string for a specified value and returns the last position of where it was found
# rindex()	#Searches the string for a specified value and returns the last position of where it was found
# rjust()	#Returns a right justified version of the string
# rpartition()	#Returns a tuple where the string is parted into three parts
# rsplit()	#Splits the string at the specified separator, and returns a list
# rstrip()	#Returns a right trim version of the string
# split()	#Splits the string at the specified separator, and returns a list
# splitlines()	#Splits the string at line breaks and returns a list
# startswith()	#Returns true if the string starts with the specified value
# strip()	#Returns a trimmed version of the string
# swapcase()	#Swaps cases, lower case becomes upper case and vice versa
# title()	#Converts the first character of each word to upper case
# translate()	#Returns a translated string
# upper()	#Converts a string into upper case
# zfill()	#Fills the string with a specified number of 0 values at the beginning

##############################Boolean Values##################################################

# print(10 > 9)
# print(10 == 10)
# print(10 < 9)

# a = 375
# b = 230

# if a < b:
#     print("Yes, is it.")
# else:
#     print("No, Idiot.")

# print(bool("Hello"))
# print(bool(-15.5))

# #return always true
# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])

# #return always false
# bool(False)
# bool(None)
# bool(0)
# bool("")
# print(bool(()))
# bool([])
# bool({})

# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))

# def my_function():
#    return True

# if my_function():
#    print("yes!")
# else:
#    print("no")

# x = 200
# print(isinstance(x, int))

##############################Python Operators##################################################

# print(10 + 5)  #+ ist ein Operator
# # +	Addition	x + y	
# x = 20
# y = 2
# print(y + x)
# # -	Subtraction	x - y	
# print(x - y)
# # *	Multiplication	x * y	
# print(x * y)
# # /	Division	x / y	
# print(x / y)
# # %	Modulus	x % y	
# print(x % y)
# # **	Exponentiation	x ** y	
# print(x ** y)
# # //	Floor division	x // y
# print(x // y)

# =	      x = 5	      x = 5	
# +=	    x += 3	    x = x + 3	
# -=	    x -= 3	    x = x - 3	
# *=	    x *= 3	    x = x * 3	
# /=	    x /= 3	    x = x / 3	
# %=	    x %= 3	    x = x % 3	
# //=	    x //= 3	    x = x // 3	
# **=	    x **= 3	    x = x ** 3	
# &=	    x &= 3	    x = x & 3	
# |=	    x |= 3	    x = x | 3	
# ^=	    x ^= 3	    x = x ^ 3	
# >>=	    x >>= 3	    x = x >> 3	
# <<=	    x <<= 3	    x = x << 3	
# :=	    print(x := 3)	    x = 3  print(x)


# ==	    Equal	      x == y	
# !=	    Not equal	  x != y	
# >	      Greater than	x > y	
# <	      Less than	x < y	
# >=	    Greater than or equal to	x >= y	
# <=	    Less than or equal to	x <= y
# and 	  Returns True if both statements are true	x < 5 and  x < 10	
# or	    Returns True if one of the statements is true	x < 5 or x < 4	
# not	    Reverse the result, returns False if the result is true	  not(x < 5 and x < 10)

##############################Python Lists (array in JS)##################################################

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist)) #list länge

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist)) #typ von einer liste ausgeben

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets list() um eine liste zu machen
# print(thislist)

# Liste         #ist eine Sammlung, die geordnet und veränderbar ist. Erlaubt doppelte Mitglieder.
# Tuple         #ist eine Sammlung, die geordnet und unveränderlich ist. Erlaubt doppelte Mitglieder.
# Set           #ist eine Sammlung, die ungeordnet, unveränderbar* und nicht indiziert ist. Keine doppelten Mitglieder.
# Dictionary    #ist eine Sammlung, die geordnet** und änderbar ist. Keine doppelten Mitglieder.

#del mylist[3]  älöscht den dritten Eintrag, del = delete, braucht den index
#print(mylist)
#mylist.remove("apple")     #löscht den eintrag, da braucht man keinen index
#print(mylist)

#print(mylist[-1])          # gibt immer dass letzte Element aus
##############################Access Items##################################################

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1]) #zeigt dass letzte Itme in der Liste an

# new_lsit = ["Python", "CSS", "JavaScript", "Vue.js", "Cypress", "Java"]
# # print(new_lsit[2:5]) #von bis ausgeben einer List
# print(new_lsit[:4])    #bis zum 4ten ausgeben
# print(new_lsit[2:])    #ab dem 2ten ausgeben

#_________________________________________________________________DJANGO______________________________________________________________________

## Installation

