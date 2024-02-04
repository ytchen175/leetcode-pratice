class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1, hash_map2 = dict(), dict()
        
        for i in s:
            if i in hash_map1:
                hash_map1[i] += 1
            else:
                hash_map1[i] = 1

        for j in t:
            if j in hash_map2:
                hash_map2[j] += 1
            else:
                hash_map2[j] = 1
        
        return hash_map1 == hash_map2