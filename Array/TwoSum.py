def twoSum(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        d = target - num

        if d in num_dict:
            return [num_dict[d], i]
        num_dict[num] = i

    return []


print(twoSum([2,7,11,15],9))
