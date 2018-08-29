class Intro:
    def helloBioinformatics(self):
        print "Hello Bioinformatics"

    def openFile(self, filename):
        with open(filename) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for a in content:
            if a == '':
                content.remove(a)
        return content

    def cat(self, openedFile):
        count = 0
        for a in range(len(openedFile)):
            if a == 0:
                print openedFile[a],
            else:
                if openedFile[a][0] == ">":
                    print count
                    print openedFile[a],
                    count = 0
                else:
                    count += len(openedFile[a])

    def filter(self, openedFile):
        printFlag = False
        for a in openedFile:
            if ">" in a:
                if "Rattus" in a or "Mus" in a:
                    printFlag = True
                else:
                    printFlag = False

            if printFlag == True:
                outqueue = a
            if len(outqueue) > 0:
                print outqueue[:60]
                outqueue = outqueue[60:]

    def createDataSeq(self, openedFile):
        output = ""
        for a in openedFile:
            if ">" not in a:
                output += a
                output += "@"

        print output[:-1]

    def createDataIn(self, openedFile):
        curOffset = 0
        for a in openedFile:
            if ">" in a:
                outGI = ""
                cont = True
                for b in a[4:]:
                    if b == "|":
                        cont = False
                    if cont == True:
                        outGI += b
                print outGI, curOffset
                curOffset += 1
            else:
                curOffset += len(a)

    def getSeq(self, query, DataSeq, DataIn):
        index = DataSeq[0].index(query)
        output = ""
        for a in DataIn:
            if index > a[1]:
                output = a[0]
        print output

g = Intro()
# g.helloBioinformatics()

opened = g.openFile("datafile.txt")
# g.cat(opened)

# g.filter(opened)

# g.createDataSeq(opened)

# g.createDataIn(opened)

dataSeq = g.openFile("data.seq")
rawdataIn = g.openFile("data.in")
dataIn = []
for a in rawdataIn:
    dataIn.append( a.split(" "))
for b in dataIn:
    b[1] = int(b[1])

g.getSeq("MHIQITDFGTAKVLSPDS", dataSeq, dataIn)