input_numbers = input("Enter a list of integers separated by spaces: ")
numbers_list = list(map(int, input_numbers.split()))

unique_numbers = []

for num in numbers_list:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List with unique numbers:", unique_numbers)
