print("Welcome to the Pizza Deliveries!")

size = input("What size pizza do you want? S,M Or L ?: ")

add_pepperoni = input("Do you want Pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese?, Y or N: ")

bill = 0
if size.lower() == "s":
    bill += 15
elif size.lower() == 'm':
    bill += 20
elif size.lower() =="l":
    bill += 25
else:
    print("please provide valid input")

if add_pepperoni.lower() == 'y':
    if size == 's':
        bill+=2
    else:
        bill +=3

if extra_cheese.lower() == 'y':
    bill+=1

print(f"your final bill is $ {bill}")
