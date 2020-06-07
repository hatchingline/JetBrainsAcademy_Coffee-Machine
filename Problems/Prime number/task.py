num_input = int(input())
if num_input == 1:
    print("This number is not prime")
else:
    factor_count = 0
    for factor in range(1, num_input + 1):
        if num_input % factor == 0:
            factor_count += 1
    if factor_count > 2:
        print("This number is not prime")
    else:
        print("This number is prime")
