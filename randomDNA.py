import sys
import random
from string import maketrans

class randomDNA:

    def openFile(self, filename):
        with open(filename) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for a in content:
            if a == '':
                content.remove(a)
        return content

    def generateSeqs(self, numseq, size):
        seqList = list()
        intab = "1234"
        outtab = "ACGT"
        numA = numC = numG = numT = 0
        trantab = maketrans(intab, outtab)
        for i in range(0, numseq):
            seq = ""
            for u in range(0, size):
                ran = random.randint(1,4)
                seq += str(ran)
                if ran == 1:
                    numA += 1
                elif ran == 2:
                    numC += 1
                elif ran == 3:
                    numG += 1
                else:
                    numT += 1
            seq = seq.translate(trantab)
            seqList.append(seq)

        for a in seqList:
            print a
        print "Frequencies: A:", numA, "C:", numC, "G:", numG, "T:", numT
        return seqList


g = randomDNA()
args = list(sys.argv)
if len(args) != 3:
    print "python randomDNA.py <number of seq> <size of seq>"
else:
    numseq = int(args[1])
    size = int(args[2])

    g.generateSeqs(numseq,size)

