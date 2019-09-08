''' 
    Cs2302 Data Structures
    Issac Rivas (80604101)
    Lab 1
    Dr.Fuentes
    Submited: Sep. 7th, 2019
    
'''
import time


#Takes a file name, creates a set of words from the given file, and returns the Set
def setFromFile():
    try:
        fileList = set(line.strip() for line in open(r'words_alpha.txt'))
        return fileList
    #Prints Error message if the file cannot be found
    except IOError:
        print("Error File Not Found")


############################################################################################################
############################################################################################################

#Part1

def partOne(fileSet):
    
    #Runs the program untill the user enters an empty string
    while True:
        word = input("Enter a word or empty string to finish: ").lower()
        
        #If an empty sting is entered the program prints a goodbye message and closes
        if word == '':
            print("Bye, Thanks for using this program!")
            break
        
        #If a word is not inputed then it will prompt the user that that there input
        #is invalid
        elif(not(word in fileSet)):
            print("Input invalid")
        else:
            
            #Sorts the inputted word alphabetically 
            sortedList = sorted(list(word))
            sortedWord = ''.join(sortedList)
            
            #Adds the word to the set of anagrams to start the set so the word 
            #is already in the list when we try and remove it
            anagramSet = {word}
            start = time.time()
            anagramFinder(sortedWord, '', word, fileSet, anagramSet)
            end = time.time()
            anagramSet.remove(word)
            
            
            anagramList = sorted(list(anagramSet))
            print("The word",  word, "has the following", len(anagramSet), "anagrams")
            for anagram in anagramList:
                print(anagram)
            print("It took", ((str(end - start))[:8]), "seconds to find the anagrams")
            print()

       
def anagramFinder(remainingL, scrambledL, word, fileSet, anagramSet):
    
    #Base Case if there are not letters remaining
    if len(remainingL) == 0:
        
        #Adds the word to a set then compares itself with fileSet to see if the
        #word is an anagram and if it is it is then added to the anagramSet
        tempPre = {scrambledL}
        tempSet = set.intersection(tempPre, fileSet)
        if len(tempSet) > 0:
            anagramSet.add(scrambledL)
    
    #Otherwise it beings making premutations of the inputted word and checks if
    #they are within the fileSet
    else:
        for i in range(len(remainingL)):
            scramble_letter = remainingL[i]
            remaining_letters = remainingL[:i] + remainingL[i + 1:]
            anagramFinder(remaining_letters, (scrambledL + scramble_letter), word, fileSet, anagramSet)



############################################################################################################
############################################################################################################

#Part2
            
def partTwo(fileSet):
    
    #Runs the program untill the user enters an empty string
    while True:
        word = input("Enter a word or empty string to finish: ")
        
        #If an empty sting is entered the program prints a goodbye message and closes
        if word == '':
            print("Bye, Thanks for using this program!")
            break
        
        #If a word is not inputed then it will prompt the user that that there input
        #is invalid
        elif(not(word in fileSet)):
            print("Input invalid")
        else:
            
            #Sorts the inputted word alphabetically
            sortedList = sorted(list(word))
            sortedWord = ''.join(sortedList)
            
            #Adds the word to the set of anagrams to start the set so the word 
            #is already in the list when we try and remove it
            anagramSet = {word}
            
            prefixSet = set()
            
            #Creats and Adds prefixes for all words in the fileSet
            #and adds them into the set prefixSet
            for setWord in fileSet:
                prefixSet.update(prefixes(setWord)) 
            
            start = time.time()
            anagramFinder_2(sortedWord, '', word, fileSet, anagramSet, prefixSet)
            end = time.time()
            
            #removes the original word from the anagramSet
            anagramSet.remove(word)
                
            #Converts anagramSet to a list, sorts them alphabetically, and 
            #then prints them alphabetically
            anagramList = sorted(list(anagramSet))
            print("The word",  word, "has the following", len(anagramSet), "anagrams")
            for anagram in anagramList:
                print(anagram)
            print("It took", ((str(end - start))[:8]), "seconds to find the anagrams")
            print()

       
def anagramFinder_2(remainingL, scrambledL, word, fileSet, anagramSet, prefixSet):
    
    #Base Case if there are not letters remaining
    if len(remainingL) == 0:
        
        #Adds the word to a set then compares itself with fileSet to see if the
        #word is an anagram and if it is it is then added to the anagramSet
        tempPre = {scrambledL}
        tempSet = set.intersection(tempPre, fileSet)
        if len(tempSet) > 0:
            anagramSet.add(scrambledL)
            
    #Otherwise it beings making premutations of the inputted word and checks if
    #they are within the fileSet
    else: 
        #First Optimization
        #Creates a new epmty set to hold letters already used
        duplicatedL = set()
        for i in range(len(remainingL)):
            scramble_letter = remainingL[i]
            remaining_letters = remainingL[:i] + remainingL[i + 1:]
            
            #Uses the set of prefixes to stop the recusrion if the partial word
            #is not found in the set
            if len(remainingL) > 1:
                if(not((scrambledL + scramble_letter) in prefixSet)):
                    continue
            
            #Checks the set duplicateL for duplicated Letters
            if scramble_letter in duplicatedL:
                continue
            
            #If letter has no been used yet and it is in the prefix set then it
            #is added to duplicatedL
            duplicatedL.add(scramble_letter)
            anagramFinder_2(remaining_letters, (scrambledL + scramble_letter), word, fileSet, anagramSet, prefixSet)


#Finds all prefixes of the word inputted
def prefixes(word):
    prefix = set()
    
    #Creates prfixes by adding x characters from the length of the word
    for x in range(1, len(word)):
        #Adds the list of prefixes into the empty set
        prefix.add(word[:x])
    return prefix
        

if __name__ == '__main__': 
    
    #Creates a set from the text file words_alpha.txt
    fileSet = set(line.strip() for line in open(r'C:\Users\Issac\Desktop\Cs 2302\Lab 1\words_alpha.txt'))
    
    print()
    print("--------------------------- Part One ---------------------------")
    partOne(fileSet)
    print()
    print("--------------------------- Part Two ---------------------------")
    print()
    partTwo(fileSet)
    