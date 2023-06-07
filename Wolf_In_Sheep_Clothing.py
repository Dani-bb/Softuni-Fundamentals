order_of_animals = input().split(",")

reversed_order_of_animals =[]

for animal in reversed(order_of_animals):
    reversed_order_of_animals.append(animal)

counter = 0
wolf_counter = 0



for animal in reversed_order_of_animals:
    counter += 1
    if counter == 1:
     if animal == " wolf" or animal == "wolf" or animal =="wolf ":
        print(f"Please go away and stop eating my sheep")
        break

    sheep_number = len(order_of_animals) - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
    break





