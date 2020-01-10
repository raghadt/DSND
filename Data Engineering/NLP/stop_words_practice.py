#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download('punkt')
nltk.download('stopwords')


# # Stop Words
# Combine the steps you learned so far to normalize, tokenize, and remove stop words from the text below.
# 
# **Note: All solution notebooks can be found by clicking on the Jupyter icon on the top left of this workspace.**

# In[2]:


# import statements
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[13]:


text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war ? Is AI a bad thing ?"
print(text)


# In[16]:


# Normalize text
text = re.sub(r"[^a-zA-Z0-9]"," ",text.lower())


# In[17]:


# Tokenize text
words = word_tokenize(text)
print(words)


# In[18]:


words = [w for w in words if w not in stopwords.words("english")]
print(words)


# Take a look at the stop words included in nltk's corpus!

# In[19]:


print(stopwords.words("english"))


# In[ ]:




