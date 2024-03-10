from collections import deque

def steps_to_zero_bfs(arr, k):
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

arr = [5, 1, 1, 3]
k = 2  # Index for which you want to find steps
result = steps_to_zero_bfs(arr, k)
print("Steps required for index", k, "to reach zero (using BFS):", result)