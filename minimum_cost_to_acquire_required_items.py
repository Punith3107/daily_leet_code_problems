class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        both = min(need1, need2)

        cost = both * min(costBoth, cost1 + cost2)

        remaining1 = need1 - both
        remaining2 = need2 - both

        cost += remaining1 * min(cost1, costBoth)
        cost += remaining2 * min(cost2, costBoth)

        return cost
