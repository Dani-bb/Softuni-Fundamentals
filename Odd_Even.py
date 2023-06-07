def Odd_Summ_Even_Summ_Calculator():
    summed_ODD = 0
    summed_EVEN = 0

    for num in list1:
        num = int(num)
        if num %2 == 0:
            summed_EVEN += int(num)
        else:
            summed_ODD += int(num)
    print(f"Odd sum = {summed_ODD}, Even sum = {summed_EVEN}")


ribi = input()
list1 =[]

for num in ribi:
    list1.append(num)



Odd_Summ_Even_Summ_Calculator()

