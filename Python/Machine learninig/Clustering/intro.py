# Imagine that you have a customer dataset, and you need to apply customer segmentation on this historical data. 
# Customer segmentation is the practice of partitioning a customer base into groups of individuals that have similar characteristics.
# It is a significant strategy as it allows a business to target specific groups of customers so as to more effectively 
# allocate marketing resources. For example, one group might contain customers who are high-profit and low-risk, that is,
# more likely to purchase products, or subscribe for a service.
# Knowing this information allows a business to devote more time and attention to retaining these customers. 
# Another group might include customers from non-profit organizations, and so on. A general segmentation process is not usually
# feasible for large volumes of varied data. Therefore, you need an analytical approach to deriving segments and groups from large data sets.

# Customers can be grouped based on several factors: including age, gender, interests, spending habits, and so on. 
# The important requirement is to use the available data to understand and identify how customers are similar to each other.
# Let’s learn how to divide a set of customers into categories, based on characteristics they share. 
# One of the most adopted approaches that can be used for customer segmentation is clustering. Clustering can group data only “unsupervised,”
# based on the similarity of customers to each other.

# It will partition your customers into mutually exclusive groups, for example, into 3 clusters.
# The customers in each cluster are similar to each other demographically.
# Now we can create a profile for each group, considering the common characteristics of each cluster. 
# For example, the first group is made up of AFFULUENT AND MIDDLE AGED customers. 
# The second is made up of YOUNG EDUCATED AND MIDDLE INCOME customers. 
# And the third group includes YOUNG AND LOW INCOME customers. 
# 
# Finally, we can assign each individual in our dataset to one of these groups or segments of customers.
# Now imagine that you cross-join this segmented dataset, with the dataset of the product or services that customers purchase from your company.
# This information would really help to understand and predict the differences in individual customers’ preferences and their 
# buying behaviors across various products. Indeed, having this information would allow your company to develop highly personalized
# experiences for each segment. Customer segmentation is one of the popular usages of clustering. Cluster analysis also has
# many other applications in different domains. So let’s first define clustering, and then we’ll look at other applications.

# Clustering means finding clusters in a dataset, unsupervised.
# So, what is a cluster? A cluster is group of data points or objects in a dataset that are similar to other objects in the group, 
# and dissimilar to data points in other clusters. Now, the question is, “What is different
# between clustering and classification?”
# Let’s look at our customer dataset again. Classification algorithms predict categorical
# class labels. This means, assigning instances to pre-defined classes such as “Defaulted” or “Non-Defaulted.” For example, 
# if an analyst wants to analyze customer data in order to know which customers might default on their payments, she uses
# a labeled dataset as training data, and uses classification approaches such as a decision tree, Support Vector Machines (or SVM), or, 
# logistic regression to predict the default value for a new, or unknown customer. 
# 
# Generally speaking, classification is a supervised learning where each training data instance belongs to a particular class.
# In clustering, however, the data is unlabelled and the process is unsupervised.
# For example, we can use a clustering algorithm such as k-Means, to group similar customers as mentioned, and assign them to a cluster, 
# based on whether they share similar attributes, such as age, education, and so on. While I’ll be giving you some examples in
# different industries, I’d like you to think about more samples of clustering.

# In the Retail industry, clustering is used to find associations among customers based on their demographic characteristics 
# and use that information to identify buying patterns of various customer groups. Also, it can be used in recommendation systems
# to find a group of similar items or similar users, and use it for collaborative filtering, to recommend things like books or movies to customers.
# In Banking, analysts find clusters of normal transactions to find the patterns of fraudulent credit card usage. 
# Also, they use clustering to identify clusters of customers, for instance, to find loyal customers, versus churn customers.
# In the Insurance industry, clustering is used for fraud detection in claims analysis, or to evaluate the insurance risk of certain 
# customers based on their segments. In Publication Media, clustering is used to auto-categorize news based on its content,
# or to tag news, then cluster it, so as to recommend similar news articles to readers.
# In Medicine: it can be used to characterize patient behavior, based on their similar characteristics,
# so as to identify successful medical therapies for different illnesses.
# Or, in Biology: clustering is used to group genes with similar expression patterns, or to cluster genetic markers to identify family ties.

# If you look around, you can find many other applications of clustering, but generally,
# clustering can be used for one of the following purposes: exploratory data analysis, summary generation or reducing the scale, 
# outlier detection, especially to be used for fraud detection, or noise removal, finding duplicates in datasets, 
# or, as a pre-processing step for either prediction, other data mining tasks, or, as part of a complex system.
# Let’s briefly look at different clustering algorithms and their characteristics.
# Partitioned-based clustering is a group of clustering algorithms that produces sphere-like clusters, such as k-Means, k-Median, or Fuzzy c-Means.

# These algorithms are relatively efficient and are used for Medium and Large sized databases.
# Hierarchical clustering algorithms produce trees of clusters, such as Agglomerative and Divisive algorithms. 
# This group of algorithms are very intuitive# and are generally good for use with small size datasets.
# Density based clustering algorithms produce arbitrary shaped clusters.
# They are especially good when dealing with spatial clusters or when there is noise in your dataset, for example, the DBSCAN algorithm.