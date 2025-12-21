

#Load the Real TB Genome from FASTA

# Import Libraries
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# Path to your FASTA file
# mutli drug resistance TB genome
fasta_path = "D:/Mycobacterium tuberculosis strain SCAID 320.0, complete genome/sequence.fasta"


records = list(SeqIO.parse(fasta_path, "fasta"))
genome = str(records[0].seq)

# Length of the genome

print(f"Genome loaded: {records[0].id}")
print(f"Genome length: {len(genome)}")



# Drug resistance specific genes location 

resistance_genes = {
    "rpoB":  (759807, 763325),   # Rifampicin
    "katG":  (2153888, 2156111), # Isoniazid
    "inhA":  (2161154, 2162501), # Isoniazid
    "gyrA":  (2714915, 2716432), # Fluoroquinolones
    "embB":  (4246515, 4249806)  # Ethambutol
}

def extract_gene_regions(genome, genes, upstream=500):
    regions = []
    for gene, (start, end) in genes.items():
        region_start = max(0, start - upstream)
        region_seq = genome[region_start:end]
        regions.append(region_seq)
        print(f"{gene}: extracted {len(region_seq)} bp")
    return regions

Dna = extract_gene_regions(genome, resistance_genes)



# greedy search algorthim 
# greedy motif search to find short DNA patterns (motifs) that are highly conserved across these genes.


def extract_gene_regions(genome, genes, upstream=500):
    regions = []
    for gene, (start, end) in genes.items():
        region_start = max(0, start - upstream)
        region_seq = genome[region_start:end]
        regions.append(region_seq)
        print(f"{gene}: extracted {len(region_seq)} bp")
    return regions

Dna = extract_gene_regions(genome, resistance_genes)


def score(motifs):
    score = 0
    k = len(motifs[0])
    for i in range(k):
        counts = {'A':0, 'C':0, 'G':0, 'T':0}
        for motif in motifs:
            counts[motif[i]] += 1
        score += len(motifs) - max(counts.values())
    return score


def count(motifs):
    k = len(motifs[0])
    counts = {'A':[0]*k, 'C':[0]*k, 'G':[0]*k, 'T':[0]*k}
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            counts[nucleotide][i] += 1
    return counts


def profile(motifs):
    counts = count(motifs)
    t = len(motifs)
    return {nuc: [c/t for c in counts[nuc]] for nuc in 'ACGT'}


def pr(kmer, prof):
    prob = 1
    for i, nuc in enumerate(kmer):
        prob *= prof[nuc][i]
    return prob


