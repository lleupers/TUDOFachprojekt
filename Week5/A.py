n, k = list(map(int,input().split(" ")))

letters = []
mothers = []

for x in range(n):
    letter, mother = list(input().split(" "))
    letters.append(letter)
    mothers.append(int(mother))

names = []
for i in range(n):
    if mothers[i] == 0:
        name = letters[i]
    else:
        name = letters[i]+names[mothers[i]-1]
    names.append(name)

for x in range(k):
    count = 0
    symbol = input()
    for name in names:
        if name.startswith(symbol):
            count += 1
    print(count)