#!/usr/bin/env python3

import re


class SiteString:
    """
    A peptide sequence with one or more amino acids mapped to a score or name
    """

    orig_seq = None
    sequence = None
    sites = None # Make a dict later

    def __init__(self, string):
        """
        string: A string from the data file like 'AFVNHM(8.97)M(-8.97)SSHSNHPGKR'
        """
        self.orig_seq = string
        self.sites = {}
        #pattern = '\\((-?[\\d.]+)\\)'
        pattern = '\\(([^\\)]+)\\)'
        offset = 0
        for match in re.finditer(pattern, string):
            to_value = match.group(1)
            try:
                to_value = float(to_value)
            except: pass
            self.sites[match.start() + offset] = to_value
            offset -= len(match.group(0))
        self.sequence = re.sub(pattern, '', string)

    def __str__(self):
        return self.orig_seq

    def __repr__(self):
        return self.orig_seq