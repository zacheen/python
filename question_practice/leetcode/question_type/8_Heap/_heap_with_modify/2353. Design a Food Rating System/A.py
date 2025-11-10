# 2353. Design a Food Rating System, Medium
# https://leetcode.com/problems/design-a-food-rating-system

from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop

# my solution 1 : using heap + hashmap to track the newest rating of food
# 98ms Beats85.49%
from heapq import heappush
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_2_cuisines = {}
        self.food_2_ratings = {}
        self.food_ratings = defaultdict(list) # using bucket sort to classify cuisines
        for f, c, r in zip(foods, cuisines, ratings) :
            self.food_2_cuisines[f] = c
            self.food_2_ratings[f] = r
            heappush(self.food_ratings[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        # print("in changeRating", food, newRating)
        cuisines = self.food_2_cuisines[food]
        self.food_2_ratings[food] = newRating
        heappush( self.food_ratings[cuisines], (-newRating, food) )

    def highestRated(self, cuisine: str) -> str:
        # print("in highestRated", cuisine)
        heap_ratings = self.food_ratings[cuisine]
        while True :
            best_food_info = heap_ratings[0]
            best_food = best_food_info[1]
            best_food_r = -best_food_info[0]
            if self.food_2_ratings[best_food] == best_food_r :
                return best_food
            else :
                heappop(heap_ratings)

