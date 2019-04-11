#!/usr/bin/env python
# coding: utf-8

# In[8]:


import json
import pandas as pd
from pprint import pprint
import numpy as np
from datetime import datetime


# In[21]:


data = pd.read_csv('output_table_final_version.csv',encoding = "ISO-8859-1")
data.head()


# In[17]:


data.info()


# In[34]:


year_book=data.groupby("last_year",as_index=False).count()
year_book


# In[31]:


year_book_avg=data.groupby("last_year",as_index=False).mean()
year_book_avg


# In[45]:


year_book_avg["count"]=year_book["title"]
year_book_avg


# In[56]:


year_book_data=year_book_avg[["last_year","weeks_on_list","Amazon_reviews","Amazon_rating","Amazon_price"]]
year_book_data.rename(columns={'last_year':'book_count',
                          'weeks_on_list':'weeks_on_list_avg',
                          'Amazon_reviews':'Amazon_reviews_avg',
                           'Amazon_rating':'Amazon_rating_avg',
                              'Amazon_price':'Amazon_price_avg'}, 
                 inplace=True)
year_book_data.round(2)


# In[57]:


year_book_data.round(2).to_csv('NYTBestseller_YearAsVariable.csv')


# In[ ]:




