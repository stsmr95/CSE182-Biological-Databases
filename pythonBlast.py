from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

class pythonBlast:

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

# Opens our sequences
g = pythonBlast()
opened = g.openFile("ourSequences.txt")

# Queries the sequences against the BLAST database, saves a .xml file
for z in range(37, len(opened) + 1):
    outNum = z
    curSeq = opened[z]
    outputName = "output" + str(outNum + 25) + ".xml"
    print "BLASTING SEQUENCE: " + str(outNum + 25).zfill(2) + " " + str(curSeq[0:30] + "...")
    result_handle = NCBIWWW.qblast("blastp", "nr", curSeq)
    with open(outputName, "w") as out_handle:
        out_handle.write(result_handle.read())

    result_handle.close()


# Reads through the raw data, and returns the score, e-value, and description
print "Num:" + '\t' + "Score:" + '\t' + "E-value:" + '\t' + "Description:"

for z in range(25, 127):
    outNum = z
    outputName = "output" + str(outNum) + ".xml"
    result_handle = open(outputName)
    blast_record = NCBIXML.read(result_handle)
    title = blast_record.alignments[0].title.split(">")[0]

    outstring = str(outNum) + '\t'
    for hsp in blast_record.alignments[0].hsps:
        outstring += str(hsp).split("\n")[0].split(",")[0].split(" ")[1] + '\t'
        outstring += str(hsp).split("\n")[0].split(",")[1].split(" ")[2] + '\t'

    title = title.split("|")[4]
    outstring += title[1:]
    print outstring