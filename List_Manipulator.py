list_of_work = input()
modified_lis_of_work = list_of_work.replace(' ','')

#finding the int
first_line = []
max_number_odd = 0
max_number_even = 0
min_number_even = 0
min_number_odd = 0

digit = 1
digit_for_count = 0

for word in modified_lis_of_work:
    word = int(word)
    first_line.append(word)

def exchange():
    global first_line
    removed_items = first_line[:digit ]
    new_list = first_line[digit:] + removed_items
    first_line = new_list
    pass


def max_odd(number):
    return number % 2 !=0


def max_even(number):
    return number % 2 == 0


def min_odd(number):
    return number % 2 != 0


def min_even(number):
    return number % 2 == 0

def first_count_even():
    global first_line
    unfiltered = []
    first_count_even_numbers = []
    for numbers in first_line:
        if numbers % 2 ==0:
            unfiltered.append(numbers)
        else:
            return []
    for index, number in enumerate(unfiltered):
        if len(unfiltered) < digit_for_count:
            return "Invalid count"

        if index < digit_for_count:
            first_count_even_numbers.append(number)

    return first_count_even_numbers

def first_count_odd():
    global first_line
    first_count_odd_numbers = []
    unfiltered_1 = []
    for numbers in first_line:
        if numbers % 2 != 0:
            unfiltered_1.append(numbers)
        else:
            return []
    for index, number in enumerate(unfiltered_1):
        if len(unfiltered_1) < digit_for_count:
            return "Invalid count"

        if index < digit_for_count:
            first_count_odd_numbers.append(number)

    return first_count_odd_numbers


def last_count_even():
    global first_line
    unfiltered = []
    last_count_even_numbers = []
    for numbers in first_line:
        if numbers % 2 == 0:
            unfiltered.append(numbers)
        else:
            return []
    for index, number in enumerate(reversed(unfiltered)):
        if len(unfiltered) < digit_for_count:
            return "Invalid count"

        if index < digit_for_count:
            last_count_even_numbers.append(number)

    return last_count_even_numbers

def last_count_odd():
    global first_line
    unfiltered = []
    last_count_odd_numbers = []
    for numbers in first_line:
        if numbers % 2 != 0:
            unfiltered.append(numbers)
        else:
            return []
    for index, number in enumerate(reversed(unfiltered)):
        if len(unfiltered) < digit_for_count:
            return "Invalid count"

        if index < digit_for_count:
            last_count_odd_numbers.append(number)

    return last_count_odd_numbers



while True:
    command = input()
    if command == "end":
        print(first_line)
        break
    if "exchange" in command:
        for thing in command:
            if any(char.isdigit() for char in thing):

                digit += int(thing)
                if digit < 0:
                    print("Invalid index")
                if digit > len(first_line):
                    print("Invalid index")
                exchange()
                digit = 1

    if command == "max odd":
        filtered_numbers = filter(max_odd, first_line)
        odd_numbers = list(filtered_numbers)
        if odd_numbers:
            max_odd_index = first_line.index(max(odd_numbers))
            max_number_odd += max_odd_index
            print(max_number_odd)
        else:
            print("No matches")

    if command == "max even":
        filtered_numbers = filter(max_even, first_line)
        even_numbers = list(filtered_numbers)
        if even_numbers:
            max_even_index = first_line.index(max(even_numbers))
            max_number_even += max_even_index
            print(max_number_even)
        else:
            print("No matches")
    if command == "min odd":
        filtered_numbers = filter(min_odd,first_line)
        odd_numbers = list(filtered_numbers)
        if odd_numbers:
            min_odd_index = first_line.index((min(odd_numbers)))
            min_number_odd += min_odd_index
            print(min_number_odd)
        else:
            print("No matches")
    if command == "min even":
        filtered_numbers = filter(min_even, first_line)
        even_numbers = list(filtered_numbers)
        if even_numbers:
            min_even_index = first_line.index(min(even_numbers))
            min_number_even += min_even_index
            print(min_number_even)
        else:
            print("No matches")
    if "first" in command:
        if "even" in command:
            for thing in command:
                if any(char.isdigit() for char in thing):
                    digit_for_count += int(thing)
            print(first_count_even())
            digit_for_count = 0

        if "odd" in command:
            for thing in command:
                if any(char.isdigit() for char in thing):
                    digit_for_count += int(thing)
            print(first_count_odd())
            digit_for_count = 0
    if "last" in command:
        if "even" in command:
            for thing in command:
                if any(char.isdigit() for char in thing):
                    digit_for_count += int(thing)
            print(last_count_even())
            digit_for_count = 0


        if "odd" in command:
            for thing in command:
                if any(char.isdigit() for char in thing):
                    digit_for_count += int(thing)
            print(last_count_odd())
            digit_for_count = 0







