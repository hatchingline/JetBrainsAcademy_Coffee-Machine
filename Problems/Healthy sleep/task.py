sleep_a = int(input())
sleep_b = int(input())
sleep_h = int(input())
if sleep_h < sleep_a:
    print("Deficiency")
elif sleep_h > sleep_b:
    print("Excess")
else:
    print("Normal")
