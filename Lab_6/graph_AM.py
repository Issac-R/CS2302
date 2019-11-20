import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL as gAL
import graph_EL as gEL

class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.am = np.zeros((vertices,vertices),dtype=int)-1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    def insert_edge(self,source,dest,weight=1):
        if self.directed != True:
            self.am[source][dest], self.am[dest][source] = weight, weight
        self.am[source][dest] = weight
        
    def delete_edge(self,source,dest):
        if self.directed != True:
            self.am[source][dest], self.am[dest][source] = -1, -1
        self.am[source][dest] = -1
                
    def display(self):
        print(self.am)
     
    def draw(self):
        temp = self.as_AL()
        temp.draw()
    
    def as_EL(self):
        temp = gEL.Graph(16,directed = False)
        for x in range(len(self.am)):
            for y in range(len(self.am[x])):
                if self.am[x][y] != -1:
                    temp.insert_edge(x, y)
        return temp
    
    def as_AM(self):
        return self
    
    def as_AL(self):
        temp = gAL.Graph(16,directed = False)
        for x in range(len(self.am)):
            for y in range(len(self.am[x])):
                if self.am[x][y] != -1:
                    temp.insert_edge(x, y)
        return temp
    
    def BFS(self):
        frontierQueue = []
        discoveredSet = []
        frontierQueue.append(0)
        discoveredSet.append(0)
        path = [[] for i in range(self.vertices)]
    
        while(len(frontierQueue) >  0):
           currentV = frontierQueue.pop(0)
           for x in range(len(self.am[currentV])):        
               if(x not in discoveredSet and self.am[currentV][x] != -1):
                   frontierQueue.append(x)
                   discoveredSet.append(x)
                   path[currentV].append(x)
                   
        return path
    
    def DFS(self):
        Stack = []
        discoveredSet = []
        Stack.append(0)
        discoveredSet.append(0)
        path = [[] for i in range(self.vertices)]
    
        while(len(Stack) >  0):
           currentV = Stack.pop()
           for x in range(len(self.am[currentV])):        
               if(x not in discoveredSet and self.am[currentV][x] != -1):
                   Stack.append(x)
                   discoveredSet.append(x)
                   path[currentV].append(x)
                   
        return path
    
    
        
