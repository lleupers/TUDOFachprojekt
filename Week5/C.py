firstNumber = list(map(int,input().split(" ")))
secondNumber = list(map(int,input().split(" ")))
result = list(map(int,input().split(" ")))
firstFactor = firstNumber.pop(0)
secondFactor = secondNumber.pop(0)
resultFactor = result.pop(0)

min_base = max(max(firstNumber), max(secondNumber), max(result)) + 1
max_base = 1073751825 # i chose this.

for base in range(min_base, max_base):
    firstValue = 0
    secondValue = 0
    resultValue = 0

    for d in firstNumber:
        firstValue = firstValue * base + d

    for d in secondNumber:
        secondValue = secondValue * base + d

    for d in result:
        resultValue = resultValue * base + d

    if resultValue == firstValue * secondValue:
        print(base)
        exit()

print("impossible")