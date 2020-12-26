class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
         
        result = {}
        count = 0
        for s in stones:
            if s not in result:
                result[s] = 1
            else:
                result[s] += 1

        for j in jewels:
            if j in result:
                count += result[j]
        return count