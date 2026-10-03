class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0

        res = 0

        count = {}

        for i in range(len(s)):

            count[s[i]] = 1 + count.get(s[i], 0)


            # while (i - left + 1) - max(count.values()) > k:
            #     count[s[left]] -= 1
            #     left += 1
            
            # res = max(res, i - left +1)

            if (i-left +1) - max(count.values()) <= k:
                res = max(res, i - left + 1)
            else:
                count[s[left]] -= 1
                left += 1

        
        return res





