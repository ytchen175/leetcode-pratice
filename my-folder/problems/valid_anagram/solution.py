class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = dict()
        hash_map1 = dict()
        
        for i in s:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        for i in t:
            if i not in hash_map1:
                hash_map1[i] = 1
            else:
                hash_map1[i] += 1
                
        return hash_map == hash_map1