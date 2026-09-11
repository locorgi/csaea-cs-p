import random
import math
print("hello world")
# hiiiiiiiii
a = 4  # integer
b = 5.5  # float
c = "CSAEA" # string
d = False # boolean
print(c)
print(a, b, c, d)
# operators + - ? * % ** //
# compound operators += -= /=
e = 11 % 10


#               comparsions  boleans that are alawsy true or false
# < > <= >= == !=
print(4<5)
print(7==4)
print(1!=2)
isEqual = "Yes"=="Yes"
print(isEqual)
# logical operator
# in order of precedence not and or
f= False
t= True
print(not f)
print (f and t)
print(f or t)
print(f or t and not f)
g = int(5.6536539)
s1 ="Goodnight"
s2 = " and"
s3 = " Goodbye"
end= s1+ s2+ s3
print(end)
end += ", Cowboy."

print(end)
# math libary
print(math.sqrt(14))
print(math.ceil(3.65))
print(math.floor(8.94))
print(math.pow(2,4))
# conditionals
# if elif else
t=True
f=False
if f:
    print("Reached the first condition")
elif t:
    print("Reached second condition")
else:
    print("Reached else")


if 1 > 1 and 1 == 1:
    print("Reached the first condition")
elif 6 == 7 or 3!=3:
    print("Reached second condition")
else:
    print("Reached else")
    # lists
 # a list can hold any type  grow shrink
nums = [34, 52, 64, 32]

print(nums)
# list methods
words = []

words.append("Words 1")
words.append("Words 2")
words.append("Words 3")
print(words)
words.remove("Words 1")
words.insert(0, "Words 4")
print(words)

