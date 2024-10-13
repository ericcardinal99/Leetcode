def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    current_longest = 1
    total_longest = 1
    prev_num = float('inf')
    nums.sort()
    for num in nums:
        if prev_num == num - 1:
            current_longest+=1
        elif prev_num != num:
            current_longest = 1  
        if current_longest > total_longest:
            total_longest = current_longest
        prev_num = num
    return total_longest

    '''
    nums = [100, 4, 200, 1, 3, 2]
    nums = [1, 2, 3, 4, 100, 200]
    prev_num = 1
    current_longest = 1
    total_longest = 4
    prev_num = inf
        num = 200
    return 4  
    '''