def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])

    for num in range(1, number + 1):
        print(f"{num:>{width}} {num:>{width}o} {num:>{width}X} {num:>{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
