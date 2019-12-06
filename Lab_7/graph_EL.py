import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL as gAL
import graph_AM as gAM

class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vert, weighted=False, directed = False):
        self.el = []
        self.vert = vert
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
        
    def insert_edge(self,source,dest,weight=1):
        if self.directed != True:
            for x in range(len(self.el)):
                if self.el[x].source == source and self.el[x].dest == dest and self.el[x].weight == weight:
                    return
        self.el.append(Edge(source, dest, weight))
    
    
    def delete_edge(self,source,dest):
        for x in range(len(self.el)-1):
            if self.el[x].source == source and self.el[x].dest == dest:
                del self.el[x]
                
                
    def display(self):
        for x in range(len(self.el)):
            print(self.el[x].source, self.el[x].dest, self.el[x].weight)
     
    def draw(self):
         temp = self.as_AL()
         temp.draw()
            
    def as_EL(self):
        return self
    
    def as_AM(self):
        temp = gAM.Graph(self.vert ,directed = False)
        for x in range(len(self.el)):
            temp.insert_edge(self.el[x].source, self.el[x].dest)
        return temp
    
    def as_AL(self):
        temp = gAL.Graph(self.vert ,directed = False)
        for x in range(len(self.el)):
            temp.insert_edge(self.el[x].source, self.el[x].dest)
        return temp
    
    def BFS(self):
        frontierQueue = []
        discoveredSet = []
        frontierQueue.append(0)
        discoveredSet.append(0)
        path = [[] for i in range(self.vert)]
        
        while(len(frontierQueue) >  0):
           currentV = frontierQueue.pop(0)
           for x in range(len(self.el)):        
               if(self.el[x].dest not in discoveredSet and self.el[x].source ==  currentV):
                   frontierQueue.append(self.el[x].dest)
                   discoveredSet.append(self.el[x].dest)
                   path[currentV].append(self.el[x].dest)
                   
        return path
    
    def DFS(self):
        Stack = []
        discoveredSet = []
        Stack.append(0)
        discoveredSet.append(0)
        path = [[] for i in range(self.vert)]
    
        while(len(Stack) >  0):
           currentV = Stack.pop()
           for x in range(len(self.el)):        
               if(self.el[x].dest not in discoveredSet and self.el[x].source ==  currentV):
                   Stack.append(self.el[x].dest)
                   discoveredSet.append(self.el[x].dest)
                   path[currentV].append(self.el[x].dest)
                   
        return path
