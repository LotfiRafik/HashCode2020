import operator
import sys
import time
class Library():
    def __init__(self, nbBooks, signupDays, bookPerDay,listBooks):
        self.nbBooks = nbBooks
        self.signupDays = signupDays
        self.bookPerDay = bookPerDay
        self.listBooks = listBooks

files = ["a_example","b_read_on","e_so_many_books","f_libraries_of_the_world"]
#files = ["d_tough_choices"]
finalScore = 0
timm = time.time()
for f in files:
        file_in = open(str(f) + ".txt",'r')
        file_out = open(str(f) + ".out",'w')
        file_out.write("     " + "\n")

        line1 = file_in.readline().split()
        line1 = [int(i) for i in line1]
        scoreBooks = file_in.readline().split()
        scoreBooks = [int(i) for i in scoreBooks]
        libraries = {}
        librariesNbBook = {}
        for i in range(line1[1]):
            l = file_in.readline().split()
            listBooks = file_in.readline().split()
            if(f == "d_tough_choices" or f == "b_read_on"):   #No need to sort books based on their scores because in D and B all books have same score
                listBooks = [int(i) for i in listBooks]
            else:
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
        maxScore = 0.0
        booksToScan = list()
        scoreTotal = 0
        lib = 0
        while(lib < line1[1] and line1[2] > 0 and sum(scannedBooks) != line1[0]):
            maxScore = 0.0
            booksToScan = list()
            #for each library count the score
            for id,library  in libraries.items():
                scoreOfThisLibrary = 0
                daysLeft = line1[2] - library.signupDays
                if(daysLeft > 0):
                    nbBooksCanBeScanned = daysLeft * library.bookPerDay
                    tempBooks = list()
                    #scan the maximum books that arent scanned 
                    i = 0
                    j = 0
                    while(j < nbBooksCanBeScanned and i < library.nbBooks):
                        bookId = library.listBooks[i]
                        if(scannedBooks[bookId] != 1):   #if not scanned yet
                            scoreOfThisLibrary +=  scoreBooks[bookId]
                            tempBooks.append(bookId)
                            j += 1
                        i += 1
                    scoreOfThisLibrary = scoreOfThisLibrary / library.signupDays 
                    #score , books taken , id
                    if(scoreOfThisLibrary > maxScore):
                        maxScore = scoreOfThisLibrary
                        idLibrary = id
                        booksToScan = list(tempBooks)
            if(maxScore != 0):
                scoreTotal += maxScore * libraries[idLibrary].signupDays
                file_out.write(str(idLibrary)+" "+str(len(booksToScan))+"\n")
                for k in range(len(booksToScan)):
                    file_out.write(str(booksToScan[k])+" ")
                file_out.write("\n")
                line1[2] = line1[2] - libraries[idLibrary].signupDays
                for i in booksToScan:
                    scannedBooks[i] = 1
                libraries.pop(idLibrary)
            lib += 1


        file_out.seek(0, 0)
        file_out.write(str(line1[1] - len(libraries)))  
        print("SCORE " + str(f) + " : " + str(int(scoreTotal)))
        finalScore += int(scoreTotal)


print("FINAL SCORE: " + str(finalScore))
print(str(((time.time()-timm) / 60)) + "Mn")
