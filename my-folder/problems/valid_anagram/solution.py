class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_hash_map = dict()
        character_hash_map1 = dict()
        
        if len(s) != len(t):
            return False
        
        else:
            for i in s:
                if i not in character_hash_map:
                    character_hash_map[i] = 1
                else:
                    character_hash_map[i] += 1

            for i in t:
                if i not in character_hash_map1:
                    character_hash_map1[i] = 1
                else:
                    character_hash_map1[i] += 1

        return (character_hash_map == character_hash_map1)