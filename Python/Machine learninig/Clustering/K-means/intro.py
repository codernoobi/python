# Imagine that you have a customer dataset, and you need to apply customer segmentation on this historical data. 
# Customer segmentation is the practice of partitioning a customer base into groups of individuals that have similar characteristics.
# One of the algorithms that can be used for customer segmentation is k-Means clustering.
# k-Means can group data only “unsupervised,” based on the similarity of customers to each other.
# Let’s define this technique more formally.
# There are various types of clustering algorithms, such as partitioning, hierarchical, or density-based clustering. 
# k-Means is a type of partitioning clustering, that is, it divides the data into k non-overlapping subsets (or clusters) 
# without any cluster-internal structure, or labels. This means, it’s an unsupervised algorithm. Objects within a cluster are very 
# similar and objects across different clusters are very different or dissimilar. 
# 
# As you can see, for using k-Means, we have to find similar samples (for example, similar customers).
# Now we face a couple of key questions. First, “How can we find the similarity of samples in clustering?” And then, 
# “How do we measure how similar two customers are with regard to their demographics?”
# Though the objective of k-Means is to form clusters in such a way that similar samples go into a cluster, 
# and dissimilar samples fall into different clusters, it can be shown that instead of a similarity metric, 
# we can use dissimilarity metrics. In other words, conventionally, the distance of samples from each other is used to shape
# the clusters. So, we can say, k-Means tries to minimize the “intra-cluster” distances and maximize the “inter-cluster” distances.

# Now, the question is, “How we can calculate the dissimilarity or distance of two cases, such as two customers?”
# Assume that we have two customers, we’ll call them customer 1 and 2.
# Let’s also assume that we have only one feature for each of these two customers, and that feature is Age. We can easily use a 
# specific type of Minkowski distance to calculate the distance of these two customers. Indeed, it is the Euclidian
# distance. Distance of x1 from x2 is root of 34 minus 30 power 2, which is 4. 

# What about if we have more than one feature, for example Age and Income?
# For example, if we have income and age for each customer, we can still use the same formula, but this time in a 2-dimensional space.
# Also, we can use the same distance matrix for multi-dimensional vectors.
# Of course, we have to normalize our feature set to get the accurate dissimilarity measure.
# There are other dissimilarity measures as well that can be used for this purpose, but it is highly dependent on data type and also the 
# domain that clustering is done for it. For example, you may use Euclidean distance, cosine similarity, average distance, and so
# on. Indeed, the similarity measure highly controls how the clusters are formed, so it is recommended to understand the domain 
# knowledge of your dataset, and data type of features, and then choose the meaningful distance measurement.

# Now, let’s see how k-Means clustering works. 
# For the sake of simplicity, let’s assume that our dataset has only two features, the age and income of customers.
# This means, it’s a 2-dimentional space. We can show the distribution of customers using a scatterplot. 
# The y-axes indicates Age and the x-axes shows Income of customers. We try to cluster the customer dataset into
# distinct groups (or clusters) based on these two dimensions.
# In the first step, we should determine the number of clusters.
# The key concept of the k-Means algorithm is that it randomly picks a center point for each cluster. It means, we must initialize k, 
# which represents "number of clusters." Essentially, determining the number of clusters in a data set, or k, is a hard problem in 
# k-Means that we will discuss later. For now, let’s put k equals 3 here, for our sample dataset.

# It is like we have 3 representative points for our clusters.
# These 3 data points are called centroids of clusters, and should be of same feature size of our customer feature set. 
# There are two approaches to choose these centroids:
# 1) We can randomly choose 3 observations out of the dataset and use these observations as the initial means. 
# 2) We can create 3 random points as centroids of the clusters, which is our choice that is shown in this plot with red color.

# After the initialization step, which was defining the centroid of each cluster, we have to assign each customer to the closest center. 
# For this purpose, we have to calculate the distance of each data point (or in our case, each customer) from the centroid points.
# As mentioned before, depending on the nature of the data and the purpose for which clustering is being used, 
# different measures of distance may be used to place items into clusters.
# Therefore, you will form a matrix where each row represents the distance of a customer from each centroid. It is called the "distance-matrix."

