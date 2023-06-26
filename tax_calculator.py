family_cars = input().split('>>')

total_tax = 0

for family_car in family_cars:
    car_info = family_car.split()

    if car_info[0] == "family":
        tax = 50
        if int(car_info[1]) > 0:
            tax -= 5 * int(car_info[1])
        if int(car_info[2]) >= 3000:
            additional_distance = int(car_info[2])
            additional_tax = (additional_distance // 3000) * 12
            tax += additional_tax
        print(f"A {car_info[0]} car will pay {tax:.2f} euros in taxes.")
        total_tax += tax
    elif car_info[0] == "heavyDuty":
        tax = 80
        if int(car_info[1]) > 0:
            tax -= 8 * int(car_info[1])
        if int(car_info[2]) >= 9000:
            additional_distance = int(car_info[2])
            additional_tax = (additional_distance // 9000) * 14
            tax += additional_tax
        print(f"A {car_info[0]} car will pay {tax:.2f} euros in taxes.")
        total_tax += tax
    elif car_info[0] == "sports":
        tax = 100
        if int(car_info[1]) > 0:
            tax -= 9 * int(car_info[1])
        if int(car_info[2]) >= 2000:
            additional_distance = int(car_info[2])
            additional_tax = (additional_distance // 2000) * 18
            tax += additional_tax
        print(f"A {car_info[0]} car will pay {tax:.2f} euros in taxes.")
        total_tax += tax
    else:
        print("Invalid car type.")
        continue

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
