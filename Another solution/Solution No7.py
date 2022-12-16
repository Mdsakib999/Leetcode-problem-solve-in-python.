def longestConsecutive(nums):
    longest = 0

    for x in nums:
        currNum = x
        currStreak = 1

        while (currNum+1) in nums:
            currNum += 1
            currStreak += 1

        longest = max(currStreak, longest)

    return longest

nums = list(map(int, input("nums = ").split()))

ans = longestConsecutive(nums)
print("Length of longest consecutive subsequence in nums: ", ans)