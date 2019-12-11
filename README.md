# BetweennessCentrality
This projects main purpose is to understand what betweenness centrality actually means. Betweenness Centrality is a metric that measures the importance of each node in a graph/network by giving it a numerical value. The nodes with the highest values of Betweenness Centrality will be the most important nodes in the graph. 

In this project, we will consider an undirected, unweighted, connected graphs with no loops. DFS & BFS algorithms have been used to calculate the shortest distance between two vertices.

Betweenness Centrality of node V = Summation(Number of shortest Path from Node s to t that pass from vertex V / total number of shortest path from Node s to t)

# To Run the file
Clone the repository and extract the folder. To run the file, you need to have python3 installed. You can follow instructions given in this website (https://realpython.com/installing-python/) to install python3. Also, you need to make sure that the following modules are already installed in your system.
1. Itertools
2. re
3. copy

Once you have installed python3 and the modules, you can run the file by opening the folder location in your terminal/Command Line and typing in the following command - python3/python SBC.py

# Input 
The first line must contain all the vertices(integers) of the graph seperated with a space. The second line, "n" contains total number of bidirectional edges in the graph, and the following "n" lines contain two space seperated integers which act as vertices of the graph. 

The output: Prints node/nodes(If equal SBC) with the highest Standardized Betweenness Centrality (SBC) with thier SBC.
