# age = int(input("enter your age: "))
# next_year = age + 1
# print(f" your age:{age}")
# print(f'next year you will be: {next_year}')

# name = "Mirzabek"
# surname = "Aliev"
# age = 18
# nex_year = int(age) + 1
# print("My name is " + name + " and  I am "+ str(age) + "  years old.")
# print(f" my name is {name} {surname} and I am {age} years old")
# print (f'Next year I will be {next_year}')
# print(f"next year i will be {age + 1} years old")

# price = 15999.5
# print(f"price: {price:.2f} sum")
# pi = 3.141599265359
# print(f" Pi to 2 decimals: {pi:.2f}")
# print(f"Pi to 5 decimals: {pi:.5f}")
# print(int(pi) )
# print(f"{pi}")

# item = input(" Enter your item name bro: ")
# quantity = int(input(" How much do you have?: "))
# price_per_item= float(input("Enter your price bro: "))

# total = quantity * price_per_item

# print(f"\n{'='*40}")
# print(f"        RECEIPT")
# print(f"{'='*40}")
# print(f'Item: {item}')
# print(f"Quantity:{quantity}")
# print(f"Price per item: {price_per_item:.2f} sum")
# print(f"{'='*40}")
# print()
# print('Please, tell us the temperature!')
name=input('What is your name?\n')
income=int(input('How much is your income?\n'))
rent=int(input('How much is your rent?\n'))
internet=int(input('How much is your internet and phone bill?\n'))
food=int(input('How much do you pay for groceries?\n'))
tr=int(input('How much do you pay for transportation?\n'))
ent=int(input('How much do you pay for entertainment?\n'))
save=int(input('How much do you save now?\n'))
goal=int(input('How much do you wanna save?\n'))
month=int(input('How many months do wou wanna spend?\n'))
expense= rent + internet + food + tr + ent 
saving= income - expense
percent= saving/income*100
target= saving*month
amount=save + target
need=amount/month
negative = saving - target  
# print(f'Shortfall: {negative}')
# positive = saving - target >0
# print(f'surplus: {positive}')
print(f"\n\n\nBudget analyzer of {name}")
print(f'Your monthly income: {income}') 
print(f'Your monthly expenses: {expense}') 
print(f'Your monthly savings: {saving}')
print(f'Savings rate percentage: {percent}')
print(f'projected Savings after target months: {target}')
print(f'Total projected amount after target months: {amount}')
print(f'Monthly savings needed to reach goal : {need}')
print(f'Total projected amount after target months: {amount}')
print(f"Additional monthly savings needed: {negative} ")

