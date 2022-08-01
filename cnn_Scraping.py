#!/usr/bin/env python
# coding: utf-8

# # Automatic Scrape of CNN's Climate News
# 
# https://www.cnn.com/specials/world/cnn-climate
# 

# In[20]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[21]:


response = requests.get("https://www.cnn.com/specials/world/cnn-climate")
doc = BeautifulSoup(response.text)


# In[23]:


# Grab all of the headline titles
# Make sure to just copy paste from the website .media__title 
titles = doc.select(".cd__headline")
titles


# In[47]:


titles[0].a['href']


# In[24]:


for title in titles:
    print(title.text.strip())


# In[37]:


url = doc.select(".cd__headline a")
url


# In[48]:


# Start with an empty list
rows = []

for title in titles:
    # Go through each title, building a dictionary
    # with a 'title' and a 'url'
    row = {}
    
    # title
    row['title'] = title.text.strip()
     # link
    row['url'] = title.a['href']
    
    # Then add it to our list of rows
    rows.append(row)

# then we're going to make a dataframe from it!!!
df = pd.DataFrame(rows)
df.head()


# In[49]:


df.to_csv("cnn.csv", index=False)


# In[ ]:




