class Solution:
    def maxLength(self, nums):
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        ans=1
        n=len(nums)
        for i in range(n):
            p=1
            g=0
            l=1
            for j in range(i,n):
                x=nums[j]
                p*=x
                g=gcd(g,x)
                l=l*x//gcd(l,x)
                if p==g*l:
                    ans=max(ans,j-i+1)
        return ans
      
