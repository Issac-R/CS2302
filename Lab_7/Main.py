''' 
    Cs2302 Data Structures
    Issac Rivas (80604101)
    Lab 6
    Dr.Fuentes
    
'''
import math
import numpy as np
import graph_AL as gAL
import graph_AM as gAM
import graph_EL as gEL

#Part 1:Randomized Algorithms
def RandomizedHamiltion(V, E):
    if len(E.el) < V:
        print('Not enough Edges')
    for i in range(2**(len(E.el))):
        Eh = gEL.Graph(V,directed = False)
        temp = np.random.randint(0, len(E.el)-1) 
        while len(Eh.el) < V:
            tempRev = gEL.Edge(E.el[temp].dest, E.el[temp].source)
            while E.el[temp] in Eh.el or tempRev in E.el:
                temp = np.random.randint(0, len(E.el)-1)
            Eh.insert_edge(E.el[temp].source, E.el[temp].dest)
            temp = np.random.randint(0, len(E.el)-1)
        al = Eh.as_AL()
        c, path = cycle(al)
        if check(al) and c:
            return path
    return

def check(g):
    temp = [[0] for i in range(len(g.al))]
    for x in range(len(g.al)):
        if len(g.al[x]) < 2:
            return False
        if g.inDegree(x) < 2:
            return False
        if (g.al[x][0].dest == g.al[x][-1].dest):
            return False
        temp[g.al[x][0].dest][0] += 1
    return True

def cycle(g):
    CC = True
    visited = [0]
    x = 0
    while len(visited) != len(g.al):
        if not(g.al[x][0].dest in visited):
            visited += [(g.al[x][0].dest)]
            x = g.al[x][0].dest
        else:
            visited += [(g.al[x][-1].dest)]
            x = g.al[x][-1].dest
    visited += [0]
    for x in range(len(g.al)):
        if not(x in visited):
            CC = False
    if CC:      
        return True, visited
    return False, visited

#Part 2: Backtracking
def Backtracking(G, pos, used):
    if pos not in set(used):
        used.append(pos)
        if len(used)==len(G.al):
            for x in range(len(G.al[used[-1]])):
                if G.al[used[-1]][x].dest == 0:
                    return used
            return [-1]
        for nextV in range(len(G.al[pos])):
            new = [i for i in used]
            trial = Backtracking(G, G.al[pos][nextV].dest, new)
            if trial is not None:
                return trial
        
#Part3 3: Dynamic Programming
def edit_distance(s1,s2):
    vowels = ['a', 'e', 'i', 'o', 'u']
    normal = s2
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                d[i,j] =d[i-1,j-1]
            else:
                if (s1[i-1] in vowels) and (s2[j-1] in vowels) and (i == j):
                    s2 = s2[:j-1] + s1[i-1] + s2[j:]
                    d[i,j] =d[i-1,j-1]
                elif not(s1[i-1] in vowels) and not(s2[j-1] in vowels) and (i == j):
                    s2 = s2[:j-1] + s1[i-1] + s2[j:]
                    d[i,j] =d[i-1,j-1] 
                else:
                    n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                    d[i,j] = min(n)+1   
    if normal != s2:
        print(normal, 'was modified To: ', s2)
    else:
        print(normal, 'was not Modified')
    return d[-1,-1]                
                
  

if __name__ == "__main__":   

    print("Enter '1' To Check a Graph for Hamiltonian Cycles.")
    print("Enter '2' To Check Modified Edit Distance of 2 Words.")
    print('------------------------------------------------------------------')
    ans = int(input("Input: "))
    while(ans != 1 and ans != 2):
        print()
        print("Incorrect input entered please Try again.")
        print("Enter 1 To Check a Graph for Hamiltonian Cycles.")
        print("Enter 2 To Check Modified Edit Distance of 2 Words.")
        ans = int(input("Input: "))
    if ans == 1:
        print("Choose table implementation:")
        print("Enter '1'  to solve with a Randomized Algorithm.")
        print("Enter '2'  to solve using Backtracking.")
        print('------------------------------------------------------------------')
        ctype = int(input("Input: "))
        while(ctype != 1 and ctype != 2):
            print()
            print("Incorrect input entered please Try again.")
            print("Enter '1'  to solve with a Randomized Algorithm.")
            print("Enter '2'  to solve using Backtracking.")
            ctype = int(input("Input: "))

        #Build Graph
        print('Enter How many Verticies You want the graph to have.')
        vert = int(input("Input: "))
        while(vert <= 2):
            print('Error, Enter a Number Greater then Two.')
            print('Enter How many Verticies You want the graph to have.')
            vert = int(input("Input: "))
        print('------------------------------------------------------------------')
        g = gAL.Graph(vert,directed = False)
        print()
        print('Now Enter all the edges for your graph.')
        edge = 0
        pos = 0
        pos2 = 0
        while edge != -1:
            print('Enter the first vertice.')
            print('Then enter the vertice it will connect to.')
            pos = int(input("Main vertice: "))
            while pos > vert or pos < 0:
                print('Error Incorrect input please enter another number.')
                print('Enter the first vertice.')
                pos = int(input("Main vertice: "))
            pos2 = int(input("Connecting vertice: "))
            while pos2 > vert or pos2 < 0:
                print('Error Incorrect input please enter another number.')
                print('Then enter the vertice it will connect to.')
                pos2 = int(input("Connecting vertice:: "))
            g.insert_edge(pos, pos2)
            
            print()
            print('Enter 0 to add another edge, or')
            print('Enter -1 if you are done adding edges.')
            edge = int(input("Input: "))
            while edge != -1 and edge != 0:
                print('Error Incorrect input please enter another number.')
                print('Enter 0 to add another edge, or')
                print('Enter -1 if you are done adding edges.')
                edge = int(input("Input: "))
            print('------------------------------------------------------------------')
        g.draw()
        
        if ctype == 1:
            temp = RandomizedHamiltion(len(g.al), g.as_EL())
            if temp == None:
                print()
                print('There was No Hamiltion Cycle found using Randomization')
            else:
                print()
                print('The Hamiltion Cycle found using Randomization is:')
                print(temp)
        elif ctype == 2:
            temp = Backtracking(g, 0, [])
            if not(temp == None):
                print()
                print('The Hamiltion Cycle found using Backtracking is:')
                print(temp + [0])
            else:
                print()
                print('There was No Hamiltion Cycle found using BackTracking')
    elif ans == 2:
        print()
        print("Enter the Main word you would like to use.")
        s1 = input("Main Word: ")
        while not(s1.isalpha()):
            print('Word format is incorrect please enter another word.')
            s1 = input("Main Word: ")
        print()
        print("Now enter the word you would like to modified.")
        s2 = input("Second Word: ")
        while not(s2.isalpha()):
            print('Word format is incorrect please enter another word.')
            s2 = input("Second Word: ")
        print('------------------------------------------------------------------')
        print()
        temp = edit_distance(s1.lower(), s2.lower())
        print('The Edit Distance between "' + s1 + '" and "' + s2 + '" is:', temp)