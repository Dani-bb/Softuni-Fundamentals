inventory = input().split(',')


while True:
    command = input().split(" - ")
    if command[0] == "Craft!":
        break

    if command[0] == "Collect":
        if command[1] in inventory:
            continue
        else:
            inventory.append(command[1])
    if command[0] == "Drop":
        if command[1] in inventory:
            inventory.remove(command[1])
        else:
            continue
    if command[0] == "Combine Items":
        items = command[1].split(':')
        if items[0] in inventory:
            old_item = inventory.index(items[0])
            inventory.insert(old_item + 1,items[1])
        else:
            continue
    if command[0] == "Renew":
        if command[1] in list:
            inventory.remove(command[1])
            inventory.append(command[1])
        else:
            continue

inventory_str = ",".join(inventory)
print(inventory_str)