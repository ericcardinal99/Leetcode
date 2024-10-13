def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 1 :
        return 0

    current_longest_string = set()
    longest_len = 0
    left = 0
    right = 0
    while right < len(s):
        if(s[right] in current_longest_string):
            while(s[right] in current_longest_string):
                current_longest_string.remove(s[left])
                left+=1
            current_longest_string.add(s[right])
        else:
            current_longest_string.add(s[right])
            longest_len = max(longest_len, len(current_longest_string))
        right+=1
    return longest_len