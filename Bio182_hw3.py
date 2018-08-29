class HW3:
    def openFile(self, filename):
        with open(filename) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for a in content:
            if a == '':
                content.remove(a)
        return content

    def initializeTrie(self):
        pointList = list()
        points = list()
        pointList.append(points)
        letterList = list()
        letters = list()
        letterList.append(letters)
        countList = list()
        counts = list()
        countList.append(counts)

        return pointList, letterList, countList

    def appendTrie(self, pointList, letterList, countList, string):
        curPoint = 0
        for a in string:
            if a in letterList[curPoint]:
                pos = letterList[curPoint].index(a)
                curPoint = pointList[curPoint][pos]
                countList[curPoint][0] += 1
            else:
                letterList[curPoint].append(a)
                pointList[curPoint].append(len(pointList))

                curPoint = len(pointList)
                counts = list()
                countList.append(counts)
                countList[curPoint].append(1)
                newList = list()
                pointList.append(newList)
                newLetters = list()
                letterList.append(newLetters)

        return pointList, letterList, countList

    def numTimes(self, pointList, letterList, countList, string):
        curPoint = 0
        for a in string:
            if a in letterList[curPoint]:
                pos = letterList[curPoint].index(a)
                curPoint = pointList[curPoint][pos]
            else:
                return 0

        return countList[curPoint][0]


g = HW3()
dblinesraw = g.openFile("DNA.txt")
dblinesraw = dblinesraw[1:]

queries = g.openFile("queries2.txt")


dblines = ""
for a in dblinesraw:
    dblines += a

pointList, letterList, countList = g.initializeTrie()

totallines = len(queries)
for h in queries:
    print "Number of lines left: ", totallines
    for i in range(len(dblines) - len(h)):
        if h[0:10] == dblines[i:i+10]:
            pointList, letterList, countList = g.appendTrie(pointList, letterList, countList, dblines[i:i + 50])
    totallines -= 1

print "Numbers of times found:"
for q in queries:
    print q, g.numTimes(pointList,letterList,countList,q)
