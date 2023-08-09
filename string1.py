input_string = input("Enter a string: ")
vowels = "AEIOUaeiou"
vowel_count = 0
vowel_list = []

for char in input_string:
    if char in vowels:
        vowel_count += 1
        vowel_list.append(char)
        

print("Number of vowels:", vowel_count)
print("Vowels extracted:", "".join(vowel_list))
