import os
import random

file_in = open("d_quite_big.in",'r')
line = file_in.readline()
maxSlices,nbTypes = [int(i) for i in line.split()]
line = file_in.readline()
slices = [int(i) for i in line.split()]
types = [i for i in range(nbTypes)]

greedyMax = 0
greedyIndices = list()

#greedy algo
for i in range(10000):
    random.shuffle(types)
    indices = list()
    maxfound = 0
    j = nbTypes - 1
    while(j > 0):
        if(slices[types[j]] + maxfound <= maxSlices):
            maxfound = slices[types[j]] + maxfound
            indices.append(types[j])
        if(slices[types[j]] + maxfound == maxSlices):
            j = 0
        j = j - 1
    if(maxfound > greedyMax):
        greedyMax = maxfound
        greedyIndices = list(indices)

print("Maximul slices found ") 
print(greedyMax)


