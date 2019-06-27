# An international team of scientists, led by UCLA biologists, used this dendrogram to report genetic data from more than 900 dogs from
# 85 breeds -- and more than 200 wild gray wolves worldwide, including populations from North America, Europe, the Middle East, and East Asia.
# They used molecular genetic techniques to analyze more than 48,000 genetic markers.
# This diagram, shows hierarchical clustering of these animals based on the similarity in
# their genetic data. 
# 
# Hierarchical clustering algorithms build a hierarchy of clusters where each node is a cluster consisting of the clusters of its
# daughter nodes. Strategies for hierarchical clustering generally fall into two types: Divisive and Agglomerative.

# Divisive is top-down, so you start with all observations in a large cluster and brea it down into smaller pieces. 
# Think about divisive as "dividing" the cluster.

# Agglomerative is the opposite of divisive, so it is bottom-up, where each observation starts in its own cluster and pairs 
# of clusters are merged together as they move up the hierarchy.
# Agglomeration means to amass or collect things, which is exactly what this does with the cluster.
# The Agglomerative approach is more popular among data scientists

# Let’s look at a sample of Agglomerative clustering.
# This method builds the hierarchy from the individual elements by progressively merging clusters. 
# In our example, let’s say we want to cluster 6 cities in Canada based on their distances from one another.
# They are: Toronto, Ottawa, Vancouver, Montreal, Winnipeg, and Edmonton.
# We construct a distance matrix at this stage, where the numbers in the row i column j is the distance between the i and j cities. 
# In fact, this table shows the distances between each pair of cities.

# The algorithm is started by assigning each city to its own cluster.
# So, if we have 6 cities, we have 6 clusters, each containing just one city.
# Let’s note each city by showing the first two characters of its name.
# The first step is to determine which cities -- let’s call them clusters from now on -- to merge into a cluster. 
# Usually, we want to take the two closest clusters according to the chosen distance. Looking at the distance matrix, Montreal and
# Ottawa are the closest clusters. So, we make a cluster out of them.
# Please notice that we just use a simple 1-dimentional distance feature here, but our object can be multi-dimensional, 
# and distance measurement can be either Euclidean, Pearson, average distance, or many others, depending on data type and domain knowledge.
# Anyhow, we have to merge these two closest cities in the distance matrix as well.
# So, rows and columns are merged as the cluster is constructed.
# As you can see in the distance matrix, rows and columns related to Montreal and Ottawa cities are merged as the cluster is constructed. 
# Then, the distances from all cities to this new merged cluster get updated. But how? For example, how do we calculate the distance
# from Winnipeg to the Ottawa-Montreal cluster? Well, there are different approaches, but let’s assume, for example, 
# we just select the distance from the centre of the Ottawa-Montreal cluster to Winnipeg. Updating the distance matrix, we now have
# one less cluster. Next, we look for the closest clusters once again. In this case, Ottawa-Montreal and Toronto
# are the closest ones, which creates another cluster. In the next step, the closest distance is between the Vancouver cluster and the Edmonton
# cluster. Forming a new cluster, their data in the matrix table gets updated. Essentially, the rows and columns are merged
# as the clusters are merged and the distance updated. This is a common way to implement this type of clustering, and has the benefit of caching
# distances between clusters. In the same way, agglomerative algorithm proceeds by merging clusters.
# And we repeat it until all clusters are merged and the tree becomes completed. It means, until all cities are clustered into a single 
# cluster of size 6. 

# Hierarchical clustering is typically visualized as a dendrogram as shown on this slide.
# Each merge is represented by a horizontal line. The y-coordinate of the horizontal line is the similarity of the two clusters that were
# merged, where cities are viewed as singleton clusters. By moving up from the bottom layer to the top node, a dendrogram allows us to reconstruct
# the history of merges that resulted in the depicted clustering.
# Essentially, Hierarchical clustering does not require a pre-specified number of clusters.
# However, in some applications we want a partition of disjoint clusters just as in flat clustering.
# In those cases, the hierarchy needs to be cut at some point.
# For example here, cutting in a specific level of similarity, we create 3 clusters of similar cities.

