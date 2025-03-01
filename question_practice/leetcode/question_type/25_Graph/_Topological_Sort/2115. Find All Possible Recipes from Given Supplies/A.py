# 2115. Find All Possible Recipes from Given Supplies
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

from typing import List
from math import inf
from collections import defaultdict

# my 67ms Beats65.72%
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        li = defaultdict(list)
        deg = defaultdict(int)
        for rec, ing_l in zip(recipes, ingredients) :
            deg[rec] += len(ing_l)
            for ing in ing_l :
                li[ing].append(rec)

        end_point = supplies
        ans = []
        while end_point:  # 拓樸排序，剪掉圖上所有樹枝
            now_n = end_point.pop()
            for nei_n in li[now_n] :
                deg[nei_n] -= 1
                if deg[nei_n] == 0:
                    end_point.append(nei_n)
                    ans.append(nei_n)
        return ans

# given ans
# using DFS and cache (so don't have to identify every recipe)


s = Solution()
print("ans :",s.findAllRecipes(recipes = ["bread"], 
    ingredients = [["yeast","flour"]], 
    supplies = ["yeast","flour","corn"])) # ["bread"]
print("ans :",s.findAllRecipes(recipes = ["bread","sandwich"], 
    ingredients = [["yeast","flour"],["bread","meat"]], 
    supplies = ["yeast","flour","meat"])) # ["bread","sandwich"]
print("ans :",s.findAllRecipes(recipes = ["bread","sandwich","burger"], 
    ingredients = [["yeast","flour"],["bread","meat"],["bread","meat"]], 
    supplies = ["yeast","flour","meat"])) # ["bread","sandwich","burger"]



