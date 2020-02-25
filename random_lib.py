import operator
import sys
import random
import time


class Library():
    def __init__(self, nbBooks, signupDays, bookPerDay,listBooks):
        self.nbBooks = nbBooks
        self.signupDays = signupDays
        self.bookPerDay = bookPerDay
        self.listBooks = listBooks

file_in = open("e_so_many_books.txt",'r')
file_out = open("e_so_many_books.out",'w')

line1 = file_in.readline().split()
line1 = [int(i) for i in line1]
scoreBooks = file_in.readline().split()
scoreBooks = [int(i) for i in scoreBooks]
libraries = {}
for i in range(line1[1]):
    l = file_in.readline().split()
    listBooks = file_in.readline().split()
    temp = {}
    for j in listBooks:
        temp[int(j)] =  scoreBooks[int(j)]
    listBooks = list()
    for j in range(int(l[0])):
        k = max(temp.items(), key=operator.itemgetter(1))[0]
        listBooks.append(k)
        temp.pop(k)
    libraries[i]= Library(int(l[0]),int(l[1]),int(l[2]),listBooks)






#init list books to save if book is scanned or not (0 OR 1) 
scannedBooks = [0] * line1[0]
idLibraries = []

for id,library  in libraries.items():
    idLibraries.append(id)

MAXE = 5034898
maxScore = 0
for i in range(1000):
    #timm = time.time()
    random.shuffle(idLibraries)
    #print(time.time()-timm)
    scannedBooks = [0] * line1[0]
    scoreTotal = 0
    lib = 0
    idLibraryOutput = []
    booksToScanOutput = []

    daysLeft = line1[2]
        #Count the score of all libraries randomly ( shuffled array )
    while(daysLeft > 0 and lib < line1[1] and sum(scannedBooks) != line1[0]):
            id = idLibraries[lib]
            scoreOfThisLibrary = 0
            daysToScanBooks = daysLeft - libraries[id].signupDays
            if(daysToScanBooks > 0):
                nbBooksCanBeScanned = daysToScanBooks * libraries[id].bookPerDay
                booksToScan = list()
                #scan the maximum books that arent scanned 
                k = 0
                j = 0
                while(j < nbBooksCanBeScanned and k < libraries[id].nbBooks):
                    bookId = libraries[id].listBooks[k]
                    if(scannedBooks[bookId] != 1):   #if not scanned yet
                        scoreOfThisLibrary +=  scoreBooks[bookId]
                        booksToScan.append(bookId)
                        j += 1
                    k += 1
            if(scoreOfThisLibrary != 0):
                scoreTotal += scoreOfThisLibrary
                daysLeft = daysLeft - libraries[id].signupDays
                for k in booksToScan:
                    scannedBooks[k] = 1
            idLibraryOutput.append(id)
            booksToScanOutput.append(booksToScan)
            lib += 1

    print("Random " + str(i) + " Score Total  :" + str(int(scoreTotal)))        
    if(scoreTotal > maxScore):
        maxScore = scoreTotal
        #if(maxScore > MAXE):
        #    MAXE = maxScore
        #    print("MAX MAX FOUND " + str(maxScore))
        #    file_out.seek(0, 0)
        #    file_out.write(str(lib - 1))
        #    for i in range(len(idLibraryOutput)):
        #        file_out.write(str(idLibraryOutput[i])+" "+str(len(booksToScanOutput[i]))+"\n")
        #        for k in range(len(booksToScanOutput[i])):
        #            file_out.write(str(booksToScanOutput[i][k])+" ")
        #        file_out.write("\n")
    

print("MAXIMUM SCORE FOUND :" + str(int(maxScore)))        

