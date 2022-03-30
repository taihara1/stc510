#!/usr/bin/env python
# coding: utf-8

# **Project 4 Basics: Tiffany Aihara**
# 
# **Goal:** Using Python Libraries & Beautiful Soup for **Educational Purposes ONLY**
# 
# **Directions:** "Write a Python script that, when executed once, goes to the Phoenix Craigslist site, and crawls each of the listings in the "Garage & Moving Sales" page, looking for mentions of the words above, and generates a csv that lists the keyword and the URL at which it was found." 
# 
# **Project Notes:** Terms = mattress, cabinet, wrench; essentially a tool that schedules a daily check for these keywords in market
# 
# **Disclaimer:** Due to size, I limited the results to 10/page. 

# In[ ]:


import requests 
from bs4 import BeautifulSoup 
from time import sleep
import pandas as pd


# In[ ]:


webpage = requests.get('https://losangeles.craigslist.org/search/sss?query=garage%20and%20moving') #https://losangeles.craigslist.org/search/sss?query=garage+and+moving
#https://losangeles.craigslist.org/search/sss?query=garage%20and%20moving
bs = BeautifulSoup(webpage.text, 'html.parser')


# Using the **prettify()** method allows me to see the hmtl code in a more "readable" format. This help find what classes and attribute tags each results (and its context) were under) 

# In[ ]:


#bs.prettify() 
#post = bs.find_all('li',class_='result-row') 
#posts.prettify() 


# **check_keyword()** Similar to the Project 1, this function will take a list of words (keyword) and a line (title). It will check whether each word in the list is in the title. If it is, it will create a string of the keyword in the title. 

# In[1]:


def check_keyword(keywords: 'list of words', title: 'titletext'): 
    #Returns the keywords (str) if it is in the title 
    title = title.lower() 
    result = '' 
    for every_word in keywords: 
        if every_word in title: 
            result += every_word + ', '
    return result


# **Page Numbers:** Since the website has more than one page of results, the **num_results** will find the number of results in the cateogry of "Garage & Moving Sale." After obtaining the number of results under this category, you divide it by 120, which can be found when moving to the next page. The first page does not have a page parameter in the url. As you click on my pages, the increments in the page increases by 120. Therefore, each page (after 1) wil have a page param of +120. 

# In[ ]:


#Establishing the # of pages from the listing
num_results = int(bs.find('span', 'totalcount').text) 
pages = num_results // 120
#pages


# The **main()** method is the "main" function of the project and produces the end result of the project's goal. The keywords, page number parameter and a result (final) dictionary were created. The page number is the range because the url (and request) will be dependent on the page number (as mentioned above). The second url is the url from the second page's results. The "s=" is the param before the results that change on every page. A **+=** for the **page_num** was used to update the page once the for-loop in the page posts is complete. Those that did not have an empty string as a result (passed the check_keyword) were put into a dictionary, put as a data frame, and were written to a file. 
# 
# **Quick Note:** Since the URL looks at Los Angeles Craigslit, the keywords (in the scenario) did not apply to most of the results. Therefore, I included the word garage and sale to where I saw immediate results (and knew I would get at least 1 post), during the build of this function. 

# In[ ]:


def main():
    #Runs the Main Program 
    page_num = 120
    keywords = ['mattress', 'cabinet', 'sale', 'garage']
    final = {'Keyword': [], 'Title': [], 'URL': []}
    url2 = 'https://losangeles.craigslist.org/search/sss?query=garage%20and%20moving&' 
    
    sleep(5)
    for i in range(pages): 
        if i == 0: 
            sleep(10)
            
            post = bs.find_all('li',class_='result-row')
            count = 0 
             
            for each_post in post[:10]: #ONLY DOING FIRST 10 POSTS BECAUSE OF TESTING TO SEE IF FUNC WORKS
                sleep(10)
                
                eachpost_title = each_post.find('a', class_='result-title hdrlnk')
                eachpost_link = eachpost_title['href']
                eachpost_titletext = eachpost_title.text
                
                sleep(10)
            
                if check_keyword(keywords, eachpost_titletext) != '': 
                    final['Keyword'].append(check_keyword(keywords, eachpost_titletext))
                    final['Title'].append(eachpost_titletext)
                    final['URL'].append(eachpost_link) 
                else:  
                    continue 
                
                count += 1 
                
                print('Result #' + str(count) + ' complete.')
    
            print('Completing page: ' + str(i + 1))
        elif i > 0: 
            #print(url2 + 's=' + str(page_num))
            
            new_url = requests.get(url2 + 's=' + str(page_num)) 
            soup = BeautifulSoup(new_url.text, 'html.parser')
            post = soup.find_all('li', class_='result-row') 
            count = 0 
            sleep(10)
            
            for each_post in post[:10]: 
                sleep(5)
                
                eachpost_title = each_post.find('a', class_='result-title hdrlnk')
                eachpost_link = eachpost_title['href']
                eachpost_titletext = eachpost_title.text 
                
                sleep(10)
                
                if check_keyword(keywords, eachpost_titletext) != '': 
                    final['Keyword'].append(check_keyword(keywords, eachpost_titletext))
                    final['Title'].append(eachpost_titletext)
                    final['URL'].append(eachpost_link)
                else:  
                    continue 
                    
                count += 1 
                
                print('Result #' + str(count) + ' complete.')
            
            page_num += 120 

            print('Completing page: ' + str(i + 1))
            
        else:
            continue 
    df = pd.DataFrame(final)
    df.to_csv('craiglist_search.csv') 
    print('\nFile Complete')


# In[ ]:


main()

