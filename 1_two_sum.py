def twoSum(nums, target):
    seen = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i


print(twoSum([1,2,3,56,2], 57))
