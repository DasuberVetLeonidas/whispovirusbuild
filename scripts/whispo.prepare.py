from __future__ import print_function
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import base.prepare
from base.prepare import prepare
from datetime import datetime
from base.utils import fix_names
import argparse

def collect_args():
    """Returns a Hendra-specific argument parser.
    """
    parser = base.prepare.collect_args()
    parser.set_defaults(
        viruses_per_month=1,
        file_prefix="whispo"
    )
    return parser

# dropped_strains = [
# ]
genes_array = []
genes_list = open('gene_list.txt')
for line in genes_list:
    line = line.strip().lstrip('     gene            ')
    genes_array.append(line)

config = {
    "dir": "whispo",
    "file_prefix": "whispo",
    "title": "Real-time tracking of white spot disease virus transmission",
    "maintainer": ["Matt and Leo", ""],
    "input_paths": ["whispo_edited.fasta"],
    "header_fields": { 0:'strain', 3:'date', 4:'country', 8:'host'},
    # "filters": (
    # ),
    # "subsample": {
    #     "category": lambda x:(x.attributes['date'].year, x.attributes['date'].month, x.attributes['town']),
    # },
    "colors": ["country", "host"],
    "color_defs": ["colors.tsv"],
    "lat_longs": ["country"],
    "auspice_filters": ["country", "host"],
    "reference": {
        "path": "whispovirus_reference.gb",
        "metadata": {
            'strain': "whispovirus", "accession": "NC_003225", "date": "1994-10-1",
            'host': "Marsupenaeus japonicus", 'country': "china"
        },
        "include": 2,
        "genes": genes_array
    }
}

if __name__=="__main__":
    parser = collect_args()
    params = parser.parse_args()
    # if params.viruses_per_month == 0:
    #     config["subsample"] = False
    # else:
    #     config["subsample"]["threshold"] = params.viruses_per_month
    #
    if params.sequences is not None:
        config["input_paths"] = params.sequences

    if params.file_prefix is not None:
        config["file_prefix"] = params.file_prefix

    runner = prepare(config)
    runner.load_references()
    print('runner.load_reference finished')
    # runner.applyFilters()
    runner.ensure_all_segments()
    print('runner.ensure_all_segments finished')
    runner.subsample()
    print('runner.subsample finished')
    runner.colors()
    runner.latlongs()
    runner.write_to_json()
