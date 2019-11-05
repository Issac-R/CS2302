'''
    Cs2302 Data Structures
    Issac Rivas
    Lab 4 
    Dr.Fuentues
'''
import Binary_Search_Tree as BSTree
import BTree
import HashTables_Chaining as HTC
import HashTables_LP as HTLP
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
    print("Enter the number '1' for a Binary Search Tree")
    print("'2' for a B-tree")
    print("'3' for a Hash Table with Linear Probing")
    print("'4' for a Hash Table with Chaining")
    ans = int(input("Input: "))
    while(ans != 1 and ans != 2 and ans != 3 and ans != 4):
        print()
        print("Incorrect input entered please Try again.")
        print("Type 1 for binary search or 2 for B-tree")
        ans = int(input("Input: "))
    
    filepath = 'C:/Users/Issac/Desktop/Lab_5/glove.6B.50d.txt'
    testpath = 'C:/Users/Issac/Desktop/Lab_5/test3.txt'
    
    #If user wants to create a BST
    if ans == 1:
        start = t.time()
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
    elif ans == 2:
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
        
    #If the user want to create a Hash Table with Linear Probing
    else:
        print("Choose Hash Function you would like to use:")
        print("Enter the number")
        print("'1' for The length of the string % n")
        print("'2' for The ascii value (ord(c)) of the first character in the string % n")
        print("'3' for The product of the ascii values of the first and last characters in the string % n")
        print("'4' for The sum of the ascii values of the characters in the string % n")
        print("'5' for The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n")
        print("'6' for The ascii value of each letter of the string times 2302 % n")
        ans2 = int(input("Input: "))
        while(ans2 != 1 and ans2 != 2 and ans2 != 3 and ans2 != 4 and ans2 != 5 and ans2 != 6):
            print()
            print("Enter the number")
            print("'1' for The length of the string % n")
            print("'2' for The ascii value (ord(c)) of the first character in the string % n")
            print("'3' for The product of the ascii values of the first and last characters in the string % n")
            print("'4' for The sum of the ascii values of the characters in the string % n")
            print("'5' for The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n")
            print("'6' for The ascii value of each letter of the string times 2302 % n")
            ans2 = int(input("Input: "))
        if ans == 3:
            start = t.time()
            count = 0
            with open(filepath,  encoding="utf8") as fp:
                for line in fp:
                    count += 1
            T = HTLP.HashTableLP(int(count+1), ans2)
            counter = 0
            with open(filepath,  encoding="utf8") as fp:
                for line in fp:
                    word, emb = lineSplit(line)
                    if word.isalpha():
                        temp = WordEmbedding(word, emb)
                        
                        #If the used buckests/Unused is grteater then 0.8 precent resize the bucket
                        if (counter / len(T.item)) >= 0.95:
                            T = HTLP.resize(T)
                        HTLP.insert(T, temp)
                        counter += 1
            Total = t.time() - start
            print()
            print("Building Hash Table with Linear Probing")
            print()
            print("Hash Table Stats:")
            print("Length of the Hash Table with Linear Probing: ", len(T.item))
            print("Number of items in the Hash Table with Linear Probing: ", counter)
            print("Running time for Hash Table with Linera Probing construction:", round(Total, 4), " seconds")
            print()
            print("Reading word file to determine similarities")
            print()
            print("Word similarities found:")
            start = t.time()
            with open(testpath) as tp:
                for line in tp:
                    words = line.split()
                    W1 = WordEmbedding(words[0], [])
                    W2 = WordEmbedding(words[1], [])
                    temp0 = HTLP.find(T, W1)
                    temp1 = HTLP.find(T, W2)
                    sim = Similarity(T.item[temp0], T.item[temp1])
                    print("Similarity [" + words[0] + "," + words[1] + "] = ", round(sim, 4)) 
            Total = t.time() - start
            print()
            print("Running time for Hash Table with Linear Probing query processing: ", round(Total, 7))
            
        #If the user want to create a Hash Table with Chaining
        elif ans == 4:
            start = t.time()
            count = 0
            with open(filepath,  encoding="utf8") as fp:
                for line in fp:
                    count += 1
            T = HTC.HashTableChain(int(count/20), ans2)
            counter = 0
            with open(filepath,  encoding="utf8") as fp:
                for line in fp:
                    word, emb = lineSplit(line)
                    if word.isalpha():
                        temp = WordEmbedding(word, emb)
                        HTC.insert(T, temp)
                        counter += 1
            Total = t.time() - start
            print()
            print("Building Hash Table with Chaining")
            print()
            print("Hash Table Stats:")
            print("Length of the Hash Table with Chaining: ", len(T.bucket))
            print("Number of items in the Hash Table with Chaining: ", counter)
            print("Running time for Hash Table with Chaining construction:", round(Total, 4), " seconds")
            print()
            print("Reading word file to determine similarities")
            print()
            print("Word similarities found:")
            start = t.time()
            with open(testpath) as tp:
                for line in tp:
                    words = line.split()
                    W1 = WordEmbedding(words[0], [])
                    W2 = WordEmbedding(words[1], [])
                    temp0, ind0 = HTC.find(T, W1)
                    temp1, ind1 = HTC.find(T, W2)
                    sim = Similarity(T.bucket[temp0][ind0], T.bucket[temp1][ind1])
                    print("Similarity [" + words[0] + "," + words[1] + "] = ", round(sim, 4)) 
            Total = t.time() - start
            print()
            print("Running time for Hash Table with Chaining query processing: ", round(Total, 7))
