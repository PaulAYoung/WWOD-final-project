WWOD-final-project
===================

This is my final project for working with open data spring 2014. 

Setup
==================
Requirements can be installed by running `pip install -r requirements.txt`.
<<<<<<< HEAD
Data can be downloaded from the California Department of Education by running
`python get-cal-ed-data.py`. Some of these data files (the .exe files) need to be extracted on *nix machines you can just run `unzip data/*.exe`on *nix machines you can just run `unzip data/*.exe` You can combine data from different years by running `python ed-data-compile.py`.
=======

Data used in analysis is downloaded using one of the get-....py scripts and combined together using the combine....py scripts. These scripts respectively download data files and combine datafiles that are all part of one data set (usually when there are different files for different years of the same data). 

Some of the files downloaded are .exe files. These are zip files and will need to be unzipped before the combine step. On linux, I have used `unzip data/*.exe` to unzip these all at once. 
>>>>>>> 0c154c9daac4f724197f9aff0b0f0e58960e6a22
