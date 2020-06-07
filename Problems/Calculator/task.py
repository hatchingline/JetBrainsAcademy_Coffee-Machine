# put your python code here
first_num = float(input())
second_num = float(input())
operator = input()
if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "/":
    if second_num == 0:
        print("Division by 0!")
    else:
        print(first_num / second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "mod":
    if second_num == 0:
        print("Division by 0!")
    else:
        print(first_num % second_num)
elif operator == "pow":
    print(first_num ** second_num)
elif operator == "div":
    if second_num == 0:
        print("Division by 0!")
    else:
        print(first_num // second_num)
