# my 
# Beats 100%
class Solution(object):
    def averageWaitingTime(self, customers):
        total_wait_time = 0
        next_start_time = 0
        for arrive_time, prepare_time in customers :
            if next_start_time < arrive_time :
                total_wait_time += prepare_time
                next_start_time = arrive_time + prepare_time
            else :
                next_start_time = next_start_time + prepare_time
                total_wait_time += (next_start_time - arrive_time)
        return total_wait_time/len(customers)
# given ans

s = Solution()
print(s.averageWaitingTime([[1,2],[2,5],[4,3]]))
print(s.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))



