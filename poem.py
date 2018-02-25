"""
Created on Sat Feb 24 06:48:04 2018

@author: Oyedayo Oyelowo
"""
#Getting the document directly online
from collections import defaultdict
import pandas as pd
import numpy as np
import os

def read_text(filepath, strip_title=None):
    """read_poem"""
    #READING FROM THE USER DIRECTORY
    with open(filepath, 'r') as file:
        text = file.read()
    if strip_title:
        text = text.lstrip(strip_title)
    return text


def words_list(text_data):
    #Get the list of words from the Poem
   return text_data.lower().split()
    

def delta_time_list(text_data, initial_time = 1, word_time=1, line_time=2, chapter_time=6):
    """delta_time"""
    #CONVERT THE CONTENT TO LOWERCASE
    text_lower = text_data.lower()
    delta_time_list = []
    time_cost = initial_time
    delta_time_list.append(time_cost)
    last_element = 1
    for index_chp, chapter in enumerate(text_lower.split("\n\n")):
        for index_ln, line in enumerate(chapter.split("\n")):
            for index_wd in range(len(line.split())):
                if index_wd < len(line.split()) - last_element:
                    time_cost += word_time
                    delta_time_list.append(time_cost)
            if index_ln < len(chapter.split("\n")) - last_element:
                time_cost += line_time
                delta_time_list.append(time_cost)
        if index_chp < len(text_lower.split("\n\n")) - last_element:
            time_cost += chapter_time
            delta_time_list.append(time_cost)
    return delta_time_list


###############################################################################
def words_time_str(text_data):
    dt_list = delta_time_list(text_data)
    w_list = words_list(text_data)
    #The position of each word corresponds with the cumulative time cost(or time axis) above
    words_time = ["{0}: t_{1}".format(w, dt) for w, dt in zip(w_list, dt_list)]
    words_time_str = str(words_time).strip("[]")
    return words_time_str

def words_time_dict(text_data):
    """#Create a dictionary for each word as the key and their corresponding time_cost
    #as the value"""
    dt_list = delta_time_list(text_data)
    w_list = words_list(text_data)
    wt_dict = defaultdict(list)
    for key, value in zip(w_list, dt_list):
        wt_dict[key].append(value)
    return wt_dict

def words_count_awt_df(text_data, myfolder=None, filename='Output', sep=";", \
                       file_format=".txt"):
    
    wt_dict = words_time_dict(text_data)
    #Create an empty dataframe.
    output_data = pd.DataFrame()
    for i, (key, value) in enumerate(wt_dict.items()):
        print('Processing {0}.......{1} out of{2}'.format(key, i+1, len(wt_dict)))
        output_data.loc[key, 'words'], output_data.loc[key, 'count'] = key, len(value)
        if len(value) < 2:
            output_data.loc[key, 'avg_tm'] = 0
        else:
            output_data.loc[key, 'avg_tm'] = np.mean(np.diff(value))
    if myfolder is not None:
        filepath = os.path.join(myfolder, filename + file_format)
        output_data.to_csv(filepath, sep)  
    return output_data
