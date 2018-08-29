import os

nlist = os.listdir('.')
mlist = list()
for a in nlist:
    if a[0:6] == "output":
        mlist.append(a)

for z in range(99, -1, -1):
    print z
    inputname = "output" + str(z) + ".xml"
    newz = z + 27
    outputname = "output" + str(newz) + ".xml"
    print inputname
    os.rename(inputname, outputname)