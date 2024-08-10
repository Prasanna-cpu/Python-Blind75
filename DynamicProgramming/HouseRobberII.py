

def houseRobber(nums):
    def rob_liner(houses):
        prev_max,curr_max=0,0
        for amount in houses:
            prev_max,curr_max=curr_max,max(curr_max,prev_max+amount)
        return curr_max

    if len(nums)==1:
        return nums[0]


    with_first_house=rob_liner(nums[:-1])
    without_first_house=rob_liner(nums[1:])

    return max(without_first_house,with_first_house)


print(houseRobber([2, 3, 2]))  # Output: 3