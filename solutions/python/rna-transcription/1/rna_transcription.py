def to_rna(dna_strand):
    dna_nucleotides = ["A", "C", "G", "T"]
    rna_nucleotides = ["U", "G", "C", "A"]
    rna_strand = []

    for nucleotide in dna_strand:
        if nucleotide in dna_nucleotides:
            index = dna_nucleotides.index(nucleotide)
            rna_strand.append(rna_nucleotides[index])

    return "".join(rna_strand)