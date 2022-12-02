import sys
input = sys.stdin.readline
import heapq

def garbage(heap):
    while heap and visited[heap[0][1]] == False:
        heapq.heappop(heap)

t = int(input())
for _ in range(t):
    n = int(input())
    max_heap = []
    min_heap = []
    visited = [False] * (n+1)
    for i in range(n):
        order, val = map(str, input().split())
        val = int(val)
        if order == 'I':
            heapq.heappush(min_heap, (val, i))
            heapq.heappush(max_heap, (val*-1, i))
            visited[i] = True
        else:
            if val == -1:
                while min_heap and visited[min_heap[0][1]] == False:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)        
            else:
                while max_heap and visited[max_heap[0][1]] == False:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                
    garbage(min_heap)
    garbage(max_heap)

    if min_heap and max_heap:
        print(max_heap[0][0] * -1, min_heap[0][0])
    else:
        print("EMPTY")
        
