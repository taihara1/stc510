#!/usr/bin/env python
# coding: utf-8

# **Project 4 Essentials** 
# 
# **Learning Goal:** Selenium & Beautiful Soup 
# 
# **Project Directions:** "Write a Python script that, when executed, detects any mentions of a particular keyword on Gab, Parler, Telegram, or MeWe, or similar, and stores these to a report." 
# 
# **Program Goal:** Use GAB to find posts/discussion with the following key words: "fries, ingredients, recipe, healthy, and good." Post the findings on a csv file. For privacy reasons, the username (who posted) and url were not included. 
# 
# **Script Disclaimer:** Checking the First 10 "New" Posts. For Educational Purposes **ONLY** 

# In[9]:


from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import project4_info #WILL NOT RUN UNLESS YOU ENTER OWN CREDENTIALS! 


# **Selenium:** The following section of code is to establish a Chrome Web Driver. Inside selenium's webdriver is the path of where the downloaded file is. For security and privacy reasons, the information is located on a separated file.

# In[10]:


browser = webdriver.Chrome(project4_info.path)
sleep(10)


# The next block of code are the steps to open the GAB sign in page, using the **get** method. Using the **find element** method and speification (name, id) will allow the web driver locate the areas needed to input the log-in credentials. The **send keys** method will input the str into the field. The **click** method imitates the actions of a mouse click. Lastly the **find element by link text** is a method that finds the parameter on the page. Since I had a difficult time finding the "Groups" HTML tag, this was an easier althernative to use. 
# 
# **Note:** It is important to include sleeps in-between every action ^ . ^ 

# In[11]:


login_page = 'https://gab.com/auth/sign_in'

browser.get(login_page)
sleep(20)

log_form = browser.find_element_by_id('user_email').send_keys(project4_info.user) 
sleep(20)

log_pass = browser.find_element_by_id('user_password').send_keys(project4_info.password) 
sleep(20)

pass_button = browser.find_element_by_name('button').click() 
sleep(20)

group = browser.find_element_by_link_text('Groups')
sleep(5)
group.click() 

sleep(40)

page = browser.page_source


# **Beautiful Soup:** After getting the page source from the current page, it was put into Beautiful Soup's html parser. The next few lines are similar to the first project since it had similar goals. 

# In[12]:


bs = BeautifulSoup(page, 'html.parser')


# In[13]:


def check_keyword(post: 'post text', list_words: 'list of words'): 
    #Returns a string of the keywords or an empty str if there's no match 
    posts = post.lower() 
    result = '' 
    for every_word in list_words: 
        if every_word.lower() in post: 
            result += every_word + ','
    return result 


# **Keywords:** I changed the keywords to be food-related than mattress/moving related. There wasn't much activity with words from the Basic Project, so I wanted to choose a group page with hourly posts. 

# In[14]:


posts = bs.find_all('div', class_='SslQJ _2tTSp') 
keywords = ['fries', 'ingredients', 'recipe', 'healthy', 'good']
final = {'Keyword': [], 'Post Title': [], 'Posted': []}
count = 0


# **Note**: I could have put this for-loop into a function...

# In[15]:


time = bs.find_all('time')


# In[16]:


for post in posts[:10]: 
    sleep(5) 
        
    if check_keyword(post.text, keywords) != '': 
        sleep(10)
        final['Keyword'].append(check_keyword(post.text, keywords))
        final['Post Title'].append(post.text)
        final['Posted'].append(time[count]['title'])
    
    count += 1 
    print('Completing Result # ' + str(count))

browser.quit()
df = pd.DataFrame(final)
df.to_csv('gab_cooking.csv') 
print('\nFile Complete')
        


# In[17]:


#browser.quit()

