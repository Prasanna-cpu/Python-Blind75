def LIS(nums):
    n=len(nums)
    dp=[1]*n

    for i in range(1,n):
        for j in range(i):
            if nums[i]>nums[j] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
    return max(dp)


print(LIS([10,9,2,5,3,7,101,18]))