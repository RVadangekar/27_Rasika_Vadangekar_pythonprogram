num = int(input("Enter a number: "))

if num > 1:
   
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("{0} is not a prime number".format(num))
            break
    else:
        print("{0} is a prime number".format(num))
else:
    print("{0} is not a prime number".format(num))
