def Even_filter(number):
    if number % 2 == 0:
        return True
    else:
        return False


numbers_string = input().split()
numbers_digits = []

for number in numbers_string:
    numbers_digits.append(int(number))

filtered_digits = list(filter(Even_filter,numbers_digits))

print(filtered_digits)