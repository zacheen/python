# 3387. Maximize Amount After Two Days of Conversions
# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/description/
# special limitation
    # The input is generated such that there are no contradictions or cycles in the conversion graphs for either day. 
        # Therefore, can use seen and dont have to worry about best route
    # 1 <= n == pairs1.length <= 10 : so DFS at most do ten times
from typing import List
import functools

# given ans
from collections import defaultdict
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        # Build the conversion graph and find maximum conversion rates
        day1_conversions = self.build_conversion_graph(pairs1, rates1, initialCurrency)
        day2_conversions = self.build_conversion_graph(pairs2, rates2, initialCurrency)
        
        # Calculate the maximum amount that can be obtained
        return max(day1_conversions.get(currency, 0) / rate for currency, rate in day2_conversions.items())

    def build_conversion_graph(self, pairs: List[List[str]], rates: List[float], start_currency: str):
        graph = defaultdict(list)
        for (source, target), rate in zip(pairs, rates):
            graph[source].append((target, rate))
            graph[target].append((source, 1 / rate))
        
        conversion_rates = {}
        def dfs(currency: str, value: float):
            if currency in conversion_rates:
                return
            conversion_rates[currency] = value
            for neighbor, rate in graph[currency]:
                dfs(neighbor, value * rate)
        dfs(start_currency, 1.0)
        return conversion_rates

s = Solution()
print("ans :",s.maxAmount(initialCurrency = "EUR", 
    pairs1 = [["EUR","USD"],["USD","JPY"]], 
    rates1 = [2.0,3.0], 
    pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], 
    rates2 = [4.0,5.0,6.0])) # 720
print("ans :",s.maxAmount(initialCurrency = "NGN", 
    pairs1 = [["NGN","EUR"]], 
    rates1 = [9.0], 
    pairs2 = [["NGN","EUR"]], 
    rates2 = [6.0])) # 1.5
print("ans :",s.maxAmount(initialCurrency = "USD", 
    pairs1 = [["USD","EUR"]], 
    rates1 = [1.0], 
    pairs2 = [["EUR","JPY"]], 
    rates2 = [10.0])) # 1



