# MY
# def minWindow(s: str, t: str) -> str :
#     longStr = s
#     longLen = len(longStr)
#     minsubCount = 10000
#     minStart = 0
#     minEnd = 0
#     haveAns = False
#     for i in range(longLen) :
#         countLen = 0
#         copysub = list(t).copy()
#         for ii in range(i, longLen) :
#             try :
#                 copysub.remove(longStr[ii])
#             except ValueError :
#                 pass
#             if len(copysub) == 0 :
#                 haveAns = True
#                 shortLen = ii - i
#                 if shortLen < minsubCount :
#                     minsubCount = shortLen
#                     minStart = i
#                     minEnd = ii
#                 break
    
#     if haveAns :
#         return longStr[minStart : minEnd+1]
#     else :
#         return ""

# # Given answer
# from collections import Counter
# def minWindow(s: str, t: str) :
#     # Dictionary which keeps a count of all the unique characters in t.
#     dict_t = Counter(t)

#     # Number of unique characters in t, which need to be present in the desired window.
#     required = len(dict_t)

#     # left and right pointer
#     l, r = 0, 0

#     # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
#     # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
#     formed = 0

#     # Dictionary which keeps a count of all the unique characters in the current window.
#     window_counts = {}

#     # ans tuple of the form (window length, left, right)
#     ans = float("inf"), None, None

#     while r < len(s):

#         # Add one character from the right to the window
#         character = s[r]
#         window_counts[character] = window_counts.get(character, 0) + 1

#         # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
#         if character in dict_t and window_counts[character] == dict_t[character]:
#             formed += 1

#         # Try and contract the window till the point where it ceases to be 'desirable'.
#         while l <= r and formed == required:
#             character = s[l]

#             # Save the smallest window until now.
#             if r - l + 1 < ans[0]:
#                 ans = (r - l + 1, l, r)

#             # The character at the position pointed by the `left` pointer is no longer a part of the window.
#             window_counts[character] -= 1
#             if character in dict_t and window_counts[character] < dict_t[character]:
#                 formed -= 1

#             # Move the left pointer ahead, this would help to look for a new window.
#             l += 1    

#         # Keep expanding the window once we are done contracting.
#         r += 1    
#     return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# try by my self
from collections import Counter
import sys
def minWindow(s: str, t: str) :
    l, r = 0,0
    dict_t = Counter(t)
    # print(dict_t)
    subKeys = dict_t.keys()
    need_match_word = len(dict_t)
    minLen = sys.maxsize
    minL = 0
    minR = 0
    haveAns = False

    longLen = len(s)
    while r < longLen :
        # print("r :",r ,"s[r] : ",s[r])
        eachLongWord = s[r]
        if eachLongWord in subKeys :
            # print("add match word : ",eachLongWord)
            # print("need_match_word :",need_match_word)
            # print("dict_t :",dict_t)
            dict_t[eachLongWord] = dict_t[eachLongWord] -1
            # print("after dict_t :",dict_t)
            if dict_t[eachLongWord] == 0 :
                need_match_word = need_match_word - 1
                if need_match_word == 0 :
                    # 判斷到這裡代表剛好符合substring
                    while l <= r :
                        # print("r :",r, "l :",l)
                        eachLongWord_l = s[l]
                        if eachLongWord_l in subKeys :
                            # print("minus match word : ",eachLongWord_l)
                            dict_t[eachLongWord_l] = dict_t[eachLongWord_l] + 1
                            if dict_t[eachLongWord_l] == 1 :
                                # 代表不符合substring了
                                need_match_word = need_match_word + 1
                                thisLen = r - l # 反正標準一樣所以沒差
                                if thisLen < minLen :
                                    # print("l,r : ",l,r)
                                    minL = l # 這個字不包含 因為已經脫離substr了
                                    minR = r
                                    minLen = thisLen
                                    haveAns = True
                                l = l + 1
                                break
                        l = l + 1
        r = r + 1
    if haveAns :
        # print("minL:minR",minL,minR)
        return s[minL:minR+1]
    else :
        return ""

print("ANS :",minWindow(s = "abc", t = "ab"))
# print(minWindow(s = "ADOBECODEBANC", t = "ABC"))