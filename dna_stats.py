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
        The counts of 'A', 'C', 'G', 'T' separated by spaces.

    Example:
        >>> dna_stats("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
        20 12 17 21
    """
    nucleotides = ['A', 'C', 'G', 'T']
    counts = [dna_string.count(nuc) for nuc in nucleotides]

    for count in counts:
        print(count, end=" ")

