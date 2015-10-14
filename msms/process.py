#!/usr/bin/env python3

import pandas as pd
import math

# Filter functions

def filter_bad_rows(df):

    # EX: 'Intensity Pynd_AlkKO_WCL'
    # remove known and possible contaminants
    #df = df[df['Potential contaminant'] != '+']

    # remove REV and CON

    df = df[df['Protein IDs'].str.contains("REV") == False]
    df = df[df['Protein IDs'].str.contains("CON") == False]
    #print(df['Protein IDs'].str.contains("REV"))

    return df


def compare(df, col_one, col_two, epsilon=6193.8):
    """
    Converts to log base 2 and adds epsilon if < epsilon, then divide intensities.
    :param df:
    :param col_one:
    :param col_two:
    :param epsilon:
    :return:
    """
    df = df[df[col_one] != 0 and df[col_two] != 0]
    col_one_sum = df[col_one].sum()
    col_two_sum = df[col_two].sum()
    one = df[col_one].apply(lambda x: math.log((x if x > 0 else epsilon).div(col_one_sum), 2))
    two = df[col_two].apply(lambda x: math.log((x if x > 0 else epsilon).div(col_two_sum), 2))
    return one / two
