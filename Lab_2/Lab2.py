''' 
    Cs2302 Data Structures
    Issac Rivas (80604101)
    Lab 2
    Dr.Fuentes
    
'''
#Part 1
#1.Bubble Sort
#------------------------------------------------------------------------------
def select_bubble(L,k):
    bubbleSort(L)
    print("Sorted List:", L)
    
    #If list is Empty
    if L is None:
        print("There are no elemnts in the list.")
        return -999
    
    #If k is a negative value
    elif k < 0:
        print("There is no element in position", str(k)+".")
        print("The element in position", str(len(L)-1)+" is,", str(L[len(L)-1])+".")
        return L[0]
    
    #If k is greater then the length of the list
    elif len(L)-1 < k:
        print("There is no element in position", str(k)+".")
        print("The last element of the list is in position", str(len(L)-1)+" and is,", str(L[len(L)-1])+".")
        return L[len(L)-1]
    
    #If k is within the length of the list
    else:
        print("The element at position", str(k)+" is,", str(L[k])+".")
        
    return L[k]

        
def bubbleSort(L):
    #If the list is empty there is no need to sort
    if L is None:
        return L
    
    #If the List is of length 1 there is no need to sort
    elif len(L) == 1:
        return L
    
    #Sorts through the length of the list placing the largest value at the end
    else:
        for x in range(len(L)):
            for y in range(0, (len(L)-x)-1):
                if L[y] > L[y+1]:
                    temp = L[y]
                    L[y] = L[y+1]
                    L[y+1] = temp
    return L



#2.Quicksort
#------------------------------------------------------------------------------
def select_quick(L,k):
    quicksort(L, 0, (len(L)-1))
    print("Sorted List:", L)
    
    #If List is empty
    if L is None:
        print("There are no elemnts in the list.")
        return -999
    
    #If k is a negative value
    elif k < 0:
        print("There is no element in position", str(k)+".")
        print("The element in position", str(len(L)-1)+" is,", str(L[len(L)-1])+".")
        return L[0]
    
    #If k is greater then the length of the list
    elif len(L)-1 < k:
        print("There is no element in position", str(k)+".")
        print("The last element of the list is in position", str(len(L)-1)+" and is,", str(L[len(L)-1])+".")
        return L[len(L)-1]
    
    #If k is within the length of the list
    else:
        print("The element at position", str(k)+" is,", str(L[k])+".")
        
    return L[k]


def quicksort(L, lPos, rPos):
    
    #If the left position is greater or equal to the right there is no need to sort
    if lPos >= rPos:
        return
    
    #Gets the mid point of the array which is where the pivot swaps to
    mPos = partitionQS(L, lPos, rPos)
    
    #Sorts the two opposite sides of the pivot
    quicksort(L, lPos, mPos-1)
    quicksort(L, mPos+1, rPos)


def partitionQS(L, lPos, rPos):
    pivot = L[lPos]
    leftPos = lPos + 1
    x =  leftPos
    y = rPos
    loop = True
    
    #While true it will swap values that are above and below the pivot untill
    #leftPos is > y or untill x is < rPos
    while loop:
        while L[leftPos] <= pivot and leftPos < y:
            leftPos += 1
        while pivot < L[rPos] and x < rPos:
            rPos -= 1
        if rPos <= leftPos:
            loop = False
        else:
            temp = L[leftPos]
            L[leftPos] = L[rPos]
            L[rPos] = temp
            
    #Swaps the pivot at the leftmost point with the position of the rPos
    temp = L[lPos]
    L[lPos] = L[rPos]
    L[rPos] = temp
    return rPos



