
def Palindrome_checker(numbers):
    for numb in numbers_string:
        if numb == numb[::-1]:
            print("True")
        else:
            print("False")


numbers_string = input().split(", ")



Palindrome_checker(numbers_string)
