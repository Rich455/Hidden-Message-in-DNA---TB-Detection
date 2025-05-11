# greedy_motif_search.py

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
    k = len(motifs[0])
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

# Example DNA sequences from TB genome (hypothetical short samples)
Dna = [
    "ATGACAGCAGCGATGACGATCGGTTGACGCTTAGCAGCTTG",
    "ATGACCGCTGACGATGATCGTTGACCCTGCTAGCTTGATCG",
    "ATGACAGCGACGATGACGATCGGTTCACGCTCGCCAGCTTG",
    "ATGACAGCAGCGATGATGATCGGTTGACGCTTGCCAGCTTG",
    "ATGACAGCAGTGATGACGATCGGTTGACGCTAGCTAGCTTG"
]

k = 5  # motif length
t = len(Dna)

result = greedy_motif_search(Dna, k, t)
print("Best Motifs Found:")
for motif in result:
    print(motif)
