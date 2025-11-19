firstNumber = list(map(int,input().split(" ")))
secondNumber = list(map(int,input().split(" ")))
result = list(map(int,input().split(" ")))
firstFactor = firstNumber.pop(0)
secondFactor = secondNumber.pop(0)
resultFactor = result.pop(0)

min_base = max(max(firstNumber), max(secondNumber), max(result)) + 1
max_base = 2073741825 # i chose this.

for base in range(min_base, max_base):
    firstValue = 0
    secondValue = 0
    resultValue = 0

    for i in range(firstFactor):
        firstValue += firstNumber[i] * (base ** (firstFactor - i - 1))

    for i in range(secondFactor):
        secondValue += secondNumber[i] * (base ** (secondFactor - i - 1))

    for i in range(resultFactor):
        resultValue += result[i] * (base ** (resultFactor - i - 1))

    if resultValue == firstValue * secondValue:
        print(base)
        exit()

print("impossible")