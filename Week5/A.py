n, k = list(map(int,input().split(" ")))
print(n, k)
sequences = []

for x in range(n):
    i = input()
    line = list(input().split(" "))
    letter = line[0]
    if x == 0:
        sequences.append(letter)
    else:
        sequences.append(sequences[x-1] + letter)

print(sequences)