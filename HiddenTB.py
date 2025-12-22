

#Load the Real TB Genome from FASTA

from Bio import SeqIO, pairwise2
from Bio.Seq import Seq

# Load genome safely


def load_genome(fasta_path):
    with open(fasta_path, "r") as f:
        for record in SeqIO.parse(f, "fasta"):
            return str(record.seq).upper()


# Extract gene using reference coordinates
# (coordinates are valid ONLY for H37Rv)


def extract_gene(genome, start, end):
    return genome[start:end]


# Align gene sequences and detect SNPs


def find_mutations_aligned(ref_seq, query_seq, start_pos):
    alignment = pairwise2.align.globalms(
        ref_seq, query_seq,
        2, -1, -5, -0.5,
        one_alignment_only=True
    )[0]

    aligned_ref, aligned_query = alignment.seqA, alignment.seqB

    mutations = []
    ref_index = start_pos

    for r, q in zip(aligned_ref, aligned_query):
        if r != "-":
            if q != "-" and r != q:
                mutations.append((ref_index, r, q))
            ref_index += 1

    return mutations, len(ref_seq)


# Paths

# drug sentitive is Mycobacterium tuberculosis H37Rv complete genome
# drug resistant is Mycobacterium tuberculosis strain SCAID 320.0  

DS_path = r"D:\TB_PROJECT\drug_sensitive\drug_sensitive.fasta"   # H37Rv
DR_path = r"D:\TB_PROJECT\drug_resistant\drug_resistant.fasta"   # SCAID 320.0

DS_genome = load_genome(DS_path)
DR_genome = load_genome(DR_path)

print("Drug-sensitive genome length:", len(DS_genome))
print("Drug-resistant genome length:", len(DR_genome))



# Resistance genes (H37Rv coords)

resistance_genes = {
    "rpoB":  (759807, 763325),
    "katG":  (2153888, 2156111),
    "inhA":  (2161154, 2162501),
    "gyrA":  (2714915, 2716432),
    "embB":  (4246515, 4249806)
}


# Analyze genes

print("\n--- Mutation Analysis (Aligned) ---\n")

for gene, (start, end) in resistance_genes.items():
    ref_seq = extract_gene(DS_genome, start, end)
    query_seq = extract_gene(DR_genome, start, end)

    mutations, gene_length = find_mutations_aligned(ref_seq, query_seq, start)

    percent = (len(mutations) / gene_length) * 100

    print(f"Gene: {gene}")
    print(f"Gene length: {gene_length} bp")
    print(f"Total mutations detected: {len(mutations)}")
    print(f"Mutation percentage: {percent:.2f}%")

    if mutations:
        for pos, ref, alt in mutations[:10]:
            print(f"  {pos}: {ref} → {alt}")
        if len(mutations) > 10:
            print("  ...")
    else:
        print("  No mutations detected")

    print("-" * 40)
