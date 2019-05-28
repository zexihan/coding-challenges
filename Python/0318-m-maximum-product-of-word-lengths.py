class Solution:
    def maxProduct(self, words: List[str]) -> int:
        nums = []
        for w in words:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - 97)
            nums.append(mask)
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (nums[i] & nums[j]):
                    res = max(res, len(words[i] * len(words[j])))
        return res
