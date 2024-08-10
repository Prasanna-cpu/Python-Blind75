def maxProductSubArray(nums):
    maxp=nums[0]
    minp=nums[0]
    result=nums[0]

    for i in range(1,len(nums)):
        if nums[i]<0:
            maxp,minp=minp,maxp
        maxp=max(maxp*nums[i],nums[i])
        minp=min(minp*nums[i],nums[i])
        result=max(result,maxp)

    return result


print(maxProductSubArray([2,3,-2,4]))