#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
from bs4 import BeautifulSoup
import requests



page = requests.get("http://convai.io/data/summer_wild_evaluation_dialogs.json")
soup = BeautifulSoup(page.content, 'html.parser')


# In[2]:


import pandas as pd

df = pd.read_json("http://convai.io/data/summer_wild_evaluation_dialogs.json")
df


# In[3]:


import os
os.getcwd()


# In[4]:


os.chdir("C:\\Users\\kdoshi\\OneDrive - Qualcomm\\Documents\\UCSD\\mec-mini-projects-master")


# In[5]:


df.to_csv("content.csv")


# In[62]:


my_list = []
incr=0
for row in df['dialog'].iteritems():
    #print('row[0] = ',row[0])
    #print('row[1] = ',row[1])
    #print('i = ',i)
    #print(type(i))
    for val in row[1]:
        #columns=['id','sender','text','sender_class']
        new_df = pd.DataFrame(val,index=[incr])
        incr=incr+1
        #new_df.swapaxes('index','columns')
        #print(new_df)
        my_list.append(new_df)

final_new_df = pd.concat(my_list)


# In[63]:


print(final_new_df)


# In[64]:


final_new_df.to_csv('new_df.csv')


# In[65]:


os.getcwd()


# In[ ]:




