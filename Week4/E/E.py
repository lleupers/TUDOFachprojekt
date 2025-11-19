count = int(input())

capacity = list(map(int,input().split()))
costs = list(map(int,input().split()))

capacity.sort()
costs.sort(reverse=True)

total_cost = 0
for i in range(0,count):
    total_cost += capacity[i] * costs[i]

print(total_cost * 1000)