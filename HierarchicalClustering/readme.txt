Intro to Hierarchical clustering:

- Handy method in bioinformatics and all of data science to group the data 
  into different groups/clusters in order(built either bottom up (agglomerative) 
  or topdown(divisive)).

- constructs a cluster for all values of k (k =1 to n)

- The only difference between k = r and k = r + 1 is that one of the r clusters
  splits up in order to obtain r + 1 clusters 
  (or, to put it differently, two of the r + 1 clusters combine to yield r clusters)

- visually represented as the dendogram 
	> length of branch represents what was clustered first

Application:
- Analyze the gene expression data 
- Phlogeny analysis


Ponder:
1) How to compare this clustering techniques with the k-means clustering method ?
2) How different are the clusters generated by bottom up and top down approach ?  