def most_probable_kmer(text, k, prof):
    max_prob = -1
    best_kmer = text[0:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        p = pr(kmer, prof)
        if p > max_prob:
            max_prob = p
            best_kmer = kmer
    return best_kmer


def greedy_motif_search(Dna, k, t):
    best_motifs = [dna[0:k] for dna in Dna]
    for i in range(len(Dna[0]) - k + 1):
        motifs = [Dna[0][i:i+k]]
        for j in range(1, t):
            prof = profile(motifs)
            motifs.append(most_probable_kmer(Dna[j], k, prof))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs
    

# finding and printing motifs of length 6 in the resistance genes

k = 6
t = len(Dna)

motifs = greedy_motif_search(Dna, k, t)

print("Resistance-Associated Motifs Found:")
for gene, motif in zip(resistance_genes.keys(), motifs):
    print(f"{gene}: {motif}")

# print consensus motif

from collections import Counter

def consensus(motifs):
    k = len(motifs[0])
    consensus_seq = ""
    for i in range(k):
        column = [motif[i] for motif in motifs]
        consensus_seq += Counter(column).most_common(1)[0][0]
    return consensus_seq

print("Consensus Resistance Motif:", consensus(motifs))




### Comparison between the drug sentitive and drug resistant TB genome.


# drug sentitive is Mycobacterium bovis AF2122/97
# drug resistant is Mycobacterium tuberculosis strain SCAID 320.0



import os
from Bio import SeqIO

# Function to safely load a single genome
def load_single_genome_safe(fasta_path):
    genome = []
    with open(fasta_path, "rb") as f:  # read as binary
        for line in f:
            if line.startswith(b">"):
                continue
            line = line.decode("ascii", errors="ignore").strip()
            genome.append(line)
    genome = "".join(genome)
    # Keep only valid DNA characters
    genome = "".join(base for base in genome if base in "ACGTN")
    return genome



# drug sentitive is Mycobacterium bovis AF2122/97
# drug resistant is Mycobacterium tuberculosis strain SCAID 320.0


# Paths to your genomes
DS_path = r"D:\TB_PROJECT\drug_sensitive\drug_sensitive.fasta"
DR_path = r"D:\TB_PROJECT\drug_resistant\drug_resistant.fasta"

# Load genomes
DS_genome = load_single_genome_safe(DS_path)
DR_genome = load_single_genome_safe(DR_path)

# Wrap in list for compatibility with extract_regions
DS_genomes = [DS_genome]
DR_genomes = [DR_genome]

print("Drug-sensitive genome length:", len(DS_genome))
print("Drug-resistant genome length:", len(DR_genome))

# Define resistance genes coordinates
resistance_genes = {
    "rpoB": (759807, 763325),
    "katG": (2153888, 2156111),
    "inhA": (2161154, 2162501),
    "gyrA": (2714915, 2716432),
    "embB": (4246515, 4249806)
}

# Function to extract regions including upstream bases
def extract_regions(genomes, genes, upstream=500):
    regions = []
    for genome in genomes:
        for start, end in genes.values():
            region_start = max(0, start - upstream)
            regions.append(genome[region_start:end])
    return regions

# Extract regions
DS_regions = extract_regions(DS_genomes, resistance_genes)
DR_regions = extract_regions(DR_genomes, resistance_genes)

print("DS regions:", len(DS_regions))
print("DR regions:", len(DR_regions))


# Greed search algorthim 

def score(motifs):
    score = 0
    k = len(motifs[0])
    for i in range(k):
        counts = {'A':0, 'C':0, 'G':0, 'T':0}
        for motif in motifs:
            counts[motif[i]] += 1
        score += len(motifs) - max(counts.values())
    return score

def count(motifs):
    k = len(motifs[0])
    counts = {'A':[0]*k, 'C':[0]*k, 'G':[0]*k, 'T':[0]*k}
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            counts[nucleotide][i] += 1
    return counts

def profile(motifs):
    counts = count(motifs)
    t = len(motifs)
    return {nuc: [c/t for c in counts[nuc]] for nuc in 'ACGT'}

def pr(kmer, prof):
    prob = 1
    for i, nuc in enumerate(kmer):
        prob *= prof[nuc][i]
    return prob

def most_probable_kmer(text, k, prof):
    max_prob = -1
    best_kmer = text[0:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        p = pr(kmer, prof)
        if p > max_prob:
            max_prob = p
            best_kmer = kmer
    return best_kmer

def greedy_motif_search(Dna, k, t):
    best_motifs = [dna[0:k] for dna in Dna]
    for i in range(len(Dna[0]) - k + 1):
        motifs = [Dna[0][i:i+k]]
        for j in range(1, t):
            prof = profile(motifs)
            motifs.append(most_probable_kmer(Dna[j], k, prof))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


# Motifs pattern length 

k = 6

DS_motifs = greedy_motif_search(DS_regions, k, len(DS_regions))
DR_motifs = greedy_motif_search(DR_regions, k, len(DR_regions))

print("Drug-Sensitive Motifs:")
print(DS_motifs)

print("\nDrug-Resistant Motifs:")
print(DR_motifs)


# Print the motif of drug sentitive and drug resistant

DS_set = set(DS_motifs)
DR_set = set(DR_motifs)

print("Motifs unique to DR strains:")
print(DR_set - DS_set)

print("\nMotifs unique to DS strains:")
print(DS_set - DR_set)












