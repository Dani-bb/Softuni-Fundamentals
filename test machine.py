inventory = input().split(", ")

while True:
    command = input().split(" - ")
    if command[0] == "Craft!":
        break

    if command[0] == "Collect":
        item = command[1]
        if item not in inventory:
            inventory.append(item)

    if command[0] == "Drop":
        item = command[1]
        if item in inventory:
            inventory.remove(item)

    if command[0] == "Combine Items":
        items = command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index + 1, new_item)

    if command[0] == "Renew":
        item = command[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

inventory_str = ", ".join(inventory)
print(inventory_str)
