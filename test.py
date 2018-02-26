# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 08:30:12 2018

@author: Oyedayo Oyelowo
email: oyelowo.oyedayo@helsinki.fi, oyedayooyelowo@gmail.com
"""

import poem as pm


#read filepath
filepath = "C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_verto_data_analyst/poem.txt"

#read data
data = pm.read_text(filepath, strip_title="Kahdesviidettä runo")

TOP_100_WORDS = pm.top_words_df(data)
print(TOP_100_WORDS)

pm.export_data(dataframe=TOP_100_WORDS, 
               myfolder="C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_verto_data_analyst",
               filename="POEM_ANALYSED", sep="\t")

WORLD_LIST = pm.words_list_lower(T)

delta_time_list
words_time_str
words_time_dict
unsorted_words_df




aa = pm.words_list(a)

ab=pm.delta_time_list(a)

aq=pm.words_time_str(a)
az=pm.words_time_dict(a)
ae=pm.words_count_awt_df(a)
aab=pm.sort_words(a, by='coUnT')

__all__ = ['read_text', 'words_list', 'delta_time_list', 'words_time_str',
           'words_time_dict', 'words_count_awt_df']

ae.sort_values(by='count', ascending=False)
