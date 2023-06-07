complex_wod = input()
complex_wod = complex_wod.lower()

counter = 0
if "water" in complex_wod:
    counter +=complex_wod.count("water")
if "sand" in complex_wod:
    counter +=complex_wod.count("sand")
if "fish" in complex_wod:
    counter +=complex_wod.count("fish")
if "sun" in complex_wod:
    counter +=complex_wod.count("sun")


print(counter)