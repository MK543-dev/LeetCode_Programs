class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        checklist=set()
        l = 0
        max_len=0

        for i in range(len(s)):
            while s[i] in checklist:
                checklist.remove(s[l])
                l+=1
            checklist.add(s[i])
            max_len=max(max_len, i-l + 1)
        return max_len