# Agglomerative algorithm for Hierarchical Clustering.
# Remember that Agglomerative clustering is a bottom-up approach.
# Let’s say our dataset has n data points. First, we want to create n clusters, one for each data point. 
# Then each point is assigned as a cluster. Next, we want to compute the distance/proximity matrix, which will be an n by n table.
# After that, we want to iteratively run the following steps until the specified cluster
# number is reached, or until there is only one cluster left.
# First, MERGE the two nearest clusters. (Distances are computed already in the proximity matrix.)
# Second, UPDATE the proximity matrix with the new values.
# We stop after we’ve reached the specified number of clusters, or there is only one cluster remaining, with the result stored in a dendrogram. 

# So, in the proximity matrix, we have to measure the distances between clusters, and also merge the clusters that are “nearest.”
# So, the key operation is the computation of the proximity between the clusters with one point, and also clusters with multiple data points.
# At this point, there are a number of key questions that need to be answered.
# For instance, “How do we measure the distances between these clusters and How do we define the ‘nearest’ among clusters?” 
# We also can ask, “Which points do we use?”
# First, let’s see how to calculate the distance between 2 clusters with 1 point each.
# Let’s assume that we have a dataset of patients, and we want to cluster them using hierarchy clustering. So, our data points are patients, 
# with a feature set of 3 dimensions. For example, Age, Body Mass Index (or BMI), and Blood Pressure. 
# We can use different distance measurements to calculate the proximity matrix. For instance, Euclidean distance.

# So, if we have a dataset of n patients, we can build an n by n dissimilarly-distance matrix. It will give us the distance of clusters with
# 1 data point. However, as mentioned, we merge clusters in Agglomerative clustering. Now, the question is, “How can we calculate
# the distance between clusters when there are multiple patients in each cluster?”
# We can use different criteria to find the closest clusters, and merge them.
# In general, it completely depends on the data type, dimensionality of data, and most importantly, the domain knowledge of the dataset. 
# In fact, different approaches to defining the distance between clusters, distinguish the different algorithms.
# As you might imagine, there are multiple ways we can do this.

# Single linkage is defined as the shortest distance between 2 points in each cluster,  such as point “a” and “b”. 
# Complete-Linkage Clustering. This time, we are finding the longest distance between points in each cluster, such as the distance between point “a” and “b”.
# Average Linkage Clustering, or the mean distance.
# This means we’re looking at the average distance of each point from one cluster to every point in another cluster. 
# Centroid Linkage Clustering. Centroid is the average of the feature sets of points in a cluster. This linkage takes into account the centroid
# of each cluster when determining the minimum distance.

# There are 3 main advantages to using hierarchical clustering.
# First, we do not need to specify the number of clusters required for the algorithm.
# Second, hierarchical clustering is easy to implement.
# third, the dendrogram produced is very useful in understanding the data.
# There are some disadvantages as well. First, the algorithm can never undo any previous steps. So for example, the algorithm clusters 2 points,
# and later on we see that the connection was not a good one, the program cannot undo that step. Second, the time complexity for the clustering
# can result in very long computation times, in comparison with efficient algorithms, such k-Means. Finally, if we have a large dataset, it can
# become difficult to determine the correct number of clusters by the dendrogram.

# Now, let’s compare Hierarchical clustering with k-Means.
# K-Means is more efficient for large datasets. In contrast to k-Means, Hierarchical clustering does not require the number of clusters 
# to be specified. Hierarchical clustering gives more than one partitioning depending on the resolution,
# whereas k-Means gives only one partitioning of the data.
# Hierarchical clustering always generates the same clusters, in contrast with k-Means that returns different clusters each time 
# it is run due to random initialization of centroids.
