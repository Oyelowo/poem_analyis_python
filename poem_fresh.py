"""
Created on Sat Feb 24 06:48:04 2018

@author: Oyedayo Oyelowo
"""



#Getting the document directly online
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from collections import Counter

#READING DIRECTLY FROM THE HTML PAGE
FILE = urllib.request.urlopen("http://runeberg.org/kalevala/42.html")
DOCUMENT = bs(FILE.read()).get_text()
START = DOCUMENT.find('Kahdesviidettä runo')
END = DOCUMENT.find('Project Runeberg,')
POEM = DOCUMENT[START:END]


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

#The position of each word corresponds with the cumulative time cost above
words_list = POEM_BODY_LOWERCASE.split() 
#Create an empty dataframe.
WORDS_DATA_s=pd.DataFrame()
Counter(words_list)
letter_index=[]
for i, element in enumerate(words_list):
    print("Processing Word....{0}/{1}.".format(i + 1 , len(words_list)))
    WORDS_DATA_s.loc[i, 'words'] = element
    WORDS_DATA_s.loc[i, 'count'] = words_list.count(element)
    #get the list of positions where each alphabet occured
    letter_list=[idx for idx, letter in enumerate(words_list) if letter==element] 
    if len(letter_list) > 1:
        delta_time_list=[]
        for value in range(len(letter_list)):
            if value + 1 < len(letter_list):
                time1,time2 = letter_list[value] , letter_list[value + 1]
                delta_time = time2 - time1
                delta_time_list.append(delta_time)
            WORDS_DATA_s.loc[i, 'Average_wt_time']=np.mean(delta_time_list)
    else:
        WORDS_DATA_s.loc[i, 'Average_wt_time'] = 0
        
        

grouped = WORDS_DATA_s.groupby('words')
WORDS_DATA_GROUPED=grouped['count','Average_wt_time'].agg([np.unique]).reset_index()
WORDS_DATA_GROUPED.columns=WORDS_DATA_GROUPED.columns.droplevel(1)
WORDS_DATA_GROUPED.sort_values(by='count', ascending=False)


    
    
