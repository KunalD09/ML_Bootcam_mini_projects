#!/usr/bin/env python
# coding: utf-8

# In[6]:


import googletrans


# In[7]:


import os

os.getcwd()
path = 'C:\\Users\\kdoshi\\OneDrive - Qualcomm\\Documents\\UCSD\\chatbot_dataset\\preprocessed\\evaluation_metric\\demo_data'
os.chdir(path)
os.getcwd()


# In[17]:


import json

from googletrans import Translator

translate = Translator()
tweets = []
for line in open('pred.json', 'r', encoding='utf8'):
    new_line = line.strip()
    #print(new_line)
    #print(type(new_line))
    result = translate.translate(new_line,dest='en')
    tweets.append(result.text)
    #print(result.text)
    
print(tweets)


# In[ ]:




