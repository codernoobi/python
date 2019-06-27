# how the k-nearest neighbors algorithm actually works.
# In a classification problem, the k-nearest neighbors algorithm works as follows:
# 1. Pick a value for K.
# 2. Calculate the distance from the new case (holdout from each of the cases in the dataset).
# 3. Search for the K observations in the training data that are ‘nearest’ to the measurements of the unknown data point.
# 4. predict the response of the unknown data point using the most popular response value from the K nearest neighbors.

# First, how to select the correct K; and second, how to compute the similarity between cases

# Let’s first start with second concern, that is, how can we calculate the similarity between two data points?
# Assume that we have two customers, customer 1 and customer 2.
# And, for a moment, assume that these 2 customers have only one feature, Age.
# We can easily use a specific type of Minkowski distance to calculate the distance of these 2 customers.
# It is indeed, the Euclidian distance.
# Distance of x1 from x2 is root of 34 minus 30 to power of 2, which is 4.
# What about if we have more than one feature, for example Age and Income?
# If we have income and age for each customer, we can still use the same formula, but this time, we’re using it in a 2-dimensional space.

# We can also use the same distance matrix for multi-dimensional vectors.
# Of course, we have to normalize our feature set to get the accurate dissimilarity measure.
# There are other dissimilarity measures as well that can be used for this purpose but, as mentioned, it is highly dependent on data 
# type and also the domain that classification is done for it.

# As mentioned, K in k-nearest neighbors, is the number of nearest neighbors to examine.
# It is supposed to be specified by the user.
# So, how do we choose the right K?

# Assume that we want to find the class of the customer noted as question mark on the chart.
# What happens if we choose a very low value of K, let’s say, k=1?
# The first nearest point would be Blue, which is class 1.
# This would be a bad prediction, since more of the points around it are Magenta, or class 4.
# In fact, since its nearest neighbor is Blue, we can say that we captured the noise in the data, or we chose one of the points that was an 
# anomaly in the data.

# A low value of K causes a highly complex model as well, which might result in over-fitting of the model.
# It means the prediction process is not generalized enough to be used for out-of-sample cases.
# Out-of-sample data is data that is outside of the dataset used to train the model.
# In other words, it cannot be trusted to be used for prediction of unknown samples.
# It’s important to remember that over-fitting is bad, as we want a general model that works for any data, not just the data used for training.
# Now, on the opposite side of the spectrum, if we choose a very high value of K, such as K=20, then the model becomes overly generalized.

# So, how we can find the best value for K?
# The general solution is to reserve a part of your data for testing the accuracy of the model.
# Once you’ve done so, choose k =1, and then use the training part for modeling, and calculate the accuracy of prediction using all samples in 
# your test set. Repeat this process, increasing the k, and see which k is best for your model.
# For example, in our case, k=4 will give us the best accuracy.
# Nearest neighbors analysis can also be used to compute values for a continuous target.
# In this situation, the average or median target value of the nearest neighbors is used to obtain the predicted value for the new case.

# For example, assume that you are predicting the price of a home based on its feature set, such as number of rooms, square footage, 
# the year it was built, and so on. You can easily find the three nearest neighbor houses, of course -- not only based on distance,
# but also based on all the attributes, and then predict the price of the house, as the median of neighbors.