#3.Modifed Quicksort
#------------------------------------------------------------------------------
def select_modified_quick(L,k):
    modifiedQS(L, 0, (len(L)-1), k)
    print("Sorted List:", L)
    
    #If list is empty
    if L is None:
        print("There are no elemnts in the list.")
        return -999
    
    #If k is a negative value
    elif k < 0:
        print("There is no element in position", str(k)+".")
        print("The element in position", str(0)+" is,", str(0)+".")
        return L[0]
    
    #If k is greater then the length of the list
    elif len(L)-1 < k:
        print("There is no element in position", str(k)+".")
        print("The last element of the list is in position", str(len(L)-1)+" and is,", str(L[len(L)-1])+".")
        return L[len(L)-1]
    
    #If k is within the length of the list
    else:
        print("The element at position", str(k)+" is,", str(L[k])+".")
        
    return L[k]


def modifiedQS(L, lPos, rPos, k):
    
    #If the left position is greater or equal to the right there is no need to sort
    if lPos >= rPos:
        return
    
    #Gets the mid point of the array which is where the pivot swaps to
    mPos = partitionMQS(L, lPos, rPos, k)
    
    #If the position looking for is the mPos then no need to sort more
    if k == mPos:
        return mPos
    
    #If position k is less then the midpoint then you just need to sort the left side
    elif k < mPos:
        modifiedQS(L, lPos, mPos-1, k)
        
    #If position k is greater then the midpoint then you just need to sort the right side
    else:
        modifiedQS(L, mPos+1, rPos, k)


def partitionMQS(L, lPos, rPos, k):
    pivot = L[lPos]
    leftPos = lPos + 1
    x =  leftPos
    y = rPos
    loop = True
    
    #While true it will swap values that are above and below the pivot untill
    #leftPos is > y or untill x is < rPos
    while loop:
        while L[leftPos] <= pivot and leftPos < y:
            leftPos += 1
        while pivot < L[rPos] and x < rPos:
            rPos -= 1
        if rPos <= leftPos:
            loop = False
        else:
            temp = L[leftPos]
            L[leftPos] = L[rPos]
            L[rPos] = temp
        
    #Swaps the pivot at the leftmost point with the position of the rPos
    temp = L[lPos]
    L[lPos] = L[rPos]
    L[rPos] = temp
    return rPos



#Part 2
#1. Quicksort with Stacks
#------------------------------------------------------------------------------
def stackQS(L, k):
    stackQuicksort_nr(L, 0, (len(L)-1))
    print("Sorted List:", L)
    
    #If List is empty
    if L is None:
        print("There are no elemnts in the list.")
        return -999
    
    #If k is a negative value
    elif k < 0:
        print("There is no element in position", str(k)+".")
        print("The element in position", str(len(L)-1)+" is,", str(L[len(L)-1])+".")
        return L[0]
    
    #If k is greater then the length of the list
    elif len(L)-1 < k:
        print("There is no element in position", str(k)+".")
        print("The last element of the list is in position", str(len(L)-1)+" and is,", str(L[len(L)-1])+".")
        return L[len(L)-1]
    
    #If k is within the length of the list
    else:
        print("The element at position", str(k)+" is,", str(L[k])+".")
        
    return L[k]


class classSQS(object):
    # Constructor
    def __init__(self, L, lPos, rPos):  
        self.L = L
        self.lPos = lPos
        self.rPos = rPos
    
    
#Creates a stack that keeps adding on untill the list is sorted
def stackQuicksort_nr(L, lPos, rPos):
    
    #Creates a stack and adds first left and right position
    stack = [classSQS(L, lPos, rPos)]
    
    #Runs untill the stack is empty
    while len(stack)>0:
        temp = stack.pop(-1)
        if temp.lPos < temp.rPos:
            #Gets the mPos of the list
            h = partitionSQS(temp.L, temp.lPos, temp.rPos)
            
            #Adds the left and right of the list to the stack
            stack.append(classSQS(temp.L, temp.lPos, h - 1))
            stack.append(classSQS(temp.L, h + 1, temp.rPos))    


