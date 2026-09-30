import math
score = 90
 
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

while start > 1:
    start -= 1 
    print(start)
if start ==1:
    print("liftoff")


bill = 50
tip = bill %20
total = tip + bill
print(tip)
print(total)

password = "csaea2026"
attempt = "csaea2026"
if password == attempt :
    print("Acces granted")
else:
    print("Access deined")

plate = 4827
if plate % 2==0:
    print("park on east side")
else:
    print("park on west side")
first = "Ada"
last = "Lovelace"
school = "CSAEA"
print(f"hello my name is {first} {last} from {school}")

cart = [12, 5, 30, 8]
total_price=0
for price in cart:
    total_price += price
item = len(cart)
print(f"total_price is ${total_price}")
print(f"with {item} items in cart")

