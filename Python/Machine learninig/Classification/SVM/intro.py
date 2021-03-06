# Imagine that you’ve obtained a dataset containing characteristics of thousands of human cell samples extracted from patients who 
# were believed to be at risk of developing cancer.
# Analysis of the original data showed that many of the characteristics differed significantly between benign and malignant samples.
# You can use the values of these cell characteristics in samples from other patients to give an early indication of whether a new 
# sample might be benign or malignant. You can use support vector machine, or SVM, as a classifier, to train your model to understand
# patterns within the data, that might show benign or malignant cells.

# Once the model has been trained, it can be used to predict your new or unknown cell with rather high accuracy.
# Now, let me give you a formal definition of SVM.
# A Support Vector Machine is a supervised algorithm that can classify cases by finding a separator.
# SVM works by first, mapping data to a high-dimensional feature space so that data points can be categorized, even when the data are 
# not otherwise linearly separable. Then, a separator is estimated for the data.
# The data should be transformed in such a way that a separator could be drawn as a hyperplane.

# For example, consider the following figure, which shows the distribution of a small set of cells, only based on their Unit Size and 
# Clump thickness. As you can see, the data points fall into two different categories.
# It represents a linearly, non-separable, dataset.
# The two categories can be separated with a curve, but not a line.
# That is, it represents a linearly, non-separable dataset, which is the case for most real-world datasets.
# We can transfer this data to a higher dimensional space … for example, mapping it to a 3-dimensional space.

# After the transformation, the boundary between the two categories can be defined by a hyperplane.
# As we are now in 3-dimensional space, the separator is shown as a plane. This plane can be used to classify new or unknown cases.
# Therefore, the SVM algorithm outputs an optimal hyperplane that categorizes new examples.
# Now, there are two challenging questions to consider:
# 1) How do we transfer data in such a way that a separator could be drawn as a hyperplane?
# 2) How can we find the best/optimized hyperplane separator after transformation?

# Let’s first look at “transforming data” to see how it works.
# For the sake of simplicity, imagine that our dataset is 1-dimensional data, this means, we have only one feature x.
# As you can see, it is not linearly separable. So, what we can do here?
# Well, we can transfer it into a 2-dimensional space.
# For example, your can increase the dimension of data by mapping x into a new space using a function, with outputs x and x-squared.
# Now, the data is linearly separable, right?
# Notice that, as we are in a two dimensional space, the hyperplane is a line dividing a plane into two parts where each class lays on either side.
# Now we can use this line to classify new cases. Basically, mapping data into a higher dimensional space is called kernelling.
# The mathematical function used for the transformation is known as the kernel function, and can be of different types, such as: 
# Linear, Polynomial, Radial basis function (or RBF), and Sigmoid.

# Each of these functions has its own characteristics, its pros and cons, and its equation, but the good news is that you don’t need 
# to know them, as most of them are already implemented in libraries of data science programming languages.
# Also, as there's no easy way of knowing which function performs best with any given dataset, we usually choose different functions 
# in turn and compare the results. 
# 
# Now, we get to another question, specifically, “How do we find the right or optimized separator after transformation?”
# Basically, SVMs are based on the idea of finding a hyperplane that best divides a dataset into two classes, as shown here.
# As we’re in a 2-dimensional space, you can think of the hyperplane as a line that linearly separates the blue points from the red points.
# One reasonable choice as the best hyperplane is the one that represents the largest separation, or margin, between the two classes.
# So, the goal is to choose a hyperplane with as big a margin as possible. Examples closest to the hyperplane are support vectors.

# It is intuitive that only support vectors matter for achieving our goal; and thus, other training examples can be ignored.
# We try to find the hyperplane in such a way that it has the maximum distance to support vectors.
# Please note, that the hyperplane and boundary decision lines have their own equations.
# So, finding the optimized hyperplane can be formalized using an equation which involves quite a bit more math, so I’m not going 
# to go through it here, in detail. That said, the hyperplane is learned from training data using an optimization procedure
# that maximizes the margin; and like many other problems, this optimization problem can also
# be solved by gradient descent, which is out of scope of this video.

# Therefore, the output of the algorithm is the values ‘w’ and ‘b’ for the line. You can make classifications using this estimated line.
# It is enough to plug in input values into the line equation, then, you can calculate whether an unknown point is above or below the line.
# If the equation returns a value greater than 0, then the point belongs to the first class, which is above the line, and vice versa.
# The two main advantages of support vector machines are that they’re accurate in high dimensional spaces; 
# and, they use a subset of training points in the decision function (called support vectors), so it’s also memory efficient.

# The disadvantages of support vector machines include the fact that the algorithm is prone
# for over-fitting, if the number of features is much greater than the number of samples.
# Also, SVMs do not directly provide probability estimates, which are desirable in most classification problems.
# And finally, SVMs are not very efficient computationally, if your dataset is very big, such as when you have more than one thousand rows.

# And now, our final question is, “In which situation should I use SVM?”
# Well, SVM is good for image analysis tasks, such as image classification and handwritten digit recognition.
# Also SVM is very effective in text-mining tasks, particularly due to its effectiveness in dealing with high-dimensional data.
# For example, it is used for detecting spam, text category assignment, and sentiment analysis.
# Another application of SVM is in Gene Expression data classification, again, because of its power in high dimensional data classification.
# SVM can also be used for other types of machine learning problems, such as regression, outlier detection, and clustering.