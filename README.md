# PyND's mass spec analysis for PUBS

A poorly organized repository for mass spectrometry analysis for Physical Underpinnings of Biological Systems (PUBS) 2015 at UCSF, group _E. Poss_ — PyND. Authors: Douglas Myers-Turnbull, Yuliya Birman, Nick Rettko, and Paul Thomas.

Also see `https://github.com/tlnagy/seq-analysis` for sequencing data analysis.

The code (`.py` and `.ipynb` files) is licensed under the Apache License, Version 2.0.

## Miscellaneous notes

All files:

1. Parse (read in tab-separated columns, split some columns by "i" and "|") 
2. Normalize (filter out non-ubiquitin proteins/peptides)
3.  When filtering out, might want to use 'REV' peptides and 'contaminant' fields and 'Posterior Error Probability'

First data file:

1. Take note of abundance of kinases; also: make sure ALK1 isn't there for knockout
4.  Identify which peptides are phosphorylated (directly in file)
5.  Isolate the serine-threonine ALK1 (not the ALK1 that phosphorylates tyrosine) 
6.  Try to find ALK1 binding motif?
6.  Analyze peptide/protein abundance
7.  Make list of sites that we know are not phosphorylated (or, at least, there is a high probability that they're not phosphorylated). Also, somehow account for sites that COULD be phosphorylated

Going through the table:

(Mostly use Evidence table. For Summary, just use "peaks" data. For Experiment, look at PEP . Don't need to do much with Peptides. For Modifications)
