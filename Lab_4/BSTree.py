# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:35:08 2019

@author: Issac
"""
import matplotlib.pyplot as plt
import numpy as np

class BST(object):
    def __init__(self, data, left=None, right=None):  
        self.data = data
        self.left = left 
        self.right = right
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.data.word >= newItem.word:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def numOfNodes(T):
    if T is None:
        return 0
    return numOfNodes(T.left) + 1 + numOfNodes(T.right)

def treeHeight(T):
    if T != None:
        left = 1 + treeHeight(T.left)
        right = 1 + treeHeight(T.right)
        if left > right:
            return 1 + left
        else:
            return 1 + right
    else:
        return -1
    
def Search(T, k):
    if T == None:
        return T
    if T.data.word == k:
        return T
    if T.data.word > k:
        return Search(T.left, k)
    else:
        return Search(T.right, k)
    
    
def DrawBST_(T, x0, x1, y, y_inc,ax):
    if T is not None:
        xm = (x0+x1)/2
        yn = y-y_inc
        if T.left is not None:
            p=np.array([[xm,y], [(x0+xm)/2,yn]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            DrawBST_(T.left,x0,xm,yn, y_inc,ax)
        if T.right is not None:
            p=np.array([[xm,y], [(x1+xm)/2,yn]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            DrawBST_(T.right,xm,x1,yn, y_inc,ax)
        ax.text(xm,y, str(T.data.word), size=10,ha="center", va="center",
            bbox=dict(facecolor='w',boxstyle="circle"))

def DrawBST(T): 
    fig, ax = plt.subplots()
    DrawBST_(T, 0, 200, 400, 20, ax)
    ax.set_aspect(1.0)
    ax.axis('off') 
    plt.show() 
