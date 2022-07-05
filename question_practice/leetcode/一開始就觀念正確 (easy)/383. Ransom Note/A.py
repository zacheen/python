# my Runtime: 58 ms, faster than 80.12% of Python3
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)
        
        for c, n in r_count.items() :
            if m_count[c] < n :
                return False
        return True

# given ans 一樣

s = Solution()
print(s.canConstruct())