def partitionSQS(L, lPos, rPos):
    pivot = L[lPos]
    leftPos = lPos + 1
    x =  leftPos
    y = rPos
    loop = True
    
    #While true it will swap values that are above and below the pivot untill
    #leftPos is > y or untill x is < rPos
    while loop:
        while L[leftPos] <= pivot and leftPos < y:
            leftPos += 1
        while pivot < L[rPos] and x < rPos:
            rPos -= 1
        if rPos <= leftPos:
            loop = False
        else:
            temp = L[leftPos]
            L[leftPos] = L[rPos]
            L[rPos] = temp
            
    #Swaps the pivot at the leftmost point with the position of the rPos
    temp = L[lPos]
    L[lPos] = L[rPos]
    L[rPos] = temp
    return rPos 



#2.Modified Quicksort with while loop
#------------------------------------------------------------------------------
def while_modified_quick(L,k):
    modifiedWQS(L, 0, (len(L)-1), k)
    print("Sorted List:", L)
    
    #If list is empty
    if L is None:
        print("There are no elemnts in the list.")
        return -999
    
    #If k is a negative value
    elif k < 0:
        print("There is no element in position", str(k)+".")
        print("The element in position", str(0)+" is,", str(0)+".")
        return L[0]
    
    #If k is greater then the length of the list
    elif len(L)-1 < k:
        print("There is no element in position", str(k)+".")
        print("The last element of the list is in position", str(len(L)-1)+" and is,", str(L[len(L)-1])+".")
        return L[len(L)-1]
    
    #If k is within the length of the list
    else:
        print("The element at position", str(k)+" is,", str(L[k])+".")
        
    return L[k]


def modifiedWQS(L, lPos, rPos, k):
    pivot = L[lPos]
    loop = True
    loop2 = True
    
    #While mPos dose not equal k
    while loop:
        leftPos = lPos + 1
        x = leftPos
        y = rPos
        
        #Sets the new mPos
        while loop2:
            while L[leftPos] <= pivot and leftPos < y:
                leftPos += 1
            while pivot < L[rPos] and x < rPos:
                rPos -= 1
            if rPos <= leftPos:
                loop2 = False
            else:
                temp = L[leftPos]
                L[leftPos] = L[rPos]
                L[rPos] = temp
            
        #Swaps the pivot and the mPos
        temp = L[lPos]
        L[lPos] = L[rPos]
        L[rPos] = temp
        mPos = rPos
        
        #If mPos equals k then no need to sort more
        if mPos == k:
            loop = False
            
        #If mPos is less then k you only have to sort the right side
        elif mPos < k:
            pivot = L[mPos + 1]
            lPos = mPos + 1
            rPos = y
            loop2 = True
            
        #If mPos is more then k you only need to sort the left side
        elif mPos > k:
            pivot = L[0]
            rPos = mPos - 1
            loop2 = True
            
    return L[k]
        


###############################################################################
#Main
#------------------------------------------------------------------------------
if __name__ == '__main__': 
    
    L1 = list([9,3,6,7,2,1,4,8,0,5])
    L2 = list([9,3,6,7,2,1,4,8,0,5])
    L3 = list([9,3,6,7,2,1,4,8,0,5])
    L4 = list([9,3,6,7,2,1,4,8,0,5])
    L5 = list([9,3,6,7,2,1,4,8,0,5])
    print("Unsorted list:", L1)
    print()
    
    
    print("----------------------------- Part 1 ------------------------------")
    print()
    print()
    print("--------------------------- Bubble Sort ---------------------------")
    print()
    select_bubble(L1,0)
    print()
    print("--------------------------- Quick Sort ----------------------------")
    print()
    select_quick(L2,0)
    print()
    print("----------------------- Modified Quick Sort -----------------------")
    print()
    select_modified_quick(L3,7)
    print()
    print()
    print()
    
    
    print("----------------------------- Part 2 ------------------------------")
    print()
    print()
    print("------------------------ Stack Quick Sort -------------------------")
    print()
    stackQS(L4,0)
    print()
    print("---------------------- While Loop Quick Sort ----------------------")
    print()
    while_modified_quick(L5,7)
    print()