numbers = list(map(int, input().split()))
remover = [numbers.remove(min(numbers)) for _ in range (int(input()))]
filtered = ''
index = 0
for num in numbers:
    filtered+= str(num)

    index +=1
    if index != remover:
        filtered += ", "



print(filtered)