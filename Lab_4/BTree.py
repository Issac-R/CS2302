# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:18:15 2019

@author: Issac
"""
class BTree(object):
    def __init__(self,data,max_data,child=[],isLeaf=True):  
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data
    
def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.data =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)  
        
def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        if k.word < T.data[i].word:
            return i
    return len(T.data)

def FindChildSearch(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        if k.word < T.data[i].word:
            return i
    return len(T.data)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTree(T.data[:mid],max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTree(T.data[:mid],T.max_data,T.child[:mid+1],T.isLeaf)
        rightChild = BTree(T.data[mid+1:],T.max_data,T.child[mid+1:],T.isLeaf) 
    return T.data[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):  
    temp = []
    for x in range(0, len(T.data)):
        temp.append(T.data[x].word)
    temp.append(i.word)
    temp.sort()
    for y in range(0,len(temp)):
        if temp[y] == i.word:
            T.data.insert(y, i)
            return

def IsFull(T):
    return len(T.data) >= T.max_data

def Leaves(T):
    # Returns the leaves in a b-tree
    if T.isLeaf:
        return [T.data]
    s = []
    for c in T.child:
        s = s + Leaves(c)
    return s
     
def Height(T):
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[0])    
         
def PrintD(T,space):
    # Prints data and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i].word)
    else:
        PrintD(T.child[len(T.data)],space+'   ')  
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i].word)
            PrintD(T.child[i],space+'   ')
 
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    for x in range(0, len(T.data)):
        if k.word == T.data[x].word:
            return T.data[x]
    if T.isLeaf:
        return None
    return Search(T.child[FindChildSearch(T,k)],k)

def Set_x(T,Dx):
    # Finds x-coordinate to display each node in the tree
    if T.isLeaf:
        return 
    else:
        for c in T.child:
            Set_x(c,Dx)
        d = (Dx[T.child[0].data[0]] + Dx[T.child[-1].data[0]] + 10*len(T.child[-1].data))/2
        Dx[T.data[0]] = d - 10*len(T.data)/2
        
def NumItems(T):
    if T.isLeaf:
        return len(T.data)
    else:
        totalBelow = len(T.data)
        for x in range(0, len(T.child)):
            totalBelow = totalBelow + NumItems(T.child[x])
        return totalBelow
