class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self,word):
        current=self.root
        for char in word:
            node=current.children.get(char)
            if node is None:
                node=TrieNode()
                current.children.update({char:node})
            current=node
        current.isEndOfWord=True
        print('Inserted')

newTrie = Trie()
newTrie.insertString('APP')
newTrie.insertString('APPL')