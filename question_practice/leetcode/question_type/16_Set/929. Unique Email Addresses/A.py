# 929. Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses

from typing import List
from math import inf

# my 
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails :
            l, d = e.split("@")
            l = l.split("+")[0]
            l = l.replace(".", "")
            s.add(l + "@" + d)
        return len(s)

s = Solution()
print("ans :",s.numUniqueEmails(["test.email+alex@leetcode.com",
                              "test.e.mail+bob.cathy@leetcode.com",
                              "testemail+david@lee.tcode.com"]))



