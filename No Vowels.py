vowel = input()

sorted = [letter for letter in vowel if letter.lower() not in['a','o','e','u','i']]

print(''.join(sorted))
