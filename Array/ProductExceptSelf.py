def productExceptSelf(nums):
    n = len(nums)
    left, right, result = [1] * n, [1] * n, [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(n):
        result[i] = left[i] * right[i]

    return result


print(productExceptSelf([1, 2, 3, 4]))
