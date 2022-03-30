#!/usr/bin/env python
# coding: utf-8

# **Project 6 Basics: Tiffany Aihara** 
# 
# **Directions:** "Analyze a covert social network to determine who the weakest link is, and what happens to the network when you remove that link. Provide notes and a write-up, which should include at least some level of visualization.
# 
# **Goal:** To create a social network using the networkx library.
# 
# **Source:** D. Lusseau, K. Schneider, O. J. Boisseau, P. Haase, E. Slooten, and S. M. Dawson, The bottlenose dolphin community of Doubtful Sound features a large proportion of long-lasting associations, Behavioral Ecology and Sociobiology 54, 396-405 (2003). Retrieved from: http://www-personal.umich.edu/~mejn/netdata/.

# In[1]:


import pandas as pd
import networkx as nx
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# **Note:** The program will show two ways to create a networkx (file, zip link). I wanted to practice both approaches. 

# In[2]:


path = '/Users/tiffanyaihara/Desktop/dolphins.xml' 
url = 'http://www-personal.umich.edu/~mejn/netdata/dolphins.zip'


# **Part 1: From a File** 
# 
# The first thing was to open and read the file. The file was a "xml" file which can be put into Beautiful Soup to read. From the file, HTML tags that indicated nodes and links were present. The variables *node* and *link* were used to store all the tags with nodes (node) and links (link). 

# In[3]:


file = BeautifulSoup(open(path).read(), 'xml')
node = file.find_all('node')
link = file.find_all('link')


# Since the data (for both node/link) is a a series, we have to iterate through through the data set by indexing. If we index each series then the information needed for the graph can be gathered. For ease, I created a tuple of the data collection and store the tuples as an item in a list. 

# In[4]:


links = []
for i in range(len(link)): 
    tuples = (link[i]['source'], link[i]['target']) 
    links.append(tuples)
    
nodes = []  
for i in range(len(node)): 
    tups = (node[i]['id'], node[i]['title']) 
    nodes.append(tups)


# In[5]:


graph = nx.DiGraph()


# Graphing the node is just one value and therefore can be added to the graph by using networkx's builtin function. For the edges, networkx's built-in function *add_edge* takes a tuple. Since "links" stores a list of tuples, it is easier to graph the edge. 

# In[6]:


for each_node in nodes: 
    graph.add_node(each_node[0])
    #nodes[1] = name of dolphin

for each_tuple in links: 
    graph.add_edge(each_tuple[0], each_tuple[1])
     


# In[13]:


fig = plt.figure() 
nx.draw_networkx(graph)
fig.savefig('initial_networkx.png')


# In[8]:


nx.number_weakly_connected_components(graph) #Returns the number of weakly connected components in G.


# In[9]:


plt.show() 
plt.savefig("initial_graph.png")


# 
# The following lines of code generates a set of nodes that are weakly connected. The graph shows the max weakly connections.  

# In[10]:


options = {
    'node_color': 'purple', 
    'node_size': 30, 
    'width': 0.1,
    'with_labels': False
}


# In[11]:


components = nx.weakly_connected_components(graph)
low_components = max(components, key=len)

subgraph = graph.subgraph(low_components)

#nx.draw_networkx(subgraph, **options)


# In[12]:


f = plt.figure() 
nx.draw_networkx(subgraph, **options)
f.savefig('weakest_components.png')

