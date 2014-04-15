#!/usr/bin/env python

data_sets = {
    "grads1":
    {
        'url': "http://www.cde.ca.gov/ds/sd/sd/filesgrads.asp",
        'href_pattern': "",
        'inner_pattern': r"grads\d\d"
    },
    "grads2":
    {
        'url': "http://www.cde.ca.gov/ds/sd/sd/filesgradaf.asp",
        'href_pattern': "",
        'inner_pattern': r"gradaf\d\d"
    },
    "enrolment":
    {
        'url': "http://www.cde.ca.gov/ds/sd/sd/filesenr.asp",
        'href_pattern': "",
        'inner_pattern': r"enr\d\d"
    },
    "dropouts":
    {
        'url': "http://www.cde.ca.gov/ds/sd/sd/filesdropouts.asp",
        'href_pattern': "",
        'inner_pattern': r"dropouts\d\d"
    },
    "staffassignments":
    {
        'url': "http://www.cde.ca.gov/ds/sd/df/filesassign.asp",
        'href_pattern': "",
        'inner_pattern': r"assign\d\d|staffassign\d\d"
    },

    "SchoolList": "ftp://ftp.cde.ca.gov/demo/schlname/pubschls.txt",
    "CourseList": "ftp://ftp.cde.ca.gov/demo/paif/asgncode.txt"
    }
