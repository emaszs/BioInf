from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO, AlignIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from subprocess import call

"""
enterez_query = 'mammals[Organism]'
ncbi = NCBIWWW.qblast(program="blastp" , database="swissprot", 
                                sequence="4504347", 
                                entrez_query=enterez_query, expect=10.0, hitlist_size=21) #seka, pagal kuria ieskoma  galima nurodyti ir kodu
     
# Nuskaitom XML formatu parsiustus duomenis. Patartina siuos duomenis issisaugoti i faila, ir pakartotinai kreiptis tik esant butinybei.
print (ncbi)
blast = NCBIXML.read(ncbi)
for sequence in blast.alignments:
    print ('>%s'%sequence.title) # rasto atitikmens pavadinimas fasta formatu
    print (sequence.hsps[0].sbjct) # rasto atitikmens labiausiai patikimo sutampancio fragmento seka. Kiti maziau patikimi fragmentai [kuriu indeksai didesni nei 0] nedomina. 
   
writeArray = []
 
for sequence in blast.alignments:
    record = SeqRecord(seq=Seq(sequence.hsps[0].sbjct), id=sequence.title)
    writeArray.append(record)
SeqIO.write(writeArray, "sequences.faa", "fasta")
   
# Kvieciame muscle palyginio sudarymo komanda per komandine eilute. 
# muscle.exe failas turi buti prieinamas visoje operacineje sistemoje
muscleCommand = "muscle -in sequences.faa -out sequences.afa"
call(muscleCommand)
"""
alignedSequences =  AlignIO.read("sequences.afa", "fasta")

humanSequence = None
for i in range(len(alignedSequences)):
    if "HBA_HUMAN" in alignedSequences[i].name:
        humanSequence = alignedSequences[i]
        
        # sukuriamas naujas palyginiu sarasas be zmogaus sekos
        alignedNoHuman = alignedSequences[:i]
        alignedNoHuman.extend(alignedSequences[i+1:])
        break


sumArray = []
    
print("Sulygintos sekos:")
for seq in alignedNoHuman:
    print(seq.seq)
    
# Kiekviena zmogaus geno stulpeli
for i in range(len(humanSequence.seq)):
    # Lyginame su visais kitais panasiais genais ir sumuojame sutapimu skaiciu
    currentSum = 0
    for sequence in alignedNoHuman:
        if sequence.seq[i] == humanSequence.seq[i]:
            currentSum += 1
    sumArray.append(currentSum)
    
print("Sumu masyvas:")
print(sumArray) 

searchSequenceLen = 25

minSum = 9999
minSumPosition = -1
maxSum = -1
maxSumPosition = -1

for i in range(len(humanSequence) - searchSequenceLen):
    currentSum = 0
    for j in range(i, i+searchSequenceLen, 1):
        currentSum += sumArray[j]
        
    if currentSum < minSum:
        minSum = currentSum
        minSumPosition = i     
    if currentSum > maxSum:
        maxSum = currentSum
        maxSumPosition = i
        
print("Min. indeksas: %d Maks. indeksas: %d" % (minSumPosition, maxSumPosition))

print("Maziausiai i kitus panasus zmogaus hemoglobino geno 25 ilgio fragmentas su suma %d:" % minSum)
print(humanSequence[minSumPosition:minSumPosition+searchSequenceLen].seq)
print("Labiausiai i kitus panasus zmogaus hemoglobino geno 25 ilgio fragmentas su suma %d:" % maxSum)
print(humanSequence[maxSumPosition:maxSumPosition+searchSequenceLen].seq)        
    

    