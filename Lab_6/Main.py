''' 
    Cs2302 Data Structures
    Issac Rivas (80604101)
    Lab 6
    Dr.Fuentes
    
'''
import graph_AL as gAL
import graph_AM as gAM
import graph_EL as gEL

def printPathBFS(list):
    x = 0
    print('Path is: ', end = '')
    while x != 15:
        print(x, ', ', end = '')
        x = list[x][0]
    print(x, end = '')
    print()
    
def printPathDFS(list):
    x = 0
    print('Path is: ', end = '')
    while x != 15:
        print(x, ', ', end = '')
        x = list[x][-1]
    print(x, end = '')
    print()


if __name__ == "__main__":   

    g = gAL.Graph(16,directed = False)
    '''
        Proposed Solution:
        Take Chicken Across, Go Back Alone, Take the Fox Across With him, Returm With the chicken,
        Take The Grain Back Across,Leave the grain With the fox and cross back alone, Cross with the chicken.
        (0,5,4,7,2,11,10,15)
        
    '''
    
    #Legal Moves
    
    g.insert_edge(0,5)
    g.insert_edge(2,7)
    g.insert_edge(2,11)
    g.insert_edge(4,5)
    g.insert_edge(4,7)
    g.insert_edge(4,13)
    g.insert_edge(8,11)
    g.insert_edge(8,13)
    g.insert_edge(10,15)
    g.insert_edge(11,10)   

    
    print('Adjacency List representation')
    g.display()
    g.draw()
    print()
    print('Breadth First Search ', end = '')
    printPathBFS(g.BFS())
    print('Depth First Search ', end = '')
    printPathDFS(g.DFS())
    print('------------------------------------------------------------')
    print()
    print('Adjacency Matrix representation')
    g2 = g.as_AM()
    g2.display()
    g2.draw()
    print()
    print('Breadth First Search ', end = '')
    printPathBFS(g2.BFS())
    print('Depth First Search ', end = '')
    printPathDFS(g2.DFS())
    print('------------------------------------------------------------')
    print()
    print('Edge List representation')
    g3 = g.as_EL()
    g3.display()
    g3.draw()
    print()
    print('Breadth First Search ', end = '')
    printPathBFS(g3.BFS())
    print('Depth First Search ', end = '')
    printPathDFS(g3.DFS())
    