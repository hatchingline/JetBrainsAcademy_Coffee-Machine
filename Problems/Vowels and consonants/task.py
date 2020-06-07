str_input = input().lower()
for char in str_input:
    if char in "aeiou":
        print("vowel")
    elif char in "bcdfghijklmnpqrstvwxyz":
        print("consonant")
    else:
        break
