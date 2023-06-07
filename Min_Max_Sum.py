def Min_Max_Sum(number):
    minimum = 0
    maximum = 0
    sum_of_them = 0
    minimum += min(number)
    maximum += max(number)
    sum_of_them += sum(number)
    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum number is: {sum_of_them}")





numbers_string = input().split()
numbers_digits = []

for number in numbers_string:
    numbers_digits.append(int(number))

Min_Max_Sum(numbers_digits)