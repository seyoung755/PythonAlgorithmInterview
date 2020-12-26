import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = collections.Counter(stones)
        count = 0

        for j in jewels:
            count += result[j]
        return count        