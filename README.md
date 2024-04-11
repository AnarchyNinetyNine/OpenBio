# OpenBio

Welcome to the OpenBio repository! This collection of functions and scripts provides useful tools for performing bioinformatics analysis tasks. Whether you're working with DNA sequences, calculating molecular properties, or analyzing genetic data, these tools can help streamline your workflow.

## Installation

Clone this repository to your local machine using:

```bash
git clone https://github.com/AnarchyNinetyNine/bioinformatics_tools.git
```

## Functions

### `dna_stats`

Counts the occurrences of each nucleotide in a given DNA strand.

#### Usage

```python
from bioinformatics_tools import dna_stats

dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
dna_stats(dna_string)

# Output: 20 12 17 21
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for new features, improvements, or bug fixes.

## License

This project is licensed under the MIT License - see the [License page](https://github.com/AnarchyNinetyNine/bioinformatics_tools/blob/main/LICENSE) for details.
