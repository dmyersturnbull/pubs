#!/usr/bin/env python3


import pytest

# TODO: This was copied from a Jupyter notebook; we need a better way to run

from site_string import SiteString

test_sites = SiteString('AFVNHM(8.97)MM(-8.97)SSHSNH(1.0)PGKR')
assert 'AFVNHMMMSSHSNHPGKR' == test_sites.sequence
assert {6: 8.97, 8: -8.97, 14: 1.0} == test_sites.sites

test_sites_2 = SiteString('ABCD(efg)HIJK')
assert 'ABCDHIJK' == test_sites_2.sequence
assert {4: 'efg'} == test_sites_2.sites
assert 'ABCD(efg)HIJK' == str(test_sites_2)

test_sites_empty = SiteString('')
assert '' == test_sites_empty.sequence
assert {} == test_sites_empty.sites
assert '' == str(test_sites_empty.sequence)

print("Tests passed")