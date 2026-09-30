class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        for str in strs:
            key = tuple(sorted(str))
            if key not in hashmap:
                hashmap[key] = []
                
            hashmap[key].append(str)


        ans = []
        for k,v in hashmap.items():
            ans.append(v)

        return ans
        