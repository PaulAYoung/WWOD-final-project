#!/usr/bin/env python

import os
import re
import urllib2

import requests
from bs4 import BeautifulSoup


def download_file(url, outpath):
    """Downloads given url to given path"""
    print "downloading {} to {}".format(url, outpath)

    # get file
    data = urllib2.urlopen(url)

    # determine extention
    # content disposition has the intended filname
    # splits out the extension so it can be added to the file
    file_info = data.headers.getheader("content-disposition")
    if file_info:
        ext = os.path.splitext(file_info)[-1]
    else:
        ext = os.path.splitext(url)[-1]

    #write file
    outpath = outpath + ext
    outfile = open(outpath, "wb")
    outfile.write(data.read())


def mass_downloader(url, href_pattern=False, inner_pattern=False):
    """
    Scrapes a page and downloads all files that match given patterns
    href_pattern - pattern to match within link
    inner_pattern - pattern to match in inner html
    e.g:
    <a href="href_pattern">inner_pattern</a>
    """
    #get page and beautify
    page = requests.get(url)
    soup = BeautifulSoup(page.content)

    # go through links and apply search patterns
    for link in soup.find_all('a'):
        get_flag = True
        href = link.get('href')
        if not href:
            href = ""
        inner = link.getText()
        if not inner:
            inner = ""
        print "Checking {}".format(link)
        if href_pattern:
            matchobj = re.search(href_pattern, href)
            if not matchobj:
                get_flag = False
        if get_flag and inner_pattern:
            matchobj = re.search(inner_pattern, inner)
            if not matchobj:
                get_flag = False
        if get_flag:
            # download file
            outpath = os.path.join("data", inner)
            download_file(href, link.get(href, outpath))
