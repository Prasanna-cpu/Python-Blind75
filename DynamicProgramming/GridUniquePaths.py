def UniquePaths(m,n):
    dp=[[0]*n for _ in range(m)]

    for i in range(m):
        dp[i][0]=1
    for j in range(n):
        dp[0][j]=1

    if m==1 or n==1:
        return 1

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]

    return dp[m-1][n-1]


print(UniquePaths(5,5))