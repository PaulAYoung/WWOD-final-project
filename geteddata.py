#!/usr/bin/env python

import sys

from datascrape import mass_downloader, download_file

data_sources = [
    {
        'url': "http://www.cde.ca.gov/ds/sd/sd/filesgrads.asp",
        'href_pattern': "",
        'inner_pattern': r"grads\d\d"
    },
    {
        'url': "http://www.cde.ca.gov/ds/sd/sd/filesgradaf.asp",
        'href_pattern': "",
        'inner_pattern': r"gradaf\d\d"
    },
    {
        'url': "http://www.cde.ca.gov/ds/sd/sd/filesenr.asp",
        'href_pattern': "",
        'inner_pattern': r"enr\d\d"
    },
    {
        'url': "http://www.cde.ca.gov/ds/sd/sd/filesdropouts.asp",
        'href_pattern': "",
        'inner_pattern': r"dropouts\d\d"
    }
    ]


def get_data(sources):
    for source in sources:
        print source
        mass_downloader(**source)


def main():
    args = sys.argv
    if len(args) == 1:
        data = data_sources[int(args[0])]
    elif len(args) == 2:
        data = data_sources[int(args[0]):int(args[1])]
    else:
        data = data_sources

    get_data(data)
    #download list of public schools
    download_file(
        "ftp://ftp.cde.ca.gov/demo/schlname/pubschls.txt",
        "pubschls",
        retry=True
        )


if __name__ == '__main__':
    main()
