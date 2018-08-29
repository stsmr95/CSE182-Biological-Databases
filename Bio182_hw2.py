from locAL import locAL
from randomDNA import randomDNA

class HW2:

    def openFile(self, filename):
        with open(filename) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for a in content:
            if a == '':
                content.remove(a)
        return content

# h = locAL()
g = randomDNA()

seqs1 = g.generateSeqs(500, 1000)
for a in seqs1:
    print a
# seqs2 = g.generateSeqs(500, 1000)

# lengths = list()
# for i in range(0, 500):
#     h.localAlignment(seqs1[i], seqs2[i], 1, -30, 0, False)
