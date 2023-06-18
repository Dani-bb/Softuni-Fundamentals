room = input(). split("|")

health = 100
bitcoin = 0
room_counter = 0
while True:
    for thing in room:
        room_counter += 1
        if thing[1] == "potion":
            if health + int(thing[2]) > 100:
                health = 100
                print(f"You healed for {100 - health} hp.")
                print(f"Current health: {health} hp.")
            else:
                health += int(thing[2])
                print(f"You healed for {thing[2]} hp.")
                print(f"Current health: {health} hp.")
        if thing[1] == "chest":
            bitcoin += int(thing[2])
            print(f"You found {thing[2]} bitcoins.")
        else:
            health -= int(thing[2])
            if health <= 0:
                print(f"You died! Killed by {thing[1]}.")
                print(f"Best room: {room_counter}")
                break
    if health > 0:
        print("You've made it!")
        print(f"Bitcoins: {bitcoin}")
        print(f"Health: {health}")
    else:
        break
