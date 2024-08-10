

#House Robber-1

def houseRobberI(nums:[]):
    n=len(nums)

    dp=[0]*n

    if n==0:
        return 0
    elif n==1:
        return nums[0]

    dp[0]=nums[0]
    dp[1]=max(nums[1],nums[0])

    for i in range(2,n):
        dp[i]=max(nums[i]+dp[i-2],dp[i-1])

    return dp[n-1]


print(houseRobberI([1,2,3,1]))