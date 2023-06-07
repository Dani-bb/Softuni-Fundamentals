number_of_lines = int(input())

left_one_counter = 0
right_one_counter = 0
combo = 0
for char in range(number_of_lines):
    character = input()
    if character == "(":
        left_one_counter += 1
    if character == ")":
        right_one_counter +=1
    if left_one_counter == right_one_counter:
        combo += 1
        left_one_counter = 0
        right_one_counter = 0
if combo >= 1:
    print(f"BALANCED")
else:
    print("UNBALANCED")



