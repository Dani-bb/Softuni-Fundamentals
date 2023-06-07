def Ranged_Char():
    between = []
    string_of_char = ""
    first = ord(char_a)
    second = ord(char_b)

    for char in range(first +1,second):
        between.append(chr(char))
    for char1 in between:
        string_of_char += char1 + " "


    print(string_of_char)


char_a = input()
char_b = input()


Ranged_Char()

