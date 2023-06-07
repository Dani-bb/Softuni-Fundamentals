how_much_to_add = int(input())
how_many_words = int( input())
word = ""
for char in range(how_many_words):
    characters =  input()
    digitalised = ord(characters) + how_much_to_add
    word += chr(digitalised)


print(word)