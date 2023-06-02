list_of_numers = input().split()

opposite = []

for elements in list_of_numers:
   current_number = -int(elements)
   opposite.append(current_number)

print(opposite)