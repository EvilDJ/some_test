path = r'G:\DATA\FDDB\folds.txt'
pa = r'G:\DATA\FDDB\new_folds.txt'
nf = open(path,'w')
j = 0
d = 0
with open(pa,'r') as f:
    for i in f:
        if '.' in i:
            j += 1
            print(i)
        else:
            d += 1
            nf.write(i)
nf.closed
print(j,d)