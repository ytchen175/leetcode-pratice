class TrieNode:
    def __init__(self):
        self.childrens = dict() 
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.childrens:
                curr.childrens[w] = TrieNode()
                curr = curr.childrens[w]
            else:
                curr = curr.childrens[w]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for w in word:
            if w not in curr.childrens:
                return False
            else:
                curr = curr.childrens[w]

        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for w in prefix:
            if w not in curr.childrens:
                return False
            else:
                curr = curr.childrens[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)