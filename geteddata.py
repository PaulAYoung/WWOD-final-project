#!/usr/bin/env python

import argparse
import os
import zipfile

from datascrape import mass_downloader, download_file
from datasources import data_sets


def get_data(sources):
    for source in sources:
        outpath = os.path.join(os.path.curdir, 'data')
        if type(source) == dict:
            mass_downloader(out_dir=outpath, retry=True, **source)
        elif type(source) == str:
            path = os.path.split(os.path.splitext(source)[0])[1]
            path = os.path.join(outpath, path)
            download_file(source, path, retry=True)
        else:
            raise Exception("Data source in invalid format")

        # unzip if file is .zip or .exe
        if path[-4:].lower() in [".exe", ".zip"]:
            with zipfile.ZipFile(path, 'r') as z:
                z.extractall(outpath)


def list_data_sets():
    """docstring for list_data_sets"""
    sources = data_sets.keys()
    sources.sort()
    print "Data sets:"
    for d in sources:
        print "\t - {}".format(d)


def main():
    parser = argparse.ArgumentParser(description="Download data sets")
    parser.add_argument(
        'data',
        type=str,
        nargs='*',
        help="A list of datasets to be downloaded."
        )
    parser.add_argument(
        '-a',
        '-all',
        help="This option indicates all data sets should be downloaded.",
        action="store_true"
        )
    parser.add_argument(
        '-l',
        '-ls',
        help="List all available data sources",
        action="store_true"
        )

    opts = parser.parse_args()

    sources = []
    if opts.l:
        list_data_sets()
    elif opts.a and len(opts.data) > 0:
        print "You can't specify specific data sets and all"
    elif opts.a:
        print "Downloading all data."
        sources = data_sets.values()
        get_data(sources)
    elif len(opts.data) > 0:
        print opts.data
        for i in opts.data:
            if i in data_sets:
                sources.append(data_sets[i])
            else:
                print "{} not found".format(i)
                print "Please review data sets and retry."
                list_data_sets()
                raise Exception("Invalid data source.")
            print sources
            get_data(sources)
    else:
        print "No data sets specified."


if __name__ == '__main__':
    main()
