
height = int(input("What's is your height in cm?"))
bill = 0

if height >=120:
    print("you can ride the rollercoaster!")

    age = int(input("What's your age?"))

    if age<12:
        bill = 5
        print("child tickets are $ 5")

    elif age<=18:
        bill = 7
        print("Youth tickets are $7")

    elif age >=45 and age<=55:
        print("Everything is going to ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are  $12")

