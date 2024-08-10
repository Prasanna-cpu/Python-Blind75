

def CountBits(n):
    ans=[0]*(n+1)

    ans[0]=0

    for i in range(1,n):
        ans[i]=ans[i>>1]+(n&1)
    return ans

print(CountBits(7))