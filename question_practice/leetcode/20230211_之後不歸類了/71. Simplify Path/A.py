# my Beats 96.51%
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        for path_name in path.split("/") :
            if path_name == ".." :
                if path_stack :
                    path_stack.pop()
            elif path_name == "" or path_name == "." :
                continue
            else :
                path_stack.append(path_name)
        return "/" + "/".join(path_stack)

# given ans
# 完全一樣

s = Solution()
print(s.simplifyPath(path = "/home/"))
print(s.simplifyPath(path = "/../"))
print(s.simplifyPath(path = "/home//foo/"))



