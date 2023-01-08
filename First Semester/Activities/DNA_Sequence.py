protein_map = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 
        'TAT': 'Y', 'TAC': 'Y', 'TGT': 'C', 'TGC': 'C', 
        'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 
        'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 
        'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 
        'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 
        'CGG': 'R', 'ATT': 'T', 'ATC': 'T', 'ATA': 'T', 
        'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 
        'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 
        'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 
        'AGG': 'R', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 
        'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 
        'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 
        'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 
        'GGG': 'G', "*": "*"
    }

DNA_seq = input("Input the DNA sequence: ")

seq_len = len(DNA_seq)
codons = []

s = 0
seq_end = seq_len - seq_len % 3
for i in range(3, seq_end + 1, 3):
    codons.append(DNA_seq[s:i])
    s = i
    
if seq_end < seq_len:
    codons.append("*")

print(*[protein_map[i] for i in codons],sep="")