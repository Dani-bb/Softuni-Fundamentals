from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron = float(input())
flour_prices = 0
#one student = 1 apron, 10 eggs,1 flour

apron_price = apron * ceil(students + (students * 0.20))
egg_prices = students * 10 * egg_price
flour_prices += students * flour_price
if students % 5 == 0:
    flour_prices -= flour_price * (students // 5)

final_sum = apron_price + egg_prices+ flour_prices

if final_sum <= budget:
    print(f"Items purchased for {final_sum:.2f}$.")
if  final_sum > budget:
    print(f"{abs(budget-final_sum):.2f}$ more needed.")

