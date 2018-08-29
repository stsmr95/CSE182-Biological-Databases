import sys

class locAL:

    def openFile(self, filename):
        with open(filename) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for a in content:
            if a == '':
                content.remove(a)
        return content

    def localAlignment(self, seq1, seq2, match, mismatch, indels, alignment):
        n = len(seq1)
        m = len(seq2)
        scoreMatrix = [[0 for a in range(m + 1)] for b in range(n + 1)]
        bTMatrix = [[0 for c in range(m + 1)] for d in range(n + 1)]
        maxi = 0

        for i in range(1, n + 1, 1):
            for j in range(1, m + 1, 1):
                diag = scoreMatrix[i - 1][j - 1] + mismatch
                if seq1[i-1] == seq2[j-1]:
                    diag = scoreMatrix[i - 1][j - 1] + match
                scoreMatrix[i][j] = max(0,
                                     scoreMatrix[i - 1][j] + indels,
                                     scoreMatrix[i][j - 1] + indels,
                                     diag)

                if scoreMatrix[i][j] > maxi:
                    o = i
                    p = j
                    maxi = scoreMatrix[i][j]

                if scoreMatrix[i][j] == scoreMatrix[i - 1][j] + indels:
                    if scoreMatrix[i - 1][j] < 0 and scoreMatrix[i][j - 1] < 0 and scoreMatrix[i - 1][j - 1] < 0:
                        bTMatrix[i][j] = 0
                    else:
                        bTMatrix[i][j] = 3
                elif scoreMatrix[i][j] == scoreMatrix[i][j - 1] + indels:
                    if scoreMatrix[i - 1][j] < 0 and scoreMatrix[i][j - 1] < 0 and scoreMatrix[i - 1][j - 1] < 0:
                        bTMatrix[i][j] = 0
                    else:
                        bTMatrix[i][j] = 1
                elif scoreMatrix[i][j] == diag:
                    bTMatrix[i][j] = 2

        # for s in bTMatrix:
        #     print s

        print "Max score:" , maxi
        y = o
        z = p
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
        print "Length:", length
        if alignment == True:
            print ""
            print "First sequence:", self.outputLAP2(bTMatrix, seq1, y, z, scoreMatrix)
            print ""
            print "Second sequence:", self.outputLAP(bTMatrix, seq2, y, z, scoreMatrix)
        return length

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


g = locAL()
args = list(sys.argv)

# initial loCAL
if len(args) >= 8:
    seqfile = args[1]
    # print seqfile
    f = g.openFile(seqfile)
    match = args[3]
    mismatch = args[5]
    indels = args[7]
    alignment = False

    if len(args) == 9:
        if args[8] == "-a":
            alignment = True
    g.localAlignment(str(f[1]), str(f[3]), int(match), int(mismatch), int(indels), alignment)
else:
    print "python locAL.py <seq file> -m <match> -s <mismatch> -d <indel> -a"

# Modded loCAL
# print args


# seqs1 = list()
# seqs2 = list()
# for a in range(0, len(rawseqs1)):
#     seqs1.append(rawseqs1[a])
#     seqs2.append(rawseqs2[a])
#
#
# seqs1 = g.openFile(args[1])
# seqs2 = g.openFile(args[2])
# P1 = list()
#
# print "Current: "
# for b in range(0,250):
#     print b
#     P1.append(g.localAlignment(str(seqs1[b]), str(seqs2[b]), 1, -1.2, -1.2, False))
#
# print "LENGTHS: "
# for c in P1:
#     print c

