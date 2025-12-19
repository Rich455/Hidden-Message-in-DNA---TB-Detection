
# Hi, I’m Richard 👋
**M.D. | M.S. Computer Science (Bioinformatics & HPC)**  
**Interests:** Bioinformatics, Genomics, Causal Inference, Clinical Data

## DNA Motif Detection in *Mycobacterium tuberculosis*

### Project Overview
This project applies bioinformatics algorithms (**Greedy Motif Search** & **Randomized Motif Search**) to find conserved DNA motifs in *M. tuberculosis* genomes.

---

### What Does This Mean?
- **DNA motifs** are short recurring patterns in the genome, acting as:
  - Regulatory switches for TB genes
  - Markers of drug resistance (mutations near resistance genes)
  - Targets for diagnostics or new drugs

---

### How It Works
**Input:** DNA sequences from *M. tuberculosis* samples  
**Process:** Algorithm searches for the most conserved short sequence (motif) across all samples  
**Output:** Set of motifs consistently found in TB genomes

**Example Output:**

### Best Motifs Found

| Sequence # | Motif  |
|------------|--------|
| 1          | ATGAC  |
| 2          | ATGAC  |
| 3          | ATGAC  |
| 4          | ATGAC  |
| 5          | ATGAC  |

**Consensus Sequence:** `ATGAC`



---

### Why Is This Useful in Medicine?
- Helps researchers understand TB biology by finding hidden genetic messages  
- May identify drug resistance signatures, guiding better treatment  
- Supports diagnostic test development by targeting conserved motifs  
- Contributes to precision medicine by linking genomic patterns with clinical outcomes

---

### Notes
- Algorithm detects conserved motifs in any DNA sequences (bacteria, viruses, human)  
- Sequence logos can visually represent conservation and highlight important nucleotides




## DNA Motif Detection in Mycobacterium tuberculosis
This project applies bioinformatics algorithms (Greedy Motif Search & Randomized Motif Search) to find conserved DNA motifs in Mycobacterium tuberculosis genomes



1.**What does this mean?**

DNA motifs are short recurring patterns in the genome. They often act as:

Regulatory switches that turn TB genes on or off

Markers of drug resistance (e.g., mutations near resistance genes)

Targets for diagnostics or new drugs





2.**How it works:**

Input = DNA sequences from M. tuberculosis samples

The algorithm searches for the most conserved short sequence (motif) across all samples

Output = A set of motifs that appear consistently in TB genomes

Example output;-

Best Motifs Found:

Sequence 1: GATGA (position 10, score 0)

Sequence 2: GATGA (position 10, score 0)

Sequence 3: GATGA (position 10, score 0)

Sequence 4: GATGA (position 10, score 0)

Sequence 5: GATGA (position 10, score 0)

Consensus Sequence: GATGA




3.**Why is this useful in medicine?**

Helps researchers understand TB biology by finding hidden “genetic messages”

May identify drug resistance signatures, guiding better treatment

Could support diagnostic test development by targeting conserved motifs

Contributes to precision medicine by linking genomic patterns with clinical outcomes.





4.**Note**

This algorithm detects conserved DNA motifs in a set of DNA sequences.

Although demonstrated on Mycobacterium tuberculosis, it is generalizable and can be used to study the DNA patterns of any organism — bacteria, viruses, or human genes.

The results can help identify regulatory regions, disease-associated motifs, or drug resistance markers, supporting modern medicine and research.

Sequence logos can be generated to visually represent conservation and highlight functionally important nucleotides.


