# pubs
Physical Underpinnings of Biological Systems 2015, group E. Poss - PyND

## Analysis of MS/MS data

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
