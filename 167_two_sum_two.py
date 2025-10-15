def twoSumTwo(nums, target):
    l,r = 0, len(nums)-1

    while l < r:
        curSum = nums[l] + nums[r]
        print(curSum)
        if curSum < target:
            l += 1
        elif curSum > target:
            r -= 1
        else:
            return [l+1, r+1]


print(twoSumTwo([1,2,4,6], 10))