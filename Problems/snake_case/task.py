string_input = input()
for char in string_input:
    if char.isupper():
        string_input = string_input.replace(char, "_" + char.lower())
print(string_input)
