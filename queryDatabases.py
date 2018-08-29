from bioservices.kegg import KEGG
from Bio.ExPASy import ScanProsite
from Bio import ExPASy
import MySQLdb

def writeTSVFile(IDList, KEGG, GO, PROSITE):
    print("Writing to file...")
    target = open("chart.tsv", 'w')
    target.write("GEN ID\tKEGG PATHWAY\tGO\tPROSITE\n")

    for i in range(len(IDList)):
        # writes to file

        try:
            target.write(str(IDList[i]) + '\t' + ', '.join(KEGG[i]['PATHWAY'].values()) + '\t' + str(GO[i]) + '\t' + str(PROSITE[i]) + '\n')
        except KeyError:
            target.write(str(IDList[i]) + '\t' + "None" + '\t' + str(GO[i]) + '\t' + str(PROSITE[i]) + "\n")

    target.close()

def queryProsite(theSeqs):
    print("Currently querying Prosite...")
    prositeData = list()

    for i in theSeqs:
        handle = ScanProsite.scan(seq=i, skip="0")
        result = ScanProsite.read(handle)

        try:
            handle = ExPASy.get_prosite_entry(result[0]["signature_ac"])
            res = handle.read()

            splitted = res.split("\n")
            line = 0
            for a in range(0, len(splitted)):
                if splitted[a][0:2] == "DE":
                    line = a

            prositeData.append(splitted[line][5:-1])
            print(splitted[line][5:-1])
        except IndexError:
            prositeData.append(None)
            print(None)

    return prositeData

def queryGO(theNames):
    print("Currently querying GO...")

    GOdata = list()

    #db connect
    db = MySQLdb.connect(host="mysql-amigo.ebi.ac.uk", user="go_select", passwd="amigo", db="go_latest", port=4085)
    cur = db.cursor()
    cur2 = db.cursor()

    for i in range(len(theNames)):
        
        #query calls
        sql = "SELECT * FROM term WHERE name LIKE'" + theNames[i] + "'"
        #query term name directly
        cur.execute(sql)
        term = cur.fetchone()

        if term is None:
            # query term synonyms
            sql2 = "SELECT * FROM term INNER JOIN term_synonym ON (term.id=term_synonym.term_id)\
             WHERE term_synonym LIKE '" + theNames[i] + "'"
            cur2.execute(sql2)
            term2 = cur2.fetchone()
            GOdata.append(term2)

        else:
            GOdata.append(term)

    db.close()
    return GOdata


def queryKegg(theIDs):
    print("Currently querying KEGG...")
    k = KEGG()
    keggData = list()
    IDlist = list()

    for id in theIDs:
        ids = id[3:]
        query = k.find("acb", ids)
        query = query.split('\t')
        finalQuery = query[0]
        data = k.get(finalQuery)
        dictData = k.parse(data)

        keggData.append(dictData)
        IDlist.append(ids)

    return keggData, IDlist


def subStringIndex(list, substring):
    for i, s in enumerate(list):
        if substring in s:
              return i
    return -1

def parseHeadersForGO(headers):
    GOList = list()
    for i in headers:
        split = i.rsplit(' ')
        endingIndex = subStringIndex(split, "OS=")
        split = split[1:endingIndex]
        newSplit = ["%" + i + "%" for i in split]
        finalString = ' '.join(newSplit)
        GOList.append(finalString)
    return GOList

"""Extracts GN Number"""
def parseHeadersForKEGG(headers):
    GNList = list()
    for i in headers:
        split = i.rsplit(' ')
        matching = [s for s in split if "GN=" in s]
        string = ''.join(matching)
        GNList.append(string)

    return GNList

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
                del tempSeq[:] #python 2.7
                headers.append(i)
            else:
                tempSeq.append(i)

        finalSeq.append(''.join(tempSeq))
        del tempSeq[:] #python 2.7

        del finalSeq[0]
    return headers, finalSeq

h, s = parseFile("ourSequences.txt")

queryIDs = parseHeadersForKEGG(h)
keggsData, IDs = queryKegg(queryIDs)

queryNames = parseHeadersForGO(h)
goData = queryGO(queryNames)

proData = queryProsite(s)

writeTSVFile(IDs, keggsData, goData, proData)