class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        s = nums[0]
        best = float('inf')

        if all(nums[i] == (s + i) % n for i in range(n)):
            best = min(best, (n - s) % n, s + 2 if s else 0)

        if all(nums[i] == (s - i) % n for i in range(n)):
            c = (s + 1) % n
            b = (n - s - 1) % n
            best = min(best, c + 1, b + 1)

        return -1 if best == float('inf') else best
