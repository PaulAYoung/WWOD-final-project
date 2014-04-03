#!/usr/bin/env python

from os import path

from datacompiler import combine_datasets

data_profiles = [
    {
        "pattern": r"gradaf\d\d.txt|GRADAF\d\d.DBF",
        "columns": "ALL",
        "makelower": True,
        "outfile": "graduates.csv"
    },
    {
        "pattern": r"dropouts\d\d.txt",
        "columns": "ALL",
        "makelower": True,
        "outfile": "dropouts.csv"
    },
    {
        "pattern": r"grads\d\d.txt",
        "columns": "ALL",
        "makelower": True,
        "outfile": "ucqualifiedgrads.csv"
    },
    {
        "pattern": r"enr\d\d.txt",
        "columns": "ALL",
        "makelower": True,
        "outfile": "enrollment.csv"
    }

    ]


def mass_combiner(data_path, out_path, data_profiles):
    """docstring for mass_combiner"""
    for d in data_profiles:
        print "creating {}".format(d["outfile"])
        df = combine_datasets(data_path, **d)
        df.to_csv(path.join(out_path, d["outfile"]))


def main():
    """docstring for main"""
    mass_combiner('data/', 'compileddata', data_profiles)

if __name__ == '__main__':
    main()
