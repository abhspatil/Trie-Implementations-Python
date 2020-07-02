


class TrieNode:
    def __init__(self):
        self.childs = [None]*20
        self.val = -1
        
class Trie:
    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        return TrieNode()
        
    def insert(self,val):
        curr = self.root
        
        for i in range(31,-1,-1):
            if val & 1<<i:
                digit = 1 
            else:
                digit = 0

            if not curr.childs[digit]:
                curr.childs[digit] = self.getNode()
            
            curr = curr.childs[digit]
        
        curr.val = val 
        
    
    def maxXor(self,arr):
        ma=0
        
        for curr in arr:
            root = self.root
            
            for i in range(31,-1,-1):
                if (curr & 1<<i):
                    digit = 1 
                else:
                    digit = 0  
                    
                
                if digit == 0:
                    if root.childs[1]:
                        root = root.childs[1]
                    else:
                        root = root.childs[0]
                        
                else:
                    if root.childs[0]:
                        root = root.childs[0]
                    else:
                        root = root.childs[1]
                    
            ma = max(ma,root.val ^ curr)
                
         
        print(ma)           
        return ma

def maxXor(arr):
    ma=0
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            ma = max(ma,arr[i]^arr[j])
            
    print(ma)
 

arr=[i for i in range(100)]

maxXor(arr)
            
t= Trie()

for x in arr:
    t.insert(x)
    
t.maxXor(arr)
                
                
        

