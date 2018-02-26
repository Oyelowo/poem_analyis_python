"""
Created on Sat Feb 24 06:48:04 2018

@author: Oyedayo Oyelowo
email: oyelowo.oyedayo@helsinki.fi, oyedayooyelowo@gmail.com
Title :Text Analysis
Note : This module was created to analyse a poem but can be used for other
        articles too. It mainly performs the below functions:
        1. Read the text with option of deleting the title
        2. creating a list of words in the text.
        3. creating a list of time difference(delta) time between words, when reading.
        4. introuces time axis to the text.
        5. create and export a dataframe with all the words in the poem. Each word
            has its frequency of occurence and average waiting distance. Average waiting
            distance is the average time between occurences of same word.
        6. these dataframe can also be sorted in ascending or descending order,
            according to the frequency(count) or average waiting time.
        7. it can also create dictionary with each word as a key and its cumulative time
            as the value.
"""
#import necessary modules
import os
from collections import defaultdict
import pandas as pd
import numpy as np


def read_text(filepath, strip_title=None):
    """
    This reads the text, with the option of deleting the title.
    Arguments:
        filepath : the filepath of the text to be read.
        strip_title : default value is None. If the title is included as a string,
        it will be deleted from the text.
    Example:
        read_text(filepath = 'C:/Users/oyelowo/poem.txt, strip_title='Kahdesviidettä runo')
    """
    with open(filepath, 'r') as file:
        text = file.read()
#    if the title is included as argument
    if strip_title:
#        delete the title
        text = text.lstrip(strip_title)
    return text


def words_list_lower(data):
    """This creates list of words from the text in lowercase.
    Argument:
        data : this should be an imported file containing the texts.
    Example:
        words_list_lower(data = data)
    """
#    Convert the text to lowercase and get the list of words from it.
    return data.lower().split()


def delta_time_list(data, word_time=1, line_time=2, chapter_time=6):
    """
    This creates a list of the time difference between all the words in the text.
    The default delta time or time change between words, lines and chapters/paragraph,
    can be changed by user. This flexibility allows user to increase or reduce time cost
    of reading because speed of reading varies amongst people.
    Arguments:
        data : the data with the texts.
        word_time : the time it takes to get to the next word. Default value is 1.
        line_time : the time it takes to get to the next line. Default value is 2.
        chapter_time : the time it takes to get to the next Chapter or paragraph.
                        Default value is 6.
    Example:
        delta_time_list(data=data, word_time=1, line_time=2, chapter_time=6)
    """
#convert the the text into lower case. This is to avoid problems with uppercase and lowercase
    text_lower = data.lower()
#    set the initial time of the text.
    delta_time = 1
#    create a list with initial time.
    dt_list = [delta_time]
#    this is used in the loop to avoid getting the last lement.
    last_element = 1
#    iterate over all the chapters in the text and get the indexes and each chapter.
    for index_chp, chapter in enumerate(text_lower.split("\n\n")):
#   also, iterate over all the lines in each chapter and get the indexes and each line.
        for index_ln, line in enumerate(chapter.split("\n")):
#   also, iterate over all the words in each line and get the indexes of each word.
            for index_wd in range(len(line.split())):
# avoid the last word in a line by excluding it from the word delta time calculation the line
                if index_wd < len(line.split()) - last_element:
#                    increase the the change it time as one reads through the text
                    delta_time += word_time
#                    append the delta time to a list
                    dt_list.append(delta_time)
#The following lines follow thesame logic from line to chapters
            if index_ln < len(chapter.split("\n")) - last_element:
                delta_time += line_time
                dt_list.append(delta_time)
        if index_chp < len(text_lower.split("\n\n")) - last_element:
            delta_time += chapter_time
            dt_list.append(delta_time)
    return dt_list


def words_time_str(data):
    """
    This includes the time axis into the text, based on the time weight on
    new words, new lines and new chapters.
    Arguments:
        data : the data with the texts.
    Example:
        words_time_str(data=data)

    """
#    get all the delta time list
    dt_list = delta_time_list(data)
#    get the list of  words
    w_list = words_list_lower(data)
# The position of each word corresponds with the cumulative time cost(or time axis) above.
#get the words and delta time.
    words_time = ["{0}: t_{1}".format(w, dt) for w, dt in zip(w_list, dt_list)]
#    convert the list into string and remove the brackets from the list
    wt_str = str(words_time).strip("[]")
    return wt_str


def words_time_dict(data):
    """
    This creates a dictionary for each word as the key and their corresponding time_cost
    #as the values
    Arguments:
        data : the data with the texts.
    Example:
        words_time_dict(data=data)
    """
#   get all the delta time list above
    dt_list = delta_time_list(data)
#    get the list of all corresponding words
    word_list = words_list_lower(data)
#create an empty dictionary which allows each to take in value as list for all the points
#where the key reoccurs.
    wt_dict = defaultdict(list)
#iterate through the combined the list of words(key) and their corresponding delta time(value).
    for key, value in zip(word_list, dt_list):
#append the delta time(value) in every point the word(key) reoccurs in the list.
        wt_dict[key].append(value)
    return wt_dict


def unsorted_words_df(data):
    """
    This creates a dataframe which includes all the words, their count and
    average waiting time.
    Arguments:
        data : the data with the texts.
    Example:
        unsorted_words_df(data=data)
    """
#    get the dictionary which includes all the words and their corresponding delta times.
    wt_dict = words_time_dict(data)
#    Create an empty dataframe where the variables will be included.
    output_data = pd.DataFrame()
#  get the indexes, the words(key) and value(delta times) by iterating through
#the dictionary items
    for i, (key, value) in enumerate(wt_dict.items()):
#        print the progress
        print('Processing {0}.......{1}/{2}'.format(key, i+1, len(wt_dict)))
#insert the words and their counts by using key(word) and the length of the
#(delta time) which is equivalent to the cout.
        output_data.loc[key, 'words'], output_data.loc[key, 'count'] = key, len(value)
# insert average waiting time as 0 if the word occurs just once.
        if len(value) < 2:
            output_data.loc[key, 'avg_wait_time'] = 0
        else:
#if it occurs more than once, calculate the average of the cumulative difference
# of the delta time(value) and insert as the average waiting time.
            output_data.loc[key, 'avg_wait_time'] = np.mean(np.diff(value))
    return output_data.reset_index(drop=True)



def top_words_df(data, rank_words=100):
    """
    This creates a dataframe with the top 100 words by count by default. Number of words
    to be ranked can also be increased.
    Arguments:
        data : the data with the texts.
        rank_words : the number of words you want to rank.
    Example:
        top_words_df(data=data, word_time=1, line_time=2, chapter_time=6)
    """
#        get the unsorted dataframe with words, count and average waiting time.
    words_df = unsorted_words_df(data)
#       sort the dataframe by the variable name
    words_df = words_df.sort_values(by='count', ascending=False)
#depending on user, take the top/bottom number of sorted rows by count or avg_wait_time.
    words_df = words_df[0:rank_words]
    return words_df.reset_index(drop=True)


def export_data(dataframe, myfolder=None, filename='Output', sep=";", file_format=".txt"):
    """
    This exports the dataframe.
    Arguments:
        myfolder : the folder path you wish to write the data to.
        filename : the name of file you wish to use for the data.
            sep :  separator of dataframe to be exported(e.g ';', '\t', ',')
        file_format : format of the output dataframe(e.g '.txt', '.csv')
    Example:
        export_data(dataframe=data, myfolder=C:/Users/oyelowo/poem.txt,
                    filename='poem', sep=";",file_format=".txt")

    """
    filepath = os.path.join(myfolder, filename + file_format)
    dataframe.to_csv(filepath, sep)
