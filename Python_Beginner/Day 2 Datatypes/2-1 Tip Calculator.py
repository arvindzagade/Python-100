#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print('Welcome to tip Calculator')
bill = float(input('What is your total Bill?'))

tip = int(input('What percentage tip would you like to give? 10,12 or 15?'))

people = int(input('How many people to split the bill?'))


tip_per = tip/100
total_tip_amount = bill * tip_per

total_bill = total_tip_amount + bill

bill_per_person = total_bill/people

final_amount = round(bill_per_person,3)


print(f"Each Person should pay $ {final_amount}")



