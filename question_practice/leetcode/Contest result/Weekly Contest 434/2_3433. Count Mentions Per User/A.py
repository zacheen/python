# 3433. Count Mentions Per User
# https://leetcode.com/problems/count-mentions-per-user/description/

from typing import List
import functools

# my 24ms Beats100.00%
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        for each_item in events :
            each_item[1] = int(each_item[1])
        events.sort(key = lambda x : (x[1], 0 if x[0] == "OFFLINE" else 1))
        # print(events)
        
        ans = [0]*numberOfUsers
        off_deadline = [0]*numberOfUsers
        all_cou = 0
        for ev, ti, st in events :
            if ev == "MESSAGE" :
                if st == "ALL" :
                    all_cou += 1
                elif st == "HERE" :
                    for user_id in range(numberOfUsers) :
                        if ti >= off_deadline[user_id] :
                            ans[user_id] += 1
                else : 
                    for each_s in st.split(" ") :
                        ans[int(each_s[2:])] += 1
            elif ev == "OFFLINE" :
                off_deadline[int(st)] = ti + 60
            else :
                assert Exception

        for user_id in range(numberOfUsers) :
            ans[user_id] += all_cou
        return ans




