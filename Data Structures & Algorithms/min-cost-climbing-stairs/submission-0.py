class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def solve(n):
            if n<=1:
                return 0
            if n in dp:
                return dp[n]
            dp[n]=min(cost[n-1]+solve(n-1),cost[n-2]+solve(n-2))

            return dp[n]

        return solve(len(cost))
            
        