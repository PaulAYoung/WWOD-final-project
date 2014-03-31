#!/usr/bin/env python

import os
import re

import dbf
import pandas as pd


def dbf_to_df(dbf_file):
    """
    Takes a .dbf file and returns a pandas dataframe
    """
    table = dbf.Table(dbf_file).open('read-only')
    rows = []
    fields = table.field_names
    for r in table:
        row = {}
        for field in fields:
            row[field] = r[field]
        rows.append(row)
    df = pd.DataFrame(rows)
    return df


def file_matcher(path, pattern):
    """Takes path and returns list of files in path
    matching regex."""
    dir_files = os.listdir(path)
    file_list = []
    matcher = re.compile(pattern)
    for f in dir_files:
        if matcher.match(f):
            file_list.append(os.path.join(path, f))
    return file_list


def combine_datasets(
        data_dir,
        pattern,
        columns,
        columnmod=None,
        makelower=False,
        fcolumn=True,
        **kwargs
        ):
    """
    Takes data files and combines them

    arguments
    ========================

    data_dir - the directory holding the data files

    pattern - the regex pattern each imported file should match

    columns - the columns from eachfile to include in the new dataset
            - can also be 'ALL' to indicate all columns should be concacted

    columnmod - the transformation that should be applied to columns before
    function looks for columns. Should be dict where the key is the old column
    and the value is the new name - just will be passed to DataFrame.rename()

    makelower - converts all columns to be lower case before adding to new
    dataframe.

    fcolumn - adds column holding name of file called FILENAME
    """
    #get files
    file_list = file_matcher(data_dir, pattern)

    df_list = []
    for data_file in file_list:
        print data_file
        ext = os.path.splitext(data_file)[1]
        #turn file to df
        if ext.lower() == '.txt':
            df = pd.read_csv(data_file, sep="\t")
        elif ext.lower() == ".csv":
            df = pd.read_csv(data_file)
        elif ext.lower() == ".dbf":
            df = dbf_to_df(data_file)
        else:
            raise Exception("No parser for {}".format(data_file))

        #apply column transforms and create subset df
        if makelower:
            df.columns = map(str.lower, df.columns)
        if columnmod:
            df.rename(columns=columnmod, inplace=True)
        if fcolumn:
            df["FILENAME"] = data_file
        if columns == 'ALL':
            df_list.append(df)
        else:
            df_list.append(df[columns])

    final = pd.concat(df_list)
    return final
