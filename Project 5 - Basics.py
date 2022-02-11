#!/usr/bin/env python
# coding: utf-8

# **Project 5 Basic:** Tiffany Aihara
# 
# **Directions:** Parse, clean, and organize the Jeopardy! question data file to train a Naive Bayesian classifier.
# 
# **Goal:** "Just as we have built a classifier above, your aim here is to make sense of the data presented and create a binary classifier ("high value" and "low value," based on the points available for each) for questions.

# **Helpful:** https://www.simplilearn.com/tutorials/machine-learning-tutorial/naive-bayes-classifier?source=sl_frs_nav_playlist_video_clicked

# **Part 1: Collecting & Cleaning Data** To open the file, I imported json in order to read it. The file holds a list of individual dictionaries (for each question) with the keys of show number, air date, answer, question, value, and round. For this classifier, I decided to drop the show number, air date, answer, and question as the goal is to look at the point values.

# In[1]:


import pandas as pd 
import json
from string import punctuation 
import re

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB 
from sklearn.metrics import accuracy_score 


# In[2]:


filepath = '' #INSERT PATH OF THE JSON FILE!
file = open(filepath)
data = json.load(file)


# In[3]:


df = pd.DataFrame(data)
#filtered = df.drop(columns = ['show_number', 'air_date', 'answer', 'question'])


# In[4]:


def remove_punctuation(word): 
    #Removes punctuation & returns just the word 
    word = word.lower() 
    new_word = re.sub('[^A-Za-z0-9\s]', '', word)
    return new_word

def edit_str(word): 
    #Remove the value ($) puncts 
    new_word = word[1:]
    if punctuation[11] in new_word: 
        new_word = new_word.replace(punctuation[11], ' ')
        new = word[1:].strip(' ')
    else: 
        new_word = new_word
    return new_word


# In[5]:


df['clean_category'] = df['category'].apply(remove_punctuation)
df['clean_round'] = df['round'].apply(remove_punctuation)


# In[6]:


newdata = df.dropna(axis = 0, how ='any')
newdata['clean_value'] = newdata['value'].apply(edit_str)


# In[12]:


newdata = newdata.drop(columns = ['category', 'answer', 'question', 'show_number', 'round', 'value'])


# In[13]:


newdata.head()


# **Part 2: Creating Vectors & Binary Classifier** The testdata will include 10,000 responses from the filtered dataframe (the removed colums). The *value_matrix* is the binary classifier to determine whether a value is "high" or "low" (Low 0/High 1). 

# In[16]:


vector = CountVectorizer() 

#testdata = (filtered)

#0 = less than 1000 #1 over 1000 
value_matrix = [1 if int(x.replace(' ', '')) >= 1000 else 0 for x in newdata['clean_value']] 


# **Part 3: Naives Bayes** Looking at the likelihood of a low value question ("easy"). Since the file holds a lot of data, I decided to look at only 10,000 individual dictionaries. 

# In[18]:


values = [' '.join([x.lower()]) for x in newdata['clean_value']]


# In[25]:


testing_df = pd.DataFrame({'valuetype': values[:10000], 'high_low': value_matrix[:10000]})


# In[26]:


x_train, x_test, y_train, y_test = train_test_split(testing_df.valuetype, testing_df.high_low, random_state=1)


# In[27]:


tfidf_vectorizer = TfidfVectorizer(use_idf = True)
X_train_tf = tfidf_vectorizer.fit_transform(x_train)
X_test_tf = tfidf_vectorizer.transform(x_test)


# In[28]:


naives_bayes = MultinomialNB() 
naives_bayes.fit(X_train_tf, y_train)
predictions = naives_bayes.predict(X_test_tf)


# In[29]:


predictions 


# **Note:** The classifier is no where "accurate" to where it aligns with the project's intital goal. 

# In[30]:


print('Accuracy: ', accuracy_score(y_test, predictions)) 

