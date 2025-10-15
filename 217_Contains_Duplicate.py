def containsDuplicate(nums):
    seen = set(nums)
    return len(seen) != len(nums)

print(containsDuplicate([1,2,3,2,5]))