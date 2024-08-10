
def Minimum(nums):
    n=len( nums)
    l=0
    r=n-1

    while l<r:
        mid=l+( r - l )// 2

        if nums[mid]>nums[r]:
            l=mid + 1

        else:
            r=mid
    return nums[l]




print((Minimum([3,4,5, 1, 2] )))
