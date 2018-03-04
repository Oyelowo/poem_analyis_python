# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 08:30:12 2018

@author: Oyedayo Oyelowo
email: oyelowo.oyedayo@helsinki.fi, oyedayooyelowo@gmail.com
Description: This script contains the solution to the first task. It also shows
             how to use the funtions in "poempy" module under the package "text_analysis"

NOTE: MAKE SURE YOUR WORKING DIRECTORY IS SET TO THE FOLDER WHERE THE MODULE IS!
e.g C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_data_analyst
Alternatively, you can use the script commented out immediately below to do this automatically.
"""

# =============================================================================
#  #USE THIS TO AUTOMATICALLY SET THE  WORKING DIRECTORY TO WHERE 'poempy' MODULE IS.
# import os
# DIR_PATH = os.path.dirname(os.path.realpath('__file__'))
# for dirpath, dirnames, filenames in os.walk(DIR_PATH):
#     for dirname in dirnames:
#         if dirname == "text_analysis":
#             os.chdir(dirpath)
# =============================================================================

import os
#import the module that will be used for analysing the poem.
from text_analysis import poempy as pm

#NOTE: Change the filepath to the poem's filepath!
FILEPATH = os.path.join(os.getcwd(), "POEM_RAW.txt")

#read the poem. the encoding is used because of the special characters in finnish.
POEM_DATA = pm.read_text(FILEPATH, strip_title="Kahdesviidettä runo", encoding="ISO-8859-1")

#get the top 100 words by count and also their average waiting time.
TOP_100_WORDS = pm.top_words_df(data=POEM_DATA)
print(TOP_100_WORDS)

#export data
pm.write_data(dataframe=TOP_100_WORDS, filename="TOP100_WORDS_BY_COUNT", sep="\t")
