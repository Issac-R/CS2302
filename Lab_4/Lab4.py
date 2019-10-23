'''

    Cs2302 Data Structures
    Issac Rivas
    Lab 4 
    Dr.Fuentues

'''
import BSTree
import BTree
import numpy as np
import time as t

#Creates an object that holds the word as well as 50 element embedding list
class WordEmbedding(object):
    def __init__(self, word, embedding):
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32)

#Splis a text file line into a word and a float list of the remainig 50 elements
def lineSplit(line):
    emb = line.split()
    word = emb[0]
    del emb[0]
    for x in range(0, len(emb)):
        emb[x] = float(emb[x])
    return word, emb

#Calculates for the Similartiy of two words
def Similarity(word0, word1):
    dotProduct = np.dot(word0.emb,word1.emb)
    magnitude = np.linalg.norm(word0.emb) * np.linalg.norm(word1.emb)
    return dotProduct/magnitude
    
if __name__ == "__main__":
    print("Choose table implementation:")
    print("Enter '1' for binary search or '2' for B-tree")
    ans = int(input("Input: "))
    while(ans != 1 and ans != 2):
        print()
        print("Incorrect input entered please Try again.")
        print("Type 1 for binary search or 2 for B-tree")
        ans = int(input("Input: "))
    
    filepath = 'C:/Users/Issac/Desktop/Lab_4/glove.6B.50d.txt'
    testpath = 'C:/Users/Issac/Desktop/Lab_4/test.txt'
    start = t.time()
    
    #If user wants to create a BST
    if(ans == 1):
        T = None
        with open(filepath,  encoding="utf8") as fp:
            for line in fp:
                word, emb = lineSplit(line)
                if word.isalpha():
                    temp = WordEmbedding(word, emb)
                    T = BSTree.Insert(T, temp)
        Total = t.time() - start
        print()
        print("Building Binary Search Tree")
        print()
        print("Binary Tree Stats:")
        print("Number of Nodes: ", BSTree.numOfNodes(T))
        print("Tree Height is: ", BSTree.treeHeight(T))
        print("Running time for Binary Search Tree construction:", round(Total, 4), " seconds")
        print()
        print("Reading word file to determine similarities")
        print()
        print("Word similarities found:")
        start = t.time()
        with open(testpath) as tp:
            for line in tp:
                words = line.split()
                temp0 = BSTree.Search(T, words[0])
                temp1 = BSTree.Search(T, words[1])
                sim = Similarity(temp0.data, temp1.data)
                print("Similarity [" + words[0] + "," + words[1] + "] = ", round(sim, 4)) 
        Total = t.time() - start
        print()
        print("Running time for Binary Search Tree query processing: ", round(Total, 7))
        
    #If user wants to create a B-tree
    else:
        max_data = int(input("Please enter the maximum number of items per node: "))
        while (max_data < 1):
            print("Error please insert a number equal to or greater then 1.")
            max_data = int(input("Please enter the maximum number of items per node: "))
        start = t.time()
        T = BTree.BTree([], max_data)
        with open(filepath,  encoding="utf8") as fp:
            for line in fp:
                word, emb = lineSplit(line)
                if word.isalpha():
                    temp = WordEmbedding(word, emb)
                    BTree.Insert(T, temp) 
        print()
        print("Building B-Tree")
        print()
        print("B-Tree Stats:")
        print("Number of Nodes: ", BTree.NumItems(T))
        print("Tree Height is: ", BTree.Height(T))
        Total = t.time() - start
        print("Running time for B-tree construction (with max_items = " + str(max_data) + "):", round(Total, 4), "seconds")
        print()
        print("Reading word file to determine similarities")
        print()
        print("Word similarities found:")
        start = t.time()
        with open(testpath) as tp:
            for line in tp:
                words = line.split()
                wordemb1 = WordEmbedding(words[0], [])
                wordemb2 = WordEmbedding(words[1], [])
                temp0 = BTree.Search(T, wordemb1)
                temp1 = BTree.Search(T, wordemb2)
                sim = Similarity(temp0, temp1)
                print("Similarity [" + words[0] + "," + words[1] + "] = ", round(sim, 4)) 
        Total = t.time() - start
        print()
        print("Running time for B-Tree query processing (with max_items = " + str(max_data) + "):", round(Total, 7), "seconds")



    