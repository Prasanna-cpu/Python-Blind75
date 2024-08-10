
from collections import Counter
import heapq
def topKFrequent(nums , k: int)
    counter = Counter(nums)
    min_heap = []

    for num, freq in counter.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [num for freq, num in min_heap]