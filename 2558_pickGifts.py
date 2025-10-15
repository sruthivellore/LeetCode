import heapq
from math import floor, sqrt


def pickGift(nums, k):
    gifts = [-i for i in nums]
    heapq.heapify(gifts)

    for _ in range(k):
        n = -heapq.heappop(gifts)
        heapq.heappush(gifts, -floor(sqrt(n)))
        print(gifts)
    return -sum(gifts)

print(pickGift([10,34,28,50],3))