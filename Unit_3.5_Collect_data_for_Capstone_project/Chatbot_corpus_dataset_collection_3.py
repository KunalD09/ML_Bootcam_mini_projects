#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import spacy
import unidecode
from word2number import w2n
import contractions
import os
import re
import yaml
import string


# In[2]:


os.chdir("C:\\Users\\kdoshi\\OneDrive - Qualcomm\\Documents\\UCSD\\chatbot_dataset\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english")


# In[4]:


os.getcwd()


# In[5]:


with open("conversations_copy.yml", "r") as stream:
    dict_loaded = yaml.safe_load(stream)
print(dict_loaded["conversations"])


# In[6]:


print(dict_loaded['conversations'][3])


# In[7]:


from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from matplotlib import pyplot as plt
from collections import Counter
# Split scene_one into sentences: sentences
# sentences = [sent_tokenize(line) for line in dict_loaded]

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = [word_tokenize(word) for word in dict_loaded['conversations'][3]]

print(tokenized_sent)
# Make a set of unique tokens in the entire scene: unique_tokens
#unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
#print(unique_tokens)


# In[8]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sb


# In[13]:


lines = dict_loaded['conversations'][0]
print(lines)
print("-----------------------------------------")
my_list = []
#word_split = line.split()
#print(word_split)
for line in lines:
    tokenized_sent = word_tokenize(line)
    #print(tokenized_sent)
    for word in tokenized_sent:
        my_list.append(word)

print(my_list)
bow_simple = Counter(my_list)
print(bow_simple)

#sb.distplot(my_list,kde = False)
#plt.show()
#plt.hist(bow_simple)
plt.hist(my_list, width = 0.5, color='#0504aa',alpha=1)
# Show the plot
plt.show()


# In[26]:


for conversation in dict_loaded['conversations']:
    print(conversation)
    my_list = []
    word_split = []
    #sentence = sent_tokenize(conversation)
    #print(sentence)
    for line in conversation:
        print(line)
        #word_split = line.split()
        #print(word_split)
        tokenized_sent = word_tokenize(line)
        print(tokenized_sent)
        for word in tokenized_sent:
            my_list.append(word)
        print(my_list)
    bow_simple = Counter(my_list)
    plt.hist(bow_simple)
    # Show the plot
    plt.show()


# In[6]:


my_list = []
for i in dict_loaded["conversations"]:
    #print(i)
    for element in i:
        lower_case_ele = element.lower()
        #print(lower_case_ele)
        contractions_fix_data = contractions.fix(lower_case_ele)
        #print(contractions_fix_data)
        my_list.append(contractions_fix_data)
print("my_list = ",my_list)


# In[ ]:




