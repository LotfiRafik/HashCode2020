import os
file_in = open("d_quite_big.in",'r')
line = file_in.readline()
maxSlices,nbTypes = [int(i) for i in line.split()]
line = file_in.readline()
slices = [int(i) for i in line.split()]
#somme all
#generete combinisions
indices = list()
maxfound = 0
i = 0
while(nbTypes > 0):
    if(slices[nbTypes - 1] + maxfound == maxSlices):
        maxfound = slices[nbTypes - 1] + maxfound
        indices.append(Types - 1)
        i = i + 1
        nbTypes = 0
    elif(slices[nbTypes - 1] + maxfound < maxSlices):
        maxfound = slices[nbTypes - 1] + maxfound
        indices.append(nbTypes - 1)
        i = i + 1
    nbTypes = nbTypes - 1

#the combinisions found is in maxsumslices
print("Maximul slices found ") 
print(maxfound)
print("Number of types to order :") 
print(i)

file_out = open("d_quite_big.out",'w')
file_out.write(str(i)+"\n")
for i in reversed(indices):
        file_out.write(str(i)+" ")

