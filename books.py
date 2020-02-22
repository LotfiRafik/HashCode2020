import operator
import sys
class Library():
    def __init__(self, nbBooks, signupDays, bookPerDay,listBooks):
        self.nbBooks = nbBooks
        self.signupDays = signupDays
        self.bookPerDay = bookPerDay
        self.listBooks = listBooks

file_in = open("b_read_on.txt",'r')
file_out = open("b_read_on.out",'w')
file_out.write("     " + "\n")

line1 = file_in.readline().split()
line1 = [int(i) for i in line1]
scoreBooks = file_in.readline().split()
scoreBooks = [int(i) for i in scoreBooks]
libraries = {}
for i in range(line1[1]):
    l = file_in.readline().split()
    listBooks = file_in.readline().split()
    listBooks = [int(i) for i in listBooks]
    libraries[i]= Library(int(l[0]),int(l[1]),int(l[2]),listBooks)
    
#init list books to save if book is scanned or not (0 OR 1) 
scannedBooks = [0] * line1[0]



scoreTotal = 0
stop = False
while(not(stop)):
    maxScore = 0.0
    booksToScan = list()
    #for each library count the score
    for id,library  in libraries.items():
        scoreOfThisLibrary = 0
        daysLeft = line1[2] - library.signupDays
        if(daysLeft > 0):
            nbBooksCanBeScanned = daysLeft * library.bookPerDay
            tempBooks = list()
            if(nbBooksCanBeScanned >= library.nbBooks):
             #scan all books that arent scanned yet
                for i in library.listBooks:
                    if(scannedBooks[i] != 1):   #if not scanned yet
                        scoreOfThisLibrary +=  scoreBooks[i] / library.signupDays
                        tempBooks.append(i)
            else:
                #choose nbBooksCanBeScanned best books(score) to scan that arent scanned yet
                temp = {}
                for i in library.listBooks:
                    temp[i] =  scoreBooks[i]
                i = 0
                j = 0
                while(i < nbBooksCanBeScanned and j < len(library.listBooks)):
                    k = max(temp.items(), key=operator.itemgetter(1))[0]
                    if(scannedBooks[k] != 1):   #if not scanned yet
                        scoreOfThisLibrary +=  scoreBooks[k] / library.signupDays
                        tempBooks.append(k)
                        i += 1
                    temp.pop(k)
                    j += 1
            #score , books taken , id
            if(scoreOfThisLibrary > maxScore):
                maxScore = scoreOfThisLibrary
                idLibrary = id
                booksToScan = list(tempBooks)
    if(maxScore == 0):  stop = True #Either all books are scanned or daysLeft <= 0 or we scanned all libraries
    else:
        scoreTotal += maxScore * libraries[idLibrary].signupDays
        print(int(scoreTotal))
        file_out.write(str(idLibrary)+" "+str(len(booksToScan))+"\n")
        for k in range(len(booksToScan)):
            file_out.write(str(booksToScan[k])+" ")
        file_out.write("\n")
        line1[2] = line1[2] - libraries[idLibrary].signupDays
        for i in booksToScan:
            scannedBooks[i] = 1
        libraries.pop(idLibrary)
        

    
file_out.seek(0, 0)
file_out.write(str(line1[1] - len(libraries)))