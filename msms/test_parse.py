#!/usr/bin/env python3


import pandas
import pytest
import parse

# TODO: This was copied from a Jupyter notebook; we need a better way to run

df = pandas.DataFrame({'kerri' : pandas.Series([1., 2., 3., 4.]),
                       'ate' : pandas.Series([1., 2., 3., 4.]),
                       'our' : pandas.Series([1., 2., 3., 4.]),
                       'beloved' : pandas.Series([1., 2., 3., 4.]),
                       'pet' : pandas.Series([1., 2., 3., 4.]),
                       'chicken' : pandas.Series([1., 2., 3., 4.])})
df = remove_cols(df, ['love', 'ken'])
assert 4 == len(df.columns)
assert {'kerri', 'ate', 'our', 'pet'} == set(df.columns)
print(df)
print("Tests passed")


filter_tsv('test.tsv', 'output.tsv', 'evidence', re.compile('^keep'))
with open('output.tsv', 'r') as fp:
    assert ['a\tb\tevidence\tc\n', 'no\tno\tkeep\tno\n', 'no\tno\tkeeper\tno\n'] == fp.readlines()
import os
os.remove('output.tsv')
print('Tests passed')