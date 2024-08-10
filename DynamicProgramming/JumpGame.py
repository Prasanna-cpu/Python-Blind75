def canJump(nums:[]):

    max_reach_idx=0

    for i in range(len(nums)):
        if i>max_reach_idx:
            return False
        max_reach_idx=max(max_reach_idx,i+nums[i])

    return True
