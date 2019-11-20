import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AM as gAM
import graph_EL as gEL

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'
        
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest,weight)) 
            if not self.directed:
                self.al[dest].append(Edge(source,weight))
    
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i+=1    
        return False
    
    def delete_edge(self,source,dest):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')      
            
    def display(self):
        print('[',end='')
        for i in range(len(self.al)):
            print('[',end='')
            for edge in self.al[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']')   
     
    def draw(self):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
            
    def as_EL(self):
        temp = gEL.Graph(16,directed = False)
        for x in range(len(self.al)):
            for y in range(len(self.al[x])):
                temp.insert_edge(x, self.al[x][y].dest)
        return temp
    
    def as_AM(self):
        temp = gAM.Graph(len(self.al),directed = False)
        for x in range(len(self.al)):
            for y in range(len(self.al[x])):
                temp.insert_edge(x, self.al[x][y].dest)
        return temp
    
    def as_AL(self):
        return self
    
    
    def BFS(self):
        frontierQueue = []
        discoveredSet = []
        frontierQueue.append(0)
        discoveredSet.append(0)
        path = [[] for i in range(len(self.al))]
    
        while(len(frontierQueue) >  0):
           currentV = frontierQueue.pop(0)
           for x in range(len(self.al[currentV])):        
               if(self.al[currentV][x].dest not in discoveredSet):
                   frontierQueue.append(self.al[currentV][x].dest)
                   discoveredSet.append(self.al[currentV][x].dest)
                   path[currentV].append(self.al[currentV][x].dest)
                   
        return path
    
    def DFS(self):
        Stack = []
        discoveredSet = []
        Stack.append(0)
        discoveredSet.append(0)
        path = [[] for i in range(len(self.al))]
    
        while(len(Stack) >  0):
           currentV = Stack.pop()
           for x in range(len(self.al[currentV])):        
               if(self.al[currentV][x].dest not in discoveredSet):
                   Stack.append(self.al[currentV][x].dest)
                   discoveredSet.append(self.al[currentV][x].dest)
                   path[currentV].append(self.al[currentV][x].dest)
                   
        return path
                 