firstNumber = list(map(int,input().split(" ")))
secondNumber = list(map(int,input().split(" ")))
result = list(map(int,input().split(" ")))

min_base = max(max(firstNumber[1:]), max(secondNumber[1:]), max(result[1:])) + 1
max_base = 256 # i chose this.
print(min_base, max_base)

for base in range(min_base, max_base):
    