def combinationSum(candidates,target):

    result=[]
    def backtrack(start,target,path):
        if target==0:
            result.append(path[:])
            return

        for i in range(start,len(candidates)):
            if target-candidates[i]>=0:
                path.append(candidates)
                backtrack(i,target-candidates[i],path)
                path.pop()

    candidates.sort()
    backtrack(0,target,[])
    return result