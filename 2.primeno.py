input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def extract_prime_numbers(number_list):
    prime_numbers = [number for number in number_list if is_prime(number)]
    return prime_numbers
prime_numbers = extract_prime_numbers(input_list)

if prime_numbers:
            print("Prime numbers in the list:", prime_numbers)
else:
            print("No prime numbers found in the list.")
