def checker():
    data = input()
    if data =="int":
        number = int(input())
        number *= 2
        print(number)
    if data == "real":
        number = int(input())
        number *= 1.5
        print(f"{number:.2f}")
    if data == "string":
        number = input()
        number = "$"+ number +"$"
        print(number)

checker()