class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []
        sub = []

        def dfs(i, curr):
                if curr == target:
                    res.append(sub.copy())
                    return

                if i >= len(nums) or curr > target:
                    return

                # Include nums[i], allowing reuse
                sub.append(nums[i])
                dfs(i, curr + nums[i])

                # Backtrack
                sub.pop()

                # Exclude nums[i] and move forward
                dfs(i + 1, curr)

        dfs(0, 0)
        return res