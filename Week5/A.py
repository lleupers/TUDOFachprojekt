n, k = list(map(int,input().split(" ")))

sequences = []

for x in range(n):
    letter,_ = list(input().split(" "))
    if x == 0:
        sequences.append(letter)
    else:
        sequences.insert(0,letter + sequences[0])

print(sequences)