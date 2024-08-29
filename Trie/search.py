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
    def search(self,word):
        currentNode=self.root
        for i in word:
            node=currentNode.children.get(i)
            if node is None:
                return False
            currentNode=node
        if currentNode.isEndOfWord:
            return True
        else:
            return False
newTrie = Trie()
newTrie.insertString('APP')
newTrie.insertString('APPL')
print(newTrie.search('APP'))
print(newTrie.search('DCD'))