
def Adding():
    added_numbers = first_number + second_number
    return added_numbers

def Subtract():
    subtracted = Adding() - third_number
    return subtracted

def Add_And_Subtract():
    Adding()
    Subtract()
    print(Subtract())






first_number = int(input())
second_number = int(input())
third_number = int(input())

Add_And_Subtract()