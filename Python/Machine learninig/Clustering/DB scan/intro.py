# a density-based clustering algorithm, which is appropriate to use when examining spatial data.
# Most of the traditional clustering techniques, such as k-means, hierarchical, and fuzzy clustering, can be used to group data in an 
# un-supervised way. However, when applied to tasks with arbitrary shape clusters, or clusters within clusters,
# traditional techniques might not be able to achieve good results.
# That is, elements in the same cluster might not share enough similarity -- or the performance may be poor.

# Additionally, while partitioning-based algorithms, such as K-Means, may be easy to understand and implement in practice, 
# the algorithm has no notion of outliers. That is, all points are assigned to a cluster, even if they do not belong in any.
# In the domain of anomaly detection, this causes problems as anomalous points will be assigned to the same cluster as "normal" data points. 
# The anomalous points pull the cluster centroid towards them, making it harder to classify them as anomalous points.

# In contrast, Density-based clustering locates regions of high density that are separated from one another by regions of low density. 
# Density, in this context, is defined as the number of points within a specified radius. A specific and very popular type of density-based
# clustering is DBSCAN. DBSCAN is particularly effective for tasks like class identification on a spatial context. 
# The wonderful attribute of the DBSCAN algorithm is that it can find out any arbitrary shape cluster without getting affected by noise.

# For example, this map shows the location of weather stations in Canada.
# DBSCAN can be used here to find the group of stations, which show the same weather conditions.
# As you can see, it not only finds different arbitrary shaped clusters, it can find the denser part of data-centered samples 
# by ignoring less-dense areas or noises.

# DBSCAN stands for Density-Based Spatial Clustering of Applications with Noise.
# This technique is one of the most common clustering algorithms, which works based on density of object. 
# DBSCAN works on the idea is that if a particular point belongs to a cluster, it should be near to lots of other points in that cluster.
# It works based on 2 parameters: Radius and Minimum Points.
# R determines a specified radius that, if it includes enough points within it, we call it a "dense area." 
# M determines the minimum number of data points we want in a neighborhood to define a cluster.

# Let’s define radius as 2 units. For the sake of simplicity, assume it as radius of 2 centimeters around a point of interest. 
# Also, let’s set the minimum point, or M, to be 6 points including the point of interest. To see how DBSCAN works, we have to determine
# the type of points. Each point in our dataset can be either a core, border, or outlier point. 
# But the whole idea behind the DBSCAN algorithm is to visit each point, and find its type first.

# Then we group points as clusters based on their types. Let’s pick a point randomly. First we check to see whether it’s a core data point.
# So, what is a core point? 
# A data point is a core point if, within R-neighborhood of the point, there are at least M points. For example, as there are 6 points in the
# 2-centimeter neighbor of the red point, we mark this point as a core point.

# what happens if it’s NOT a core point?
# Let’s look at another point. Is this point a core point? No.
# As you can see, there are only 5 points in this neighborhood, including the yellow point.
# So, what kind of point is this one? In fact, it is a "border" point.
# What is a border point? A data point is a BORDER point if:
# a. Its neighborhood contains less than M data points
# b. It is reachable from some core point. Here, Reachability means it is within R-distance from a core point. 
# It means that even though the yellow point is within the 2-centimeter neighborhood of the red point, it is not by itself a core
# point, because it does not have at least 6 points in its neighborhood.
# We continue with the next point. As you can see it is also a core point. And all points around it, which are not core points, are border points.
# Next core point. And next core point.

# Let’s take another point. You can see it is not a core point, nor is it a border point. So, we’d label it as an outlier.
# What is an outlier? An outlier is a point that: Is not a core point, and also, is not close enough to be reachable from a core point.
# We continue and visit all the points in the dataset and label them as either Core, Border, or Outlier.

# The next step is to connect core points that are neighbors, and put them in the same cluster.
# So, a cluster is formed as at least one core point, plus all reachable core points, plus all their borders. It simply shapes all 
# the clusters and finds outliers as well.

# Let’s review this one more time to see why DBSCAN is cool.
# DBSCAN can find arbitrarily shaped clusters. It can even find a cluster completely surrounded by a different cluster. 
# DBSCAN has a notion of noise, and is robust to outliers. On top of that, DBSCAN makes it very practical for use in many really world 
# problems because it does not require one to specify the number of clusters, such as K in k-Means.