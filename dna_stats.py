#!/usr/bin/python3

"""Module: Counts the number of occurrences of each nucleotide in a given strand of DNA."""

def dna_stats(dna_string):
    """
    Count the occurrences of each nucleotide in a given DNA strand.

    This function takes a string representing a DNA sequence and counts the number of times each nucleotide ('A', 'C', 'G', 'T') appears in the sequence.

    Args:
        dna_string (str): A string representing the sequence of nucleobases in a single strand of DNA.

    Returns:
        None

    Prints:
        The counts of 'A', 'C', 'G', 'T' in the format:
        A: count_A, C: count_C, G: count_G, T: count_T

    Example:
        >>> dna_stats("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
        A: 20, C: 12, G: 17, T: 21
    """
    nucleotides = ['A', 'C', 'G', 'T']
    counts = [dna_string.count(nuc) for nuc in nucleotides]

    for nuc, count in zip(nucleotides, counts):
        print(f"{nuc}: {count}", end=", " if nuc != nucleotides[-1] else " ")
