# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# #Simple Approach

# total_height = sum(student_height)
# number_of_student = len(student_height)
# average_height =  round(total_height/number_of_student)
# print(average_height)

total_height = 0

for height in student_heights:
  total_height += height
print(total_height)

num_of_students = 0

for student in student_heights:
  num_of_students +=1

print(num_of_students)


average_height = round(total_height/num_of_students)
print(average_height)
