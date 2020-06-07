income = int(input())
percent_1 = 0
percent_2 = 15
percent_3 = 25
percent_4 = 28
if 0 <= income <= 15527:
    calculated_tax_1 = round(income * percent_1 / 100)
    print(f"The tax for {income} is {percent_1}%. That is {calculated_tax_1} dollars!")
elif 15528 <= income <= 42707:
    calculated_tax_2 = round(income * percent_2 / 100)
    print(f"The tax for {income} is {percent_2}%. That is {calculated_tax_2} dollars!")
elif 42708 <= income <= 132406:
    calculated_tax_3 = round(income * percent_3 / 100)
    print(f"The tax for {income} is {percent_3}%. That is {calculated_tax_3} dollars!")
else:
    calculated_tax_4 = round(income * percent_4 / 100)
    print(f"The tax for {income} is {percent_4}%. That is {calculated_tax_4} dollars!")
