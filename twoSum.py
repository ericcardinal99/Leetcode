def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_dictionary = {}
    for i in range(len(nums)):
        current_num = nums[i]
        other_num = target - current_num
        if other_num in num_dictionary:
            return [num_dictionary[other_num], i]
        if not(current_num in num_dictionary):
            num_dictionary[current_num] = i
    '''
    target = 9
    num_dictionary = {2: 0}
    [2,7,2,11,15]
        i = 2
        current_num = 2
        other_num = 7
        
    [0, 1]
    '''