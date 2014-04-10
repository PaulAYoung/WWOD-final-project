#!/usr/bin/env python

import os
import re
import urllib2
from time import sleep

import requests
from bs4 import BeautifulSoup


def confirm(msg):
    """prints message and asks for y/n response"""
    while 1:
        resp = raw_input(msg)
        if resp in ["y", "Y", "yes", "Yes"]:
            return True
        elif resp in ["n", "N", "no", "No"]:
            return False
        else:
            continue


def download_file(url, outpath, retry=False):
    """
    Downloads given url to given path
    the retry parameter catches exceptions and asks if the user would like
    to retry
    """
    print "downloading {} to {}".format(url, outpath)

    #get file, if there is an error, ask if we want to confirm
    while 1:
        try:
            data = urllib2.urlopen(url)
        except Exception as e:
            print "Exception caught while downloading {}".format(url)
            print str(e)
            if retry and confirm("Retry? (y/n)"):
                continue
            else:
                raise
        finally:
            break

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


def mass_downloader(
        url,
        href_pattern=False,
        inner_pattern=False,
        wait=0.05,
        retry=False
        ):
    """
    Scrapes a page and downloads all files that match given patterns
    href_pattern - pattern to match within link
    inner_pattern - pattern to match in inner html
    wait - time to wait after a download happens
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
            download_file(href, link.get(href, outpath), retry=retry)
            sleep(wait)
