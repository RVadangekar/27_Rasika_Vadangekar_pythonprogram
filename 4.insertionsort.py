input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(int, input_numbers.split()))

for i in range(1, len(numbers_list)):
    key = numbers_list[i]
    j = i - 1
    while j >= 0 and key < numbers_list[j]:
        numbers_list[j + 1] = numbers_list[j]
        j -= 1
    numbers_list[j + 1] = key

print("Sorted list:", numbers_list)
