from heapq import heappop, heappush
from collections import deque


def find_maximised_minimum(arr, n, m, k):

    """
    arr -> Array, n-> Size of array
    m -> increment operation that can be performed
    k -> window size
    """

    heap = []
    q = deque()
    # sliding window + heap building
    for i in range(k):
        while q and arr[q[-1]] > arr[i]:
            q.pop()
        q.append(i)

    for i in range(k, n):
        heappush(heap, [arr[q[0]], i - k, i - 1])
        while q and q[0] <= i - k:
            q.popleft()
        while q and arr[q[-1]] > arr[i]:
            q.pop()
        q.append(i)
    
    heappush(heap, [arr[q[0]], n - k, n - 1])

    # auxiliary array
    temp = [0 for i in range(n)]

    # performing M increment operations
    while m:
        top = heappop(heap)
        temp[top[1]] += 1
        try:
            temp[top[2] + 1] -= 1
        except:
            # when the index is last, so just ignore
            pass
        top[0] += 1
        heappush(heap, top)
        m -= 1

    # finding cumulative sum 
    sumi = 0
    for i in range(n):
        sumi += temp[i]
        arr[i] += sumi
    print(min(arr))


if __name__ == '__main__':
    # find([1, 2, 3, 4, 5, 6], 6, 5, 2)
    # find([73, 77, 60, 100, 94, 24, 31], 7, 9, 1)
    # find([24, 41, 100, 70, 97, 89, 38, 68, 41, 93], 10, 6, 5)
    # find([88, 36, 72, 72, 37, 76, 83, 18, 76, 54], 10, 4, 3)
    find_maximised_minimum([98, 97, 23, 13, 27, 100, 75, 42], 8, 5, 1)
