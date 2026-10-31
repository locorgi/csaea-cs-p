add = 7 + 9
print("sum:", add)

subtract = 43 -45
print("Product", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 10 / 3
print("Float division:", float_divide)

integer_devided = 7// 2
print("integer divison:", integer_devided)

mod = 7 % 2
print("mod:", mod)

exponent = 7 ** 2

print("expontent:" , exponent)

# pemdas

result = (2 + 3) * 4
print("resut:",result)

result2 = 2 **3*4
print("result2:", result2)

result3 = 5+2**3 * (4-1)
print("result3:", result3)


witha =  8*2
leangh = 5*2
print(witha + leangh)


r = 7 *7
p = 3.14
print(r * p)

b = 12.99
n= 3.5
print("total $",b *3 + n * 4)
print(f"cost of books ${b*3} \n cost of notebooks $ {n* 4} \n total cost is ${b*3 + n*4}")
l = 56 % 2
if l ==1:
    print("odd")
else:
    print("even")
# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.  
# Create separate variables for width, height, and result. Print result. 
w=8
h=5
print(w*2 + h*2)
# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. 
# (Use 3.14 for π.)  
# Separate variables for pi, radius, and result. 
pi=3.14
radius=7
result = pi * (radius ** 2)
print(result)
# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.  
# Use only one print statement. Print the result in this format: 
#     Book: <$ cost of book>
#     Notebook: <$ cost of notebook>
#     Total: <$>
b=12.99
n=3.5
print(b*3  +  n*4)
# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd. 
num=56
if num % 2 == 0: 
    print("even")
else:
    print("odd")