# The main objective of k-Means clustering is to minimize the distance of data points from the centroid of its cluster and 
# maximize the distance from other cluster centroids.
# So, in this step we have to find the closest centroid to each data point.
# We can use the distance-matrix to find the nearest centroid to data points.
# Finding the closest centroids for each data point, we assign each data point to that cluster.
# In other words, all the customers will fall to a cluster, based on their distance from centroids. We can easily say that it does not result
# in good clusters, because the centroids were chosen randomly from the first.
# Indeed, the model would have a high error. Here, error is the total distance of each point from its centroid. 
# It can be shown as within-cluster sum of squares error. Intuitively, we try to reduce this error.
# It means we should shape clusters in such a way that the total distance of all members of a cluster from its centroid be minimized. 
# Now, the question is, "How we can turn it into better clusters, with less error?"

# Okay, we move centroids. In the next step, each cluster center will be updated to be the mean for data points in its cluster. 
# Indeed, each centroid moves according to their cluster members. In other words, the centroid of each of the
# 3 clusters becomes the new mean. For example, if Point A coordination is 7.4 and 3.6, and Point B features are 7.8 and 3.8, 
# the new centroid of this cluster with 2 points, would be the average of them, which is 7.6 and 3.7.
# Now we have new centroids. As you can guess, once again, we will have to calculate the distance of all points from the new centroids.
# The points are re-clustered and the centroids move again.
# This continues until the centroids no longer move.
# Please note that whenever a centroid moves, each point’s distance to the centroid needs to be measured again.

# Yes, k-Means is an iterative algorithm, and we have to repeat steps 2 to 4 until the algorithm converges. 
# In each iteration, it will move the centroids, calculate the distances from new centroids, and assign the data points to the nearest
# centroid. It results in the clusters with minimum error, or the most dense clusters. However, as it is a heuristic algorithm, there
# is no guarantee that it will converge to the global optimum, and the result may depend on the initial clusters. 
# It means this algorithm is guaranteed to converge to a result, but the result may be a local optimum (i.e. not necessarily the best possible
# outcome). To solve this problem, it is common to run the whole process, multiple times, with different starting conditions.
# This means, with randomized starting centroids, it may give a better outcome.
# And as the algorithm is usually very fast, it wouldn’t be any problem to run it multiple times.

# Let’s define the algorithm more concretely before we talk about its accuracy.
# A k-Means algorithm works by randomly placing k centroids, one for each cluster.
# The farther apart the clusters are placed, the better.
# The next step is to calculate the distance of each data point (or object) from the centroids.
# Euclidean distance is used to measure the distance from the object to the centroid.
# Please note, however, that you can also use different types of distance measurements, not just Euclidean distance. 
# Euclidean distance is used because it’s the most popular. Then, assign each data point (or object) to
# its closest centroid, creating a group. Next, once each data point has been classified to a group, recalculate the position of the k centroids. 
# The new centroid position is determined by the mean of all points in the group.

# Finally, this continues until the centroids no longer move.
# Now the question is, "How can we evaluate the 'goodness' of the clusters formed by k-Means?" In other words, "How do we calculate the accuracy
# of k-Means clustering?” One way is to compare the clusters with the ground truth, if it’s available. However, because k-Means is an unsupervised
# algorithm, we usually don’t have ground truth in real world problems to be used.
# But, there is still a way to say how bad each cluster is, based on the objective of the k-Means. This value is the average distance between
# data points within a cluster. Also, average of the distances of data points from their cluster centroids can be used as a 
# metric of error for the clustering algorithm. Essentially, determining the number of clusters in a data set, 
# or k, as in the k-Means algorithm, is a frequent problem in data clustering. The correct choice of k is often ambiguous,
# because it’s very dependent on the shape and scale of the distribution of points in a data set. 
# 
# There are some approaches to address this problem, but one of the techniques that is commonly used, is to run the clustering across
# the different values of K, and looking at a metric of accuracy for clustering.
# This metric can be “mean distance between data points and their cluster centroid,” which indicate how dense our clusters are, 
# or to what extend we minimized the error of clustering. Then looking at the change of this metric, we can find the best value for k.
# But the problem is that with increasing the number of clusters, the distance of centroids to data points will always reduce. 
# This means, increasing K will always decrease the “error.” So, the value of the metric as a function of K is plotted and the 
# "elbow point" is determined, where the rate of decrease sharply shifts. It is the right K for clustering.
# This method is called the “elbow” method.

# So, let’s recap k-Means clustering: k-Means is a partitioned-based clustering, which is:
# a) Relatively efficient on medium and large sized datasets;
# b) Produces sphere-like clusters, because the clusters are shaped around the centroids;
# c) Its drawback is that we should pre-specify the number of clusters, and this is not an easy task.