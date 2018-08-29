def parseFile(fname):
    headers = list()
    tempSeq = list()
    finalSeq = list()
    with open(fname) as f:
        lines = [i.strip() for i in f]
        lines = [line for line in lines if line]

        for i in lines:
            if i[0] == '>':
                finalSeq.append(''.join(tempSeq))
                del tempSeq
                headers.append(i)
            else:
                tempSeq.append(i)

        finalSeq.append(''.join(tempSeq))
        del tempSeq

        del finalSeq[0]
    return headers, finalSeq

h, s = parseFile("UP000006737.fasta.txt")

newH = h[24:126]
newS = s[24:126]

print(len(newH))

target = open("ourSequences.txt", 'w')

for i in range(len(newH)):
    target.write(newH[i])
    target.write('\n')
    target.write(newS[i])
    target.write('\n')

