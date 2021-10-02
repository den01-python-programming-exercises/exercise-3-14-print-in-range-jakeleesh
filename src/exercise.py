def main():
    #write your code below this line
    numbers = []
    numbers.append(3)
    numbers.append(2)
    numbers.append(6)
    numbers.append(-1)
    numbers.append(5)
    numbers.append(1)

    print("The numbers in the range [0, 5]")
    print_numbers_in_range(numbers, 0, 5)

    print("The numbers in the range [3, 10]")
    print_numbers_in_range(numbers, 3, 10)

def print_numbers_in_range(numbers, lower_limit, upper_limit):
    for num in numbers:
        if (num >= lower_limit and num <= upper_limit):
            print(num)

if __name__ == '__main__':
    main()
