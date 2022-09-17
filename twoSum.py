# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    a = eval(input())
    target = eval(input())
    print(solution.twoSum(a,target))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
