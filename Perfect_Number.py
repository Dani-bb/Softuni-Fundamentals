def Perfect(some_number:int) -> str:
    diviser_sum = 0
    for divisor in range(1,some_number):
        if some_number % divisor == 0:
            diviser_sum +=divisor
    if some_number == diviser_sum:
        return "We have a perfect number!"

    return "It's not so perfect."









number = int(input())
print(Perfect(number))