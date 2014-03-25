#!/usr/bin/env python

from datascrape import mass_downloader

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
    get_data(data_sources)


if __name__ == '__main__':
    main()
