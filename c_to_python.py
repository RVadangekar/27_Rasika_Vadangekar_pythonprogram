def print_pattern(n):
    for rows in range(1, n + 1):
        for columns in range(n, rows, -1):
            print(" ", end="")
        
        print("*", end="")
        
        for columns in range(1, (rows - 1) * 2 + 1):
            print(" ", end="")
        
        if rows == 1:
            print()
        else:
            print("*")
    
    for rows in range(n - 1, 0, -1):
        for columns in range(n, rows, -1):
            print(" ", end="")
        
        print("*", end="")
        
        for columns in range(1, (rows - 1) * 2 + 1):
            print(" ", end="")
        
        if rows == 1:
            print()
        else:
            print("*")

def main():
    n = 5
    print_pattern(n)

if __name__ == "__main__":
    main()
