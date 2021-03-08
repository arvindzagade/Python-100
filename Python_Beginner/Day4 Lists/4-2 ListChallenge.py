# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
num_item = len(names)

random_choice = random.randint(0,num_item -1)
print(random_choice)

person_to_pay = names[random_choice]

#person_to_pay = random.choice(names)
print(person_to_pay + ' will pay for dinner.')


   