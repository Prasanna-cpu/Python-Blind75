def MaxSumSubarray(nums):
    maxSub = nums[0]

    curr = 0

    for n in nums:
        if curr < 0:
            curr = 0
        curr += n
        maxSub = max(maxSub, curr)
    return maxSub


print(MaxSumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
