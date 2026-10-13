import math
import random
sq_root = math.sqrt(25)
print("Square root:", sq_root)

round_up = math.ceil(4.5)
print("round_up ",round_up)


round_down = math.floor(4.8)
print(f"Round down: {round_down}")

e=math.pow(4 ,5)
print("power of", e)

PI=math.pi
print(PI)
d=14
r=d/2

print(PI *r )


seed= 533.47
seed2= seed +92
seed3 = seed2/ seed
result = math.ceil(seed3)
print("your random number is" , result)
randint=math.ceil(result)
print(f"Simple random num gen: {randint % 10}")
seed= 533.47
seed2= seed +92
seed3 = seed2/ seed
result = math.ceil(seed3)
print("your random number is" , result)
randint=math.ceil(result)
print(f"Simple random num gen: {randint % 10}")




ramdom_integer = random.randint(1, 100)
print(ramdom_integer)

ramdonfloat = random.random()
print(ramdonfloat)
my_list =["zach","yiynag","jacup"]
randomslection = random.choice(my_list)
print(randomslection)

random.shuffle(my_list)
print(my_list)




die_roll = random.randint(1, 6)
print(f"dice number",die_roll)

num= random.randint(1, 75)
square_root=math.sqrt(num)
rounded=math.ceil(square_root)
print(f"random number is, {num} square root is,{square_root} rounded is, {rounded}")

base= random.randint(1, 6)
exponent= random.randint(1, 6)
