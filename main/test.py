from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO, AlignIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from subprocess import call
import string
from Bio.Align import MultipleSeqAlignment

enterez_query = 'mammals[Organism]'
# ncbi = NCBIWWW.qblast(program="blastp" , database="swissprot", 
#                                 sequence="4504347", 
#                                 entrez_query=enterez_query, expect=10.0, hitlist_size=21) #seka, pagal kuria ieskoma  galima nurodyti ir kodu
  
# Nuskaitom XML formatu parsiustus duomenis. Patartina siuos duomenis issisaugoti i faila, ir pakartotinai kreiptis tik esant butinybei.
# print (ncbi)
# blast = NCBIXML.read(ncbi)
# for sequence in blast.alignments:
#     print ('>%s'%sequence.title) # rasto atitikmens pavadinimas fasta formatu
#     print (sequence.hsps[0].sbjct) # rasto atitikmens labiausiai patikimo sutampancio fragmento seka. Kiti maziau patikimi fragmentai [kuriu indeksai didesni nei 0] nedomina. 
  
writeArray = []
 
# for sequence in blast.alignments:
#     record = SeqRecord(seq=Seq(sequence.hsps[0].sbjct), id=sequence.title)
#     writeArray.append(record)
# SeqIO.write(writeArray, "sequences.faa", "fasta")
   
# Kvieciame muscle palyginio sudarymo komanda per komandine eilute. 
# muscle.exe failas turi buti prieinamas visoje operacineje sistemoje
# muscleCommand = "muscle -in sequences.faa -out sequences.afa"
# call(muscleCommand)

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
    
# Kiekviena zmogaus geno stulpeli
for seq in alignedNoHuman:
    print (seq.seq)
for i in range(len(humanSequence.seq)):
    # Lyginame su visais kitais panasiais genais ir sumuojame sutapimu skaiciu
    currentSum = 0
    for sequence in alignedNoHuman:
        if sequence.seq[i] == humanSequence.seq[i]:
            currentSum += 1
        elif sequence.seq[i] == "-":
            # Jei stulpelyje rastas tarpas, jis nebus lyginamas su kitais
            currentSum = None
            break
    sumArray.append(currentSum)
    
print (sumArray) 
    