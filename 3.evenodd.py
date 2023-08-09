input_numbers = input("Enter a tuple of numbers separated by spaces: ")
numbers_tuple = tuple(map(int, input_numbers.split()))

even_numbers = []
odd_numbers = []

for num in numbers_tuple:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
