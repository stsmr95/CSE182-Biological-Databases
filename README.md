## CSE182 Biological Databases

The following are python files written and used in the Biological Databases classes. Most functions are implemented to obtain, manipulate, or sort DNA data from online databases.

#### Bio182_hw1.py

Program used to open and process given bioinformatics data, which includes DNA sequences and descriptions.

#### Bioinf182_hw2.py

Program used to generate a random sequences of DNA using randomDNA.py and utilize the local alignment function on those sequences.

#### locAL.py 

Implements the local alignment function. This function aligns two sequences of DNA together based on long matching sequences. 

#### modAL.py

Implements a modified global alignment function. This function aligns two sequences of DNA based on the best score over the entire DNA sequence. 

#### Bioinf183_hw3.py

Implements a trie data structure to store long sequences of DNA.

#### randomDNA.py

Generates random sequences of DNA given the number of sequences and their desired length.

#### parseFafsta.py

Parses a fasta file to remove the headers of the reads and return a file of DNA sequences to be used with other functions.
 
#### pythonBlast.py

Searches the BLAST database for given DNA reads and returns the score, e-value, and description. 

#### queryDatabases.py

Seaches through multiple databases, like KEGG, GO, and Prosite  for given DNA reads and writes the returned data in a TSV file.

#### renameScript.py

Simple script used to rename files to organize files for another program.  

