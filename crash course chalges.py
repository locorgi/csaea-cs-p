import math
score = 69
 
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("F")
    
fahrenheit = 212
C = (fahrenheit -32 ) * 5/9

print(C )

start = 10

while start > 0:
    start -= 1 
    print(start)
if start ==0:
    print("liftoff")


bill = 50
tip = bill %20
total = tip + bill
print(tip)
print( total) 

password = "csaea2026"
attempt = "csaea2026"
if password == attempt :
    print("Acces granted")
else:
    print("Access deined")

students = 23 
slices_per_student = 2 
slices_per_pizza = 8 

total_slices = students * slices_per_student
pizzas_needed = math.ceil(total_slices / slices_per_pizza)

print(pizzas_needed)


first = "Ada"
last = "Lovelace"
school = "CSAEA"

# Combine the variables using string concatenation
print("Hello, my name is " + first + " " + last + " from " + school)