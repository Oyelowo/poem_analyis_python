# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 08:30:12 2018

@author: Oyedayo Oyelowo
email: oyelowo.oyedayo@helsinki.fi, oyedayooyelowo@gmail.com
Description: This script contains the solution to the first task. It also shows 
             how to use the funtions in "poempy" module under the package "text_analysis"

NOTE: MAKE SURE YOUR WORKING DIRECTORY IS SET TO THE FOLDER WHERE THE MODULE IS!
e.g C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_data_analyst
There is also a script commented out immediately below to do this automatically.
"""

# =============================================================================
#  #For automatically setting the working directory to where the module is.
# import os
# DIR_PATH = os.path.dirname(os.path.realpath('__file__'))
# for dirpath, dirnames, filenames in os.walk(DIR_PATH):
#     for dirname in dirnames:
#         if dirname == "text_analysis":
#             os.chdir(dirpath)
# =============================================================================

from text_analysis import poempy as pm

#read filepath.NOTE: Change the filepath to your filepath!
FILEPATH = "C:/Users/oyeda/Desktop/POEM_RAW.txt"

###################################################################################
#MAIN FUNCTIONS
#read data
POEM_DATA = pm.read_text(FILEPATH, strip_title="Kahdesviidettä runo")

#get the top 100 words by count and print
TOP_100_WORDS = pm.top_words_df(data=POEM_DATA)
print(TOP_100_WORDS)

#export data
pm.write_data(dataframe=TOP_100_WORDS, filename="TOP100_WORDS_BY_COUNT", sep="\t")


####################################################################################
#OTHER MINOR FUNCTIONS
#get some stats about the text
pm.text_stat(data=POEM_DATA, word_time=1, line_time=2, chapter_time=6)


#get the list of the words.
WORLD_LIST = pm.words_list_lower(data=POEM_DATA)
print(WORLD_LIST)

#Get the time delta time as a list, considering that every new word takes
#1 h, every new line takes 2 h and every new chapter takes 6 h to get to.
T_DELTA_LIST = pm.delta_time_list(data=POEM_DATA, word_time=0.2, line_time=0.5, chapter_time=1)
print(T_DELTA_LIST)

#include the time exis after every word in the poem
POEM_TIME_AXIS = pm.words_time_str(data=POEM_DATA)
print(POEM_TIME_AXIS)

#create a dictionary with words as the keys and each key with its corresponding,
#delta time.
WORDS_DT_DICT = pm.words_time_dict(POEM_DATA)
print(WORDS_DT_DICT)

#create a dataframe from the text, which includes variables such as: the words,
#their count/freauency and average waiting time.
WORDS_UNSORTED = pm.unsorted_words_df(POEM_DATA)
print(WORDS_UNSORTED)
