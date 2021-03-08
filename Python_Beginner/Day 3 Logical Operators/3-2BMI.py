# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bmi = round(weight/height **2)

if bmi <18.5:
  print(f'Your bmi is {bmi} and you are underweight')
elif bmi >=18.5 and bmi<25:
  print(f'Your bmi is {bmi} and you have normal weight')
elif bmi>25 and bmi<30:
  print(f'Your bmi is {bmi} and you  are slightly overweight')
elif bmi>=30 and bmi<=35:
  print(f'Your bmi is {bmi} and You are Obess')
else:
  print('You are clinicly Obess')