
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
print(f'Savings rate percentage: {percent} %')
print(f'projected Savings after target months: {target}')
print(f'Total projected amount after target months: {amount}')
print(f'Monthly savings needed to reach goal : {need}')
print(f'Total projected amount after target months: {amount}')
print(f"Additional monthly savings needed: {negative} ")

