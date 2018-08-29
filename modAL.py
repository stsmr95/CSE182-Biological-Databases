import sys
import time
class modAL:
    def openFile(self, filename):
        with open(filename) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for a in content:
            if a == '':
                content.remove(a)
        for b in content:
            if b[0] == ">":
                content.remove(b)
        return content


    def modGlobAlignment(self, seq1, seq2, match, mismatch, indels, dif):
        n = len(seq1)
        m = len(seq2)
        scoreMatrix = [[1 for a in range(m + 1)] for b in range(n + 1)]
        bTMatrix = [[0 for c in range(m + 1)] for d in range(n + 1)]
        # maxi = 0
        scoreMatrix[0][0] = 0
        for u in range(1, m + 1):
            scoreMatrix[0][u] = scoreMatrix[0][u - 1] + indels
        for v in range(1, n + 1):
            scoreMatrix[v][0] = scoreMatrix[v - 1][0] + indels
        for i in range(1, n + 1, 1):
            for j in range( i-dif, i+dif + 1, 1):
                if j > 0 and j < m+1:
                    diag = scoreMatrix[i - 1][j - 1] + mismatch
                    if seq1[i - 1] == seq2[j - 1]:
                        diag = scoreMatrix[i - 1][j - 1] + match
                    if scoreMatrix[i - 1][j] == 1:
                        scoreMatrix[i][j] = max(scoreMatrix[i][j - 1] + indels,
                                                diag)
                    elif scoreMatrix[i][j - 1] == 1:
                        scoreMatrix[i][j] = max(scoreMatrix[i - 1][j] + indels,
                                                diag)
                    elif scoreMatrix[i][j - 1] == 1 and scoreMatrix[i - 1][j] == 0:
                        scoreMatrix[i][j] = diag
                    else:
                        scoreMatrix[i][j] = max(scoreMatrix[i - 1][j] + indels,
                                                scoreMatrix[i][j - 1] + indels,
                                                diag)

                    if scoreMatrix[i][j] == scoreMatrix[i - 1][j] + indels:
                        bTMatrix[i][j] = 3
                    elif scoreMatrix[i][j] == scoreMatrix[i][j - 1] + indels:
                        bTMatrix[i][j] = 1
                    elif scoreMatrix[i][j] == diag:
                        bTMatrix[i][j] = 2

        # for a in scoreMatrix:
        #     print a
        # for b in bTMatrix:
        #     print b

        o = n
        p = m
        length = 0
        while bTMatrix[o][p] != 0:
            if bTMatrix[o][p] == 1:
                p -= 1
                length += 1
            elif bTMatrix[o][p] == 2:
                o -= 1
                p -= 1
                length += 1
            else:
                o -= 1
                length += 1

        # print length
        # print self.outputLAP2(bTMatrix, seq1, n, m, scoreMatrix)
        # print self.outputLAP(bTMatrix, seq2, n, m, scoreMatrix)
        # print scoreMatrix[n][m]
        if scoreMatrix[n][m] < -1 * dif:
            return -1, -1
        else:
            return scoreMatrix[n][m], length

    def outputLAP(self, bTMatrix, seq2, n, m, pLMatrix):
        # print bTMatrix
        curString = ""

        while bTMatrix[n][m] != 0:
            # if bTMatrix[n][m] != 0:
            if bTMatrix[n][m] == 3:
                n -= 1
                curString = '-' + curString
            elif bTMatrix[n][m] == 1:
                m -= 1
                curString = seq2[m] + curString
            else:
                n -= 1
                m -= 1
                curString = seq2[m] + curString

        return curString

    def outputLAP2(self, bTMatrix, seq1, n, m, pLMatrix):
        iniString = ""

        while bTMatrix[n][m] != 0:
            # print n,m, iniString
            if bTMatrix[n][m] == 3:
                n -= 1
                iniString = seq1[n] + iniString
            elif bTMatrix[n][m] == 1:
                m -= 1
                iniString = '-' + iniString
            else:
                n -= 1
                m -= 1
                iniString = seq1[n] + iniString

        return iniString


    # for s in bTMatrix:
    #     print s

    # print "Max score:", maxi
    # y = o
    # z = p
    # length = 0
    # while bTMatrix[o][p] != 0:
    #     if bTMatrix[o][p] == 1:
    #         p -= 1
    #         length += 1
    #     elif bTMatrix[o][p] == 2:
    #         o -= 1
    #         p -= 1
    #         length += 1
    #     else:
    #         o -= 1
    #         length += 1
    # print "Length:", length
    # if alignment == True:
    #     print ""
    #     print "First sequence:", self.outputLAP2(bTMatrix, seq1, y, z, scoreMatrix)
    #     print ""
    #     print "Second sequence:", self.outputLAP(bTMatrix, seq2, y, z, scoreMatrix)
    # return length



g = modAL()
args = list(sys.argv)
seqfile = args[1]
f = g.openFile(seqfile)

match = args[3]
mismatch = args[5]
indels = args[7]
d = args[8]

# print g.modGlobAlignment(str(f[1]), str(f[3]), int(match), int(mismatch), int(indels), int(d))
# print len(f)/2
runningtimes = list()
scores = list()
lengths = list()

for z in range(0, len(f), 2):
    start = time.time()
    outscore, outlength = g.modGlobAlignment(str(f[z]), str(f[z+1]), int(match), int(mismatch), int(indels), int(d))
    end = time.time()
    elapse = end - start
    runningtimes.append(elapse)
    scores.append(outscore)
    lengths.append(outlength)

print "Running times: "
for y in runningtimes:
    print y
print "Scores: "
for w in scores:
    print w
print "Lengths: "
for x in lengths:
    print x