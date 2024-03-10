from collections import deque

def counterforfinancialtickets_bfs(arr, k):
    steps = 0
    queue = deque([(k, steps)])

    while queue:
        idx, steps = queue.popleft()
        
        while arr[idx] > 0:
            arr[idx] -= 1
            steps += 1
            for i in range(len(arr)):
                if i != idx and arr[i] > 0:
                    arr[i] -= 1
                    queue.append((i, steps + 1))

    return steps
def coutnerforfinancialtickets(arr, k):
    steps = 0

    while arr[k] != 0:
        arr[k] -= 1
        steps += 1
        for i in range(len(arr)):
            if i != k and arr[i] > 0:
                arr[i] -= 1
                steps += 1

    return steps

arr = [5, 1, 7, 3]
k = 1  # Index for which you want to find steps
#result = coutnerforfinancialtickets(arr, k)
result = counterforfinancialtickets_bfs(arr, k)
print("Steps required for index", k, "to reach zero:", result)
