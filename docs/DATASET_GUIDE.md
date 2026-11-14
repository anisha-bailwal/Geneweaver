\# GeneWeaver Sample DNA Dataset



\## 1. Introduction



This dataset contains sample DNA sequences for testing

the GeneWeaver DNA alignment engine.



\## 2. File Information



\- File name: sample\_sequences.fasta

\- File format: FASTA

\- Location: data/sample\_sequences.fasta

\- Number of sequences: 10

\- Sequence type: DNA



\## 3. DNA Alphabet



DNA sequences contain four standard nucleotide bases:



\- A: Adenine

\- T: Thymine

\- G: Guanine

\- C: Cytosine



\## 4. FASTA Format



FASTA is a text-based format used to store biological

sequences.



Each sequence contains two main parts:



1\. Header: Starts with the greater-than symbol (>).

2\. Sequence: Contains the DNA nucleotide letters.



Example:



>sequence\_001

ATGCTAGCTAGCTAACGTTAGC



\## 5. Dataset Structure



The dataset contains ten sample sequences.



Each sequence has a unique identifier:



\- sequence\_001

\- sequence\_002

\- sequence\_003

\- sequence\_004

\- sequence\_005

\- sequence\_006

\- sequence\_007

\- sequence\_008

\- sequence\_009

\- sequence\_010



\## 6. Purpose of the Dataset



This dataset will be used to:



\- Test FASTA file reading.

\- Verify sequence extraction.

\- Check DNA alphabet validation.

\- Prepare input for alignment algorithms.

\- Test the GeneWeaver parser module.



\## 7. Validation Requirements



The parser should eventually verify:



\- Every sequence has a valid header.

\- DNA sequences contain only A, T, G and C.

\- Empty sequences are handled correctly.

\- Multiple sequences can be read from one file.

\- Sequence identifiers are extracted correctly.



\## 8. Current Limitations



This is a small sample dataset created for initial

development and testing.



It is not a clinical or research-grade dataset.



\## 9. Future Improvements



Future datasets may include:



\- Larger DNA sequences.

\- Thousands of input sequences.

\- Different sequence lengths.

\- Sequences containing biological ambiguity codes.

\- Publicly available biological reference datasets.



\## 10. Conclusion



The sample dataset provides an initial input source

for developing and testing the GeneWeaver parser.

