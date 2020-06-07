# put your python code here
year = int(input())
if not year % 400:
    print("Leap")
else:
    if not year % 4 and year % 100:
        print("Leap")
    else:
        print("Ordinary")
