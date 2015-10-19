#!/usr/bin/env python3

import pandas
import math
import re
from site_string import SiteString
import copy

def remove_cols(df, col_names_to_exclude):
    """
    Removes from the DataFrame every column whose name is a superset of any name in col_names_to_exclude
    Especially useful for filtering out the samples of other groups.
    """
    cols_copy = copy.copy(df.columns)
    for col in cols_copy:
        for group_name in col_names_to_exclude:
            if group_name.lower() in col.lower():
                df.drop(col, axis=1, inplace=True)
                break
    return df


def filter_tsv(input_file, output_file, col_name, pattern):
    """
    For a tab-delimited file input_file with the first line as a header,
    writes (to output_file) every line whose entry at column 'col_name' matches
    the regex pattern 'pattern'.
    """
    if isinstance(pattern, str):
        pattern = re.compile(pattern)

    with open(output_file, 'w') as to_write:
        with open(input_file, 'r') as fp:
            index=-1
            n = 0
            for line in fp:
                parts = line.split('\t')
                if n == 0:
                    index = parts.index(col_name)
                    if index < 0:
                        raise ValueError(col_name + ' not found in ' + str(input_file))
                    to_write.write(line)
                else:
                    if pattern.match(parts[index]):
                        to_write.write(line)
                n += 1


def parse_evidence(f, cols_to_drop=None):
    """
    cols_to_drop: if not set, defaults to various raw data:
        ['Raw file', 'MS/MS m/z', 'Charge', 'm/z', 'Mass', 'Resolution', 'Uncalibrated - Calibrated m/z [ppm]',
        'Uncalibrated - Calibrated m/z [Da]', 'Mass Error [ppm]', 'Mass Error [Da]', 'Uncalibrated Mass Error [ppm]',
        'Uncalibrated Mass Error [Da]', 'Max intensity m/z 0', 'Retention time', 'Retention length',
        'Calibrated retention time', 'Calibrated retention time start', 'Calibrated retention time finish',
        'Retention time calibration', 'Match time difference', 'Match m/z difference', 'Match q-value']
    """

    if cols_to_drop is None:
        cols_to_drop=['Raw file', 'MS/MS m/z', 'Charge', 'm/z', 'Mass', 'Resolution', 'Uncalibrated - Calibrated m/z [ppm]',
                      'Uncalibrated - Calibrated m/z [Da]', 'Mass Error [ppm]', 'Mass Error [Da]',
                      'Uncalibrated Mass Error [ppm]', 'Uncalibrated Mass Error [Da]', 'Max intensity m/z 0',
                      'Retention time', 'Retention length', 'Calibrated retention time',
                      'Calibrated retention time start', 'Calibrated retention time finish',
                      'Retention time calibration', 'Match time difference', 'Match m/z difference', 'Match q-value']


    df = pandas.read_table(f, header=0, index_col=0)

    # These are lists
    for m in [
            'Modifications',
            'Acetyl (Protein N-term)',
            'Proteins',
            'Leading proteins'
    ]:
        df[m] = df[m].map(lambda s: [st.strip() for st in str(s).split(';')])

    # And these are lists of ints
    for m in [
            'Oxidation (M) site IDs',
            'Phospho (STY) site IDs',
            'MS/MS IDs'
    ]:
        df[m] = df[m].map(lambda s: [int(st) for st in str(s).split(';')] if str(s) != 'nan' else [])

    # These have syntax like 'AFVNHM(8.97)M(-8.97)SSHSNHPGKR'
    for m in [
            'Oxidation (M) Score Diffs',
            'Phospho (STY) Score Diffs',
            'Phospho (STY) Probabilities',
            'Oxidation (M) Probabilities',
            'Modified sequence'
    ]:
        df[m] = df[m].map(lambda s: SiteString(str(s)) if str(s) != 'nan' else SiteString(''))

    # Make SiteString, but get rid of _s on ends
    df['Modified sequence'] = df['Modified sequence'].map(lambda s: SiteString(str(s)[1:-1]))

    # Some contain "Infinity", which float() understands but Pandas doesn't
    df['PEP'] = df['PEP'].map(lambda s: float(s))

    # Just use an empty list, not a list containing "Unmodified"
    df['Modifications'] = df['Modifications'].map(lambda lst: [] if lst == ['Unmodified'] else lst)

    df.drop(cols_to_drop, axis=1, inplace=True)

    return df


def parse_protein_groups(f):
    #col_indicies = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 19, 20, 21, 38, 39, 40, 41, 42, 43, 44, 45, 68, 69, 70, 71, 88, 89, 90, 91, 92, 93, 94, 95, 118, 119, 120, 121, 138, 139, 140, 141, 142, 143, 144, 145, 160, 161, 162, 163, 164, 165, 166, 167, 176, 177, 178, 179, 196, 197, 198, 199, 200, 201, 202, 203, 226, 227, 228, 229, 246, 247, 248, 249, 250, 251, 252, 253, 268, 277, 278, 279, 280, 297, 298, 299, 300, 301, 302, 303, 304, 327, 328, 329, 330, 347, 348, 349, 350, 351, 352, 353, 354, 377, 378, 379, 380, 397, 398, 399, 400, 401, 402, 403, 404, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433]
    df = pandas.read_table(f, header=0) # , usecols=col_indicies

    # These are lists
    for m in [
            'Protein IDs',
            'Majority protein IDs',
            'Fasta headers',
            'Peptide is razor',
        ]:
            df[m] = df[m].map(lambda s: [st.strip() for st in str(s).split(';')])

    # And these are lists of ints
    for m in [
            'Peptide IDs',
            'Peptide counts (all)',
            'Peptide counts (razor+unique)',
            'Mod. peptide IDs',
            'Evidence IDs',
            'MS/MS IDs',
            'Best MS/MS',
            'Oxidation (M) site IDs',
            'Phospho (STY) site IDs',
            'Oxidation (M) site positions',
            'Phospho (STY) site positions'
    ]:
        df[m] = df[m].map(lambda s: [int(st) for st in str(s).split(';')] if str(s) != 'nan' else [])

    return df

def parse_phosphosites(f):
    df = pandas.read_table(f, header=0)

    # These are lists
    for m in [
            'Proteins',
            'Leading proteins',
            'Fasta headers'
        ]:
            df[m] = df[m].map(lambda s: [st.strip() for st in str(s).split(';')])

    # And these are lists of ints
    for m in [
            'Positions within proteins'
    ]:
        df[m] = df[m].map(lambda s: [int(st) for st in str(s).split(';')] if str(s) != 'nan' else [])

    # TODO Parse out weird data structures

    return df

