def containsDuplicate(nums):
    occ = set()

    for n in nums:
        if n in occ:
            return True
        else:
            occ.add(n)

    return False


print(containsDuplicate([1,6,4,1]))
