"""
Created on Sat Feb 24 06:48:04 2018

@author: Oyedayo Oyelowo
"""
#Getting the document directly online
import pandas as pd
import numpy as np

#READING FROM THE USER DIRECTORY
POEM_FILEPATH = "C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_verto_data_analyst/poem.txt"
POEM_OPEN = open(POEM_FILEPATH, 'r')
POEM = POEM_OPEN.read()
POEM_OPEN.close()

#REMOVE THE TITLE
POEM_BODY = POEM.lstrip('Kahdesviidettä runo\n')

#CONVERT THE CONTENT TO LOWERCASE
POEM_BODY_LOWERCASE = POEM_BODY.lower()
COST_LIST = []
COST = 1
COST_LIST.append(COST)
for i, paragraph in enumerate(POEM_BODY_LOWERCASE.split("\n\n")):
    for j, line in enumerate(paragraph.split("\n")):
        for h in range(len(line.split())):
            if h < len(line.split())-1:
                COST += 1
                COST_LIST.append(COST)
        if j < len(paragraph.split("\n"))-1:
            COST += 6
            COST_LIST.append(COST)
    if i < len(POEM_BODY_LOWERCASE.split("\n\n"))-1:
        COST += 6
        COST_LIST.append(COST)



##############################################################################
#The position of each word corresponds with the cumulative time cost above
WORD_LIST = POEM_BODY_LOWERCASE.split()
#Create an empty dataframe.
WORDS_DATA = pd.DataFrame()
for i, word_in_list in enumerate(WORD_LIST):
    print("Processing Word....{0}/{1}.".format(i + 1, len(WORD_LIST)))
    WORDS_DATA.loc[i, 'words'] = word_in_list
    WORDS_DATA.loc[i, 'count'] = WORD_LIST.count(word_in_list)
#    get the list of positions where each alphabet occured
    letter_list = [idx for idx, letter in enumerate(WORD_LIST) if letter == word_in_list]
    if len(letter_list) > 1:
        delta_time_list = []
        for value, letter in enumerate(letter_list):
            if value + 1 < len(letter_list):
                time1, time2 = letter_list[value], letter_list[value + 1]
                delta_time = time2 - time1
                delta_time_list.append(delta_time)
            WORDS_DATA.loc[i, 'Average_wt_time'] = np.mean(delta_time_list)
    else:
        WORDS_DATA.loc[i, 'Average_wt_time'] = 0

GROUPED = WORDS_DATA.groupby('words')
WORDS_DATA_GROUPED = GROUPED['count', 'Average_wt_time'].agg([np.unique]).reset_index()
WORDS_DATA_GROUPED.columns = WORDS_DATA_GROUPED.columns.droplevel(1)
WORDS_DATA_GROUPED = WORDS_DATA_GROUPED.sort_values(by='count', ascending=False)
    