#!/usr/bin/env python3
#Name    : Mohnish Agrawal
#Date    : 1st November 2018

import re
import itertools
import copy

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    name = "Mohnish Agrawal"
    email = "#"
    roll_num = "2018053"

    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices
        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        
        self.edges    = ordered_edges
        
        self.validate()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

    def dict_graph(self):
        #Converts and returns the set of edges in array edges into a dictionary in a graph format

        dict1={}
        for i in self.edges:
            for j in i:
                listx=list(i)
                listx.remove(j)
                if j not in dict1:
                    dict1[j]=listx
                else:
                    listy=dict1[j]
                    listy.extend(listx)
                    dict1[j]=listy
        return dict1

    def bfs(self,startnode,graph2=[],neighbour=[],count=0):
        ''' This function uses the bfs algorithm to search for one of the shortest path available.
            
            Args:
                startnode: Vertex to start from
                graph2: A list which is in the form of a graph
                neighbour: A list of neighbours of startnode

            Returns:
                A list which represents a graph
         '''

        for i in self.edges:
            if startnode in i:
                listx=list(i)
                listx.remove(startnode)        
                if not any( listx[0] in sublist for sublist in graph2):
                    neighbour.append(listx[0])
                if len(graph2)==0:
                    listx=[startnode]
                    listy=list(copy.deepcopy(i))
                    listy.remove(startnode)
                    listx.append(listy[0])
                    graph2.append(listx)
                elif(count==0):
                    if not any( listx[0] in sublist for sublist in graph2):
                        listx=[startnode]
                        listy=list(copy.deepcopy(i))
                        listy.remove(startnode)
                        listx.append(listy[0])
                        graph2.append(listx)
                else:
                    for j in graph2:
                        if startnode in j:
                            if not any( listx[0] in sublist for sublist in graph2):
                                if any( j.count(l)>1 for l in i ):
                                    z=copy.deepcopy(j)
                                    listx=[startnode]
                                    listy=list(copy.deepcopy(i))
                                    listy.remove(startnode)
                                    listx.append(listy[0])
                                    z=z[:z.index(listx[0])+1]
                                    z.extend(list(i))
                                    graph2.append(z)
                                else:
                                    j.extend(list(i))
        count+=1
        for j in neighbour:
            neighbour.remove(j)
            return self.bfs(j,graph2,neighbour,count)
        return graph2

    def dfs(self,dict,startnode,endnode,path=[],path1=[],visited=[]):
        '''Implements the Depth First search algorithm to find al the possible paths that can be covered
            
            Args:
                startnode: Vertex to find distance from
                endnode: Vertex to find distance to
                path: returns the different paths available
                path1: stores different paths in a list
                visited: Elements Visited

            Returns:
            A list of all the possible paths from start node to end node
        '''
        path1=path1+[startnode]
        visited=visited+[startnode]
        for i in dict[startnode]:
            if i not in visited:
                if i==endnode:
                    path1=path1+[i]
                    path.append(path1)
                    path1=path1[0:path1.index(startnode)+1]
                else:
                    self.dfs(dict,i,endnode,path,path1,visited)
                    if i in visited:
                        visited=visited[0:visited.index(i)+1]
        return path   

    def min_dist(self, start_node, end_node):
        '''
        Finds minimum distance between start_node and end_node

        Args:
            start_node: Vertex to find distance from
            end_node: Vertex to find distance to

        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''
        graph=self.bfs(start_node,[])
        graph2=[]
        for i in graph:
            i2=[]
            for j in i:
                if j not in i2:
                    i2.append(j)
            graph2.append(i2)
        for i in graph2:
            if end_node in i:
                min_dist=i.index(end_node)-i.index(start_node)
        return min_dist

    def all_shortest_paths(self,start_node, end_node):
        """
        Finds all shortest paths between start_node and end_node

        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
        """
        min_dist=self.min_dist(start_node,end_node)
        all_shortest_paths=self.all_paths(start_node,end_node,min_dist)
        return all_shortest_paths

    def all_paths(self, node, destination, dist):
        """
        Finds all paths from node to destination with length = dist

        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path

        Returns:
            List of path, where each path is list ending on destination

            Returns None if there no paths
        """
        graph_dict=self.dict_graph()
        all_paths=self.dfs(graph_dict,node,destination,[])
        all_paths_at_partdist=[]
        for i in all_paths:
            if len(i)-1==dist:
                all_paths_at_partdist.append(i)
        return all_paths_at_partdist

    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """
        vertices2=copy.deepcopy(self.vertices)
        vertices2.remove(node)
        vertices3=copy.deepcopy(vertices2)
        bet_cent=[]
        for i in vertices2:
            vertices3.remove(i)
            for j in vertices3:
                all_shortest_paths=len(self.all_shortest_paths(i,j))
                cycle=0
                for k in self.all_shortest_paths(i,j):
                    if node in k:
                        cycle+=1
                div=cycle/all_shortest_paths
                bet_cent.append(div)
        betweenness=sum(bet_cent)
        return betweenness


    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        dict1={}
        bet_arr=[]
        for i in self.vertices:
            bet=self.betweenness_centrality(i)
            dict1[i]=bet
            bet_arr.append(bet)
        bet_arr.sort(reverse=True)
        max_bet=bet_arr[0]
        top_K_Nodes=[]
        for i in self.vertices:
            if dict1[i]==max_bet:
                top_K_Nodes=top_K_Nodes+[i]
        return top_K_Nodes

if __name__ == "__main__":
    edges    = []
    vertices = list(map(int,input().split()))
    
    #Taking in input 
    n = int(input())
    for _ in range(n):
    	insertingTuples = tuple(map(int,input().split()))
    	if insertingTuples not in edges:
    		edges.append(insertingTuples)

    #Implementing object graph of given vertices and the edges that exist between them.
    graph = Graph(vertices, edges)
    bet=graph.top_k_betweenness_centrality()
    bet1=graph.betweenness_centrality(bet[0])
    bet1=bet1*2/((len(vertices)-1)*(len(vertices)-2))

    print("k = "+str(len(bet))+", SBC = "+str(bet1)+", Top '"+str(len(bet))+"' Nodes: ",str(bet)[1:len(str(bet))-1])