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
        
def deleteString(root,word,index):
    ch=word[index]
    currentNode=root.children.get(ch)
    canThisNodeBeDeleted=False
    if len(currentNode.children)>1:
        deleteString(currentNode,word,index+1)
        return False
    if index==len(word)-1:
        if len(currentNode.children)>=1:
            currentNode.isEndOfWord=False
            return True
        else:
            root.children.pop(ch)
            return True
    if currentNode.isEndOfWord:
        deleteString(currentNode,word,index+1)
        return False
    canThisNodeBeDeleted=deleteString(currentNode,word,index+1)
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        return True
    else:
        return False
            
newTrie = Trie()
newTrie.insertString('APP')
newTrie.insertString('APPL')
deleteString(newTrie.root,'APP',0)
print(newTrie.search('APP'))