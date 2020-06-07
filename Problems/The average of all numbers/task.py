# put your python code here
a = int(input())
b = int(input())
sum_3 = 0
count = 0
for element in range(a, b + 1):
    if element % 3 == 0:
        sum_3 += element
        count += 1
print(sum_3 / count)
