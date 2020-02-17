import os
def combinations(iterable, r,maxSlices):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    max = 0
    if r > n:
        return
    indices = list(range(r))  
    types = list()
    sumslices = sum(pool[i] for i in indices)
    if max < sumslices < maxSlices:
        max = sumslices
        types = list(indices)
    while True:
        for i in reversed(range(r)):   
            if indices[i] != i + n - r:
                break
        else:
            return types,max
        indices[i] += 1 
        for j in range(i+1, r):  
            indices[j] = indices[j-1] + 1 
        sumslices = sum(pool[i] for i in indices)
        if max < sumslices < maxSlices:
            max = sumslices
            types = list(indices)

file_in = open("d_quite_big.in",'r')
line = file_in.readline()
maxSlices,nbTypes = [int(i) for i in line.split()]
line = file_in.readline()
slices = [int(i) for i in line.split()]
#somme all
#generete combinisions
found = False
while(nbTypes > 0 and found == False):
    maxsumSlices = combinations(slices,nbTypes,maxSlices)
    if(maxsumSlices[1] > 0): found = True
    nbTypes = nbTypes - 1

#the combinisions found is in maxsumslices
print(maxsumSlices)

file_out = open("d_quite_big.out",'w')
file_out.write(str(nbTypes + 1)+"\n")
for k in maxsumSlices[0]:
        file_out.write(str(k)+" ")



