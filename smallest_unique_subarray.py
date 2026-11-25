class Solution:
    def smallestUniqueSubarray(self, nums):
        n=len(nums)
        m1=10**9+7
        m2=10**9+9
        b1=911382323
        b2=972663749

        def check(k):
            p1=pow(b1,k-1,m1)
            p2=pow(b2,k-1,m2)
            h1=h2=0
            for i in range(k):
                h1=(h1*b1+nums[i])%m1
                h2=(h2*b2+nums[i])%m2
            freq={}
            for i in range(n-k+1):
                key=(h1,h2)
                freq[key]=freq.get(key,0)+1
                if i<n-k:
                    h1=((h1-nums[i]*p1)*b1+nums[i+k])%m1
                    h2=((h2-nums[i]*p2)*b2+nums[i+k])%m2
            return 1 in freq.values()

        lo,hi=1,n
        while lo<hi:
            mid=(lo+hi)//2
            if check(mid):
                hi=mid
            else:
                lo=mid+1
        return lo
