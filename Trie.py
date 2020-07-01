
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
        
        curr = self.root
        temp = []
        
        for x in data:
            idx = self.charToIdx(x)
            
            if not curr.children[idx]:
                return
            
            temp.append(x)
            
            curr = curr.children[idx]
            
        
        self.printAll(curr,temp)
            
    def count(self):
        curr = self.root
        
        return self.countWords(curr)
        
    def countWords(self,root):
        res=0
        
        if root.isEnd:
            res+=1 
            
        for i in range(26):
            if root.children[i]:
                res += self.countWords(root.children[i])
                
        return res
        
    def countChildrens(self,root,idx):
        res=0
            
        for i in range(26):
            if root.children[i]:
                res += 1
                idx[0] = i 
                
        return res
        
    def commonPrefix(self):
        
        curr = self.root
        temp=[]
        
        idx=[-1]
        
        while self.countChildrens(curr,idx) == 1 and not curr.isEnd:
            temp.append(self.idxToChar(idx[0]))
            
            curr = curr.children[idx[0]]
            
        return "".join(temp)
        
        
    def wordsWithgivenLetters(self,arr):
        hs=[False]*26
        
        for x in arr:
            hs[self.charToIdx(x)] = True
            
        #print(hs)
        
        curr = self.root
        res=[]
        
        for i in range(26):
            if hs[i] and curr.children[i]:
                self.printWordsWithLetters(curr,hs,res,[])
                
            #print(i,curr.children[i])
            
        return res
    
    def printWordsWithLetters(self,root,hs,res,temp):
        if root.isEnd:
            res.append("".join(temp))
            
        for i in range(26):
            if hs[i] and root.children[i]:
                self.printWordsWithLetters(root.children[i],hs,res,temp + [self.idxToChar(i)])
                
        
    def wordBreak(self,word):
        
        res = []
        self.wordBreakAll(word,res,[])
        
        return res 
        
    def wordBreakAll(self,word,res,temp):
        
        if len(word)==0:
            res.append(temp)
            print(temp)
            return
                
                
        for i in range(len(word)):
            prefix = word[:i+1]
            
            print(prefix)
            if self.search(prefix):
                
                self.wordBreakAll(word[i+1:],res,temp+[prefix])
    
    
    
            
            
t = Trie()

l = ["abcd","abc","ab","abcef","abc"]

for x in l:
    t.insert(x)
    
for x in l:
    print(t.search(x))
    
print(t.search(""))

#t.findAll()

t.findAllWithPrefix("ab")
                
print(t.count())

print(t.commonPrefix())

arr = ['a','b','c','d']

print(t.wordsWithgivenLetters(arr))

t1 = Trie()

l = ["abcd","abc","d","ab","cd","a","bcd","def"]

for x in l:
    t1.insert(x)
    
print(t1.wordBreak("abcd"))
