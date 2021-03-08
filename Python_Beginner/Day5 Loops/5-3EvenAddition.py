#Write your code below this row 👇
total = 0
for num in range(1,101):
  if num%2 ==0:
    total = total + num

print(total)

## 2 Approach

total = 0

for num in range(2,101,2):
  total += num
print(total)