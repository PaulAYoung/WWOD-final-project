WWOD-final-project
===================

This is my final project for working with open data spring 2014. 

Setup
==================
Requirements can be installed by running `pip install -r requirements.txt`.

Data is downloaded using `python geteddata.py`. This will pull data from the California Department of Education. If there is an error, there will b a prompt to see if you want to retry.

Some of the files downloaded are .exe files. These are zip files and will need to be unzipped before the combine step. On linux, I have used `unzip data/*.exe` to unzip these all at once. 

Once the data is downloaed and unzipped, you can combine data files from different years by running `python compiledata.py`. 
