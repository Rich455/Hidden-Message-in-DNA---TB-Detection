
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




