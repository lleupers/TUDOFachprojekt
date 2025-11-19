import heapq

count = input()
rocks = []
for x in range(int(count)):
    rocks.append(-1 * int(input()))

#wegen minheap alles mit -1
heapq.heapify(rocks)

while(len(rocks) > 1):
    first = heapq.heappop(rocks)
    second = heapq.heappop(rocks)
    if first < second:
        heapq.heappush(rocks, first - second)
    elif second < first:
        heapq.heappush(rocks, second - first)

if len(rocks) == 0:
    print('NONE')
else:
    print(-1* rocks[0])