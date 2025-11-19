n,k = input().split()
n = int(n)
k = int(k)

days = []
for x in range(n):
    days.append(int(input()))

for i in range(k - 1, n):
    important_days = days[i - k + 1:i + 1]
    print(max(important_days))