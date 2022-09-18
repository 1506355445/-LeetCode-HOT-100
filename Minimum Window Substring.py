class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1 #当counter为0时，代表找到最小覆盖子串的尾指针
            lookup[s[end]] -= 1 #s字符串中每个字符进来就减一
            end += 1 #尾指针向右移
            while counter == 0:
                if min_len > end - start:#找到满足最小子串的长度，但不一定有头指针
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:#子串中出现过两次的字符次数不为0，第一个为0的才是我们要找的头指针
                    counter += 1 #直到找到最小覆盖子串的头指针才跳出循环
                lookup[s[start]] += 1 #头指针所在的字符次数+1，直到下一次遇到该字符时就代表找到另一个覆盖子串
                start += 1
        return res

if __name__ == '__main__':
    s="ADOBECODEBANC"
    t = "ABC"
    solution=Solution()
    print(solution.minWindow(s,t))