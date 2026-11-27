class Solution:
    def maximumSaleItems(self, items, budget):
        n=len(items)
        bonus=[]
        for i in range(n):
            f=items[i][0]
            bonus.append(1+sum(items[j][0]%f==0 for j in range(n) if i!=j))

        dp=[-1]*(budget+1)
        dp[0]=0
        ans=0

        for i in range(n):
            p=items[i][1]
            v=bonus[i]
            for c in range(budget,p-1,-1):
                if dp[c-p]!=-1:
                    dp[c]=max(dp[c],dp[c-p]+v)

        for c in range(budget+1):
            if dp[c]>=0:
                ans=max(ans,dp[c]+(budget-c)//min(items[i][1] for i in range(n)))

        return ans
