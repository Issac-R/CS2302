import numpy as np

class HashTableLP(object):
    def __init__(self,size, hashNum):  
        self.item = np.zeros(size,dtype=np.object)-1
        self.hashNum = hashNum
        
def insert(self,k):
    for i in range(len(self.item)):
        pos = h(self, k)+i
        if pos >= len(self.item):
            pos = pos - len(self.item)
        if self.item[pos] == -1:
            self.item[pos] = k
            return pos
    return -1

def find(self,k):
    for i in range(len(self.item)):
        pos = h(self, k)+i
        if pos >= len(self.item):
            pos = pos - len(self.item)
        if self.item[pos] == -1:
            return -1
        if self.item[pos].word == k.word:
            return pos
    return -1
 
def delete(self,k):
    f = self.find(k)
    if f >=0:
        self.item[f] = -2
    return f

def h(self,k):
    if self.hashNum == 1:
        return ((len(k.word)-1)) % len(self.item)
    elif self.hashNum == 2:
        return ord(k.word[0]) % len(self.item) 
    elif self.hashNum == 3:
        return (ord(k.word[0])+ord(k.word[-1])) % len(self.item) 
    elif self.hashNum == 4:
        sum = 0
        for x in range(len(k.word)):
            sum = sum + ord(k.word[x])
        if sum > len(self.item):
            sum = sum - len(self.item)
        return (sum % len(self.item))
    elif self.hashNum == 5:
        return recursiveForm(self, len(self.item), k.word)
    else:
        mx = 0
        for x in range(len(k.word)):
             temp = ord(k.word[x])
             if temp > mx:
                 mx = temp
        return mx % len(self.item) 

def recursiveForm(self, n, s):
    if s == '':
        return 1
    else:
        return ((ord(s[0]) + 255*recursiveForm(self, n, s[1:])) % n)
        
def print_table(self):
    print('Table contents:')
    print(self.item)
    
def n(self, k):
    temp = []
    hash = self.h(k)
    for b in self.item:
        if self.h(b) == hash:
            temp.append(b)
    if len(temp) < 1:
        return -1
    else:
        temp.sort()
        return temp[len(temp)-1]
    
def resize(H):
    new = HashTableLP(len(H.item)*2, H.hashNum)
    for x in range(len(H.item)):
      if H.item[x] != -1:
        insert(new, H.item[x])
    return new