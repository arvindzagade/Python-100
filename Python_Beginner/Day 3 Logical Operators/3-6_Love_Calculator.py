# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# first will combine the string and then will check for letters of TRUE LOVE in them

combined_string = name1 + name2
# we need to get string in lower letters
lower_case_string = combined_string.lower()
# Now checking for the words

t= lower_case_string.count("t")
r= lower_case_string.count("r")
u= lower_case_string.count("u")
e= lower_case_string.count("e")

true = t + r + u + e

l= lower_case_string.count("l")
o= lower_case_string.count("o")
v= lower_case_string.count("v")
e= lower_case_string.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score >90):
  print(f"your love score is {love_score},You go together like coke and mentos.")

elif love_score >=40 and love_score<=50:
  print(f'your score is {love_score},you are alright together')
else:
  print(f'you love score is {love_score}')