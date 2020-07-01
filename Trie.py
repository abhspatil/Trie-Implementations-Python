
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        return TrieNode()
        
    def charToIdx(self,x):
        return ord(x) - ord('a')
        
    def idxToChar(self,idx):
        return chr(idx + ord('a'))
        
    def insert(self,data):
        curr = self.root
        
        for x in data:
            s = self.charToIdx(x)
            
            if not curr.children[s]:
                curr.children[s] = self.getNode()
                
            curr = curr.children[s]
            
        curr.isEnd = True 
        
    
    def search(self,data):
        
        curr = self.root
        
        for x in data:
            s = self.charToIdx(x)
            
            if not curr.children[s]:
                return False
            
            curr = curr.children[s]
            
        return curr and curr.isEnd
        
    def findAll(self):
        curr = self.root
        self.printAll(curr,[])
        
    def printAll(self,root,temp):
        if root.isEnd:
            print("".join(temp))
            
        for i in range(26):
            if root.children[i]:
                self.printAll(root.children[i],temp+[self.idxToChar(i)])
        
    def findAllWithPrefix(self,data):
        print()
        
        curr = self.root
        temp = []
        
        for x in data:
            idx = self.charToIdx(x)
            
            if not curr.children[idx]:
                return
            
            temp.append(x)
            
            curr = curr.children[idx]
        
        self.printAll(curr,temp)
            
            

trie = Trie()

l = ["abcd","abc","cde","def","ab","abcef"]

for x in l:
    t.insert(x)
    
for x in l:
    print(t.search(x))    // all True
    
print(t.search("abd"))     // False
 
t.findAll()         //  ["abcd","abc","cde","def","ab","abcef"]

t.findAllWithPrefix("ab")  //  ["ab","abc","abcd","abcef"]
                
            
