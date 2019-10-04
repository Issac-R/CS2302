'''

    Cs2302 Data Structures
    Issac Rivas
    Lab 3 
    Dr.Fuentues

'''
import math

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SortedList(object):
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def Append(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            H = self.head
            temp = Node(x)
            if temp.data < H.data:
                temp.next = H
                self.head = temp
            elif temp.data > H.data:
                self.tail.next = temp
                self.tail = temp
            else:
                while temp.data > H.next.data and H.next is not None:
                    H = H.next
                if temp.data > H.data and H.next is None:
                    H.next = temp
                    self.tail = temp
                else:
                    temp.next = H.next
                    H.next = temp

    def AppendList(self, python_list):
        for d in python_list:
            self.Append(d)

    def Print(self):
        t = self.head
        if t is None:
            print("List is Empty.")
        else:
            while t is not None:
                print(t.data, end = ' ')
                t = t.next
            print()
    
    def Insert(self, i):
        H = self.head
        temp = Node(i)
        if H is None:
            self.head = temp
            self.tail = temp
        else:
            if temp.data < H.data:
                temp.next = H
                self.head = temp
            else:
                while temp.data > H.data and H.next is not None:
                    H = H.next
                if temp.data > H.data and H.next is None:
                    H.next = temp
                    tail = temp
                else:
                    temp.next = H.next
                    H.next = temp

    def Delete(self, i):
        if self.head is None:
            return
        elif i == 0:
            temp = self.head.next
            self.head = temp
        else:
            H = self.head
            count = 1
            while H.next is not None and count < i:
                H = H.next
                count += 1
            if H.next is None:
                return 
            temp = H.next.next
            H.next = temp
    

    def Merge(self, M):
        if M.head is None:
            return
        elif self.head is None:
            self.head = M.head
            self.tail = M.tail
        else:
            L2 = M.head
            while L2 is not None:
                temp = L2.data
                self.Insert(temp)
                L2 = L2.next

    def IndexOf(self, i):
        if i == 0:
            return self.head.data
        else:
            H = self.head
            counter = 0
            while H is not None and counter != i:
                H = H.next
                counter += 1
            if H is None:
                return -1
            return H.data

    def Clear(self):
        self.head.next = None
        self.head = None
        self.tail = None

    def Min(self):
        if self.head is None:
            return math.inf
        return self.head.data

    def Max(self):
        if self.head is None:
            return math.inf
        return self.tail.data

    def HasDuplicates(self):
        if self.head is None:
            return False
        H = self.head
        Storage = [H.data]
        H = H.next
        while H is not None:
            for x in range(len(Storage)):
                if Storage[x] == H.data:
                    return True
            Storage = Storage + [H.data]
            H = H.next
        return False

    def Select(self, k):
        if k < 0:
            return -math.inf
        elif k == 0:
            return self.head.data
        H = self.head
        while H is not None and k >= 0:
            H = H.next
        if H is None:
            return math.inf
        return H.data
                 
if __name__ == "__main__":
    print("Unsorted List: ",end = '')
    print("9 8 7 6 5 4 3 2 1")
    print()

    #Create Sorted Linked List
    print("Sorted Linked List: ",end = '')
    L1 = SortedList()
    L1.AppendList([9,8,7,6,5,4,3,2,1])
    L1.Print()
    print()

    #Print
    print("Print: ",end = '')
    L1.Print()
    print()

    #Insert
    print("Insert(0): ",end = '')
    L1.Insert(0)
    L1.Print()
    print()

    #Delete
    print("Delete(0): ",end = '')
    L1.Delete(0)
    L1.Print()
    print()

    #Merge
    print("Merge([19,18,17,16,15,14,13,12,11,10]): ")
    L2 = SortedList()
    L3 = SortedList()
    L2.AppendList([9,8,7,6,5,4,3,2,1])
    L3.AppendList([19,18,17,16,15,14,13,12,11,10])
    L2.Merge(L3)
    L2.Print()
    print()

    #Index of
    print("Index of(0): ",end = '')
    print(L1.IndexOf(0))
    print()

    #Clear 
    print("Clear: ",end = '')
    L1.Clear()
    L1.Print()
    print()

    #Min
    print("New List: 0 1 2 3 4 5 6 7 8 9")
    print("Min: ",end = '')
    L1.AppendList([9,8,7,6,5,4,3,2,1,0])
    print(L1.Min())
    print()

    #Max
    print("Max: ",end = '')
    print(L1.Max())
    print()

    #Has Duplicates
    print("Has Duplicates: ",end = '')
    print(L1.HasDuplicates())
    print()

    #Select
    print("Select: ",end = '')
    print(L1.Select(0))
    print()