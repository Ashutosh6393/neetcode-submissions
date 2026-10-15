class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1): 
            return False
        
        f_map = {}

        for i in s1:
            f_map[i] = f_map.get(i, 0) +  1
        
        j = 0

        f2_map = {}
        for i in range(0, len(s2)):

            curr_len = i - j + 1
           
            if curr_len > len(s1): 
                f2_map[s2[j]] -= 1

                if f2_map[s2[j]] == 0: 
                    f2_map.pop(s2[j])

                j += 1

            f2_map[s2[i]] = f2_map.get(s2[i], 0) + 1
                
            
            if f_map == f2_map: 
                return True

        return False
                 


            

            


            









        