class Solution(object):
    def maxIceCream(self, costs, coins):
        if coins < min(costs):
            return 0
        c = 0
        costs.sort()
        s = 0
        for i in range(len(costs)):
            s = s + costs[i]
            if s <= coins:
                c = c + 1
            else:
                break
        
        return c
