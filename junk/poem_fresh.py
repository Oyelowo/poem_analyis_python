"""
Created on Sat Feb 24 06:48:04 2018

@author: Oyedayo Oyelowo
"""
#Getting the document directly online
from collections import defaultdict
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
COST_TIME_LIST = []
COST = 1
COST_TIME_LIST.append(COST)
for index_chp, chapter in enumerate(POEM_BODY_LOWERCASE.split("\n\n")):
    for index_ln, line in enumerate(chapter.split("\n")):
        for index_wd in range(len(line.split())):
            if index_wd < len(line.split())-1:
                COST += 1
                COST_TIME_LIST.append(COST)
        if index_ln < len(chapter.split("\n"))-1:
            COST += 2
            COST_TIME_LIST.append(COST)
    if index_chp < len(POEM_BODY_LOWERCASE.split("\n\n"))-1:
        COST += 6
        COST_TIME_LIST.append(COST)


###############################################################################
#Get the list of words from the Poem
WORD_LIST = POEM_BODY_LOWERCASE.split()

#The position of each word corresponds with the cumulative time cost(or time axis) above
LIST_DELTA_TIME = ["{0}: t_{1}".format(w, t) for w, t in zip(WORD_LIST, COST_TIME_LIST)]
#az = dict((el, h) for el,h in zip(WORD_LIST, COST_TIME_LIST))

#Create a dictionary for each word as the key and their corresponding time_cost
#as the value
WORDS_TIME_DICT = defaultdict(list)
for key, value in zip(WORD_LIST, COST_TIME_LIST):
    WORDS_TIME_DICT[key].append(value)


##############################################################################

#Create an empty dataframe.
WORDS_DATA = pd.DataFrame()
for i, (key, value) in enumerate(WORDS_TIME_DICT.items()):
    print('Processing {0}.......{1} out of{2}'.format(key, i+1, len(WORDS_TIME_DICT)))
    WORDS_DATA.loc[key, 'words'], WORDS_DATA.loc[key, 'count'] = key, len(value)
    if len(value) < 2:
        WORDS_DATA.loc[key, 'avg_tm'] = 0
    else:
        WORDS_DATA.loc[key, 'avg_tm'] = np.mean(np.diff(value))
   
