class HashTableChain(object):
    def __init__(self,size, hashNum):  
        self.bucket = [[] for i in range(size)]
        self.hashNum = hashNum
    
def insert(T,k):
    b = h(T, k)
    if len(T.bucket[b]) >= len(T.bucket)*3:
        T = resize(T)
    if not k in T.bucket[b]:
        T.bucket[b].append(k)
        
        
def find(T,k):
    b = h(T, k)
    i = -1
    for x in range(len(T.bucket[b])):
        if T.bucket[b][x].word == k.word:
            i = x
    return b, i
 
def print_table(T):
    print('Table contents:')
    for b in T.bucket:
        print(b)

def delete(T,k):
    b = T.h(k)
    try:
        T.bucket[b].remove(k)
        return 1
    except:
        return -1
    
def resize(H):
    new = HashTableChain(len(H.bucket)*2, H.hashNum)
    for x in range(len(H.bucket)):
      if H.bucket[x] != None:
        for y in range(len(H.bucket[x])):
            insert(new, H.bucket[x][y])
    return new
    
def h(self,k):
    if self.hashNum == 1:
        return ((len(k.word)-1)) % len(self.bucket)
    elif self.hashNum == 2:
        return ord(k.word[0]) % len(self.bucket) 
    elif self.hashNum == 3:
        return (ord(k.word[0])+ord(k.word[-1])) % len(self.bucket) 
    elif self.hashNum == 4:
        sum = 0
        for x in range(len(k.word)):
            sum = sum + ord(k.word[x])
        return sum % len(self.bucket) 
    elif self.hashNum == 5:
        return recursiveForm(self, len(self.bucket), k.word)
    else:
        mx = 0
        for x in range(len(k.word)):
             temp = ord(k.word[x])
             mx += temp * 2302
        return mx % len(self.bucket) 

def recursiveForm(self, n, s):
    if s == '':
        return 1
    else:
        return (ord(s[0]) + 255*recursiveForm(self, n, s[1:])) % n