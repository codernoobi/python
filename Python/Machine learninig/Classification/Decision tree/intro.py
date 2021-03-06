# Here is the way that a decision tree is built.
# A decision tree can be constructed by considering the attributes one by one.
# First, choose an attribute from our dataset.
# Calculate the significance of the attribute in the splitting of the data.
# calculate the significance of an attribute, to see if it’s an effective attribute or not.
# Next, split the data based on the value of the best attribute.
# Then, go to each branch and repeat it for the rest of the attributes.
# After building this tree, you can use it to predict the class of unknown cases 

# Consider the drug dataset again.
# “How do we build the decision tree based on that dataset?”
# Decision trees are built using recursive partitioning to classify the data.

# Let’s say we have 14 patients in our dataset.
# The algorithm chooses the most predictive feature to split the data on.
# What is important in making a decision tree, is to determine “which attribute is the best, or more predictive, to split data based on the feature.”

# Let’s say we pick “Cholesterol” as the first attribute to split data.
# It will split our data into 2 branches.
# As you can see, if the patient has high “Cholesterol,” we cannot say with high confidence that Drug B might be suitable for him.
# Also, if the Patient’s “Cholesterol” is normal, we still don’t have sufficient evidence or information to determine if either Drug A or 
# Drug B is, in fact, suitable.

# It is a sample of bad attribute selection for splitting data. So, let’s try another attribute.
# Again, we have our 14 cases. This time, we pick the “sex” attribute of patients.
# It will split our data into 2 branches, Male and Female.
# As you can see, if the patient is Female, we can say Drug B might be suitable for her with high certainty.
# But, if the patient is Male, we don’t have sufficient evidence or information to determine if Drug A or Drug B is suitable.
# However, it is still a better choice in comparison with the “Cholesterol” attribute, because the result in the nodes are more pure.
# It means, nodes that are either mostly Drug A or Drug B.
# So, we can say the “Sex” attribute is more significant than “Cholesterol,” or in other words, it’s more predictive than the other attributes.

# Indeed, “predictiveness” is based on decrease in “impurity” of nodes.
# We’re looking for the best feature to decrease the ”impurity” of patients in the leaves, after splitting them up based on that feature.
# So, the “Sex” feature is a good candidate in the following case, because it almost found the pure patients.

# For the Male patient branch, we again test other attributes to split the subtree.
# We test “Cholesterol” again here.
# As you can see, it results in even more pure leaves.
# So, we can easily make a decision here.
# For example, if a patient is “Male”, and his “Cholesterol” is “High”, we can certainly prescribe Drug A, but if it is “Normal”, 
# we can prescribe Drug B with high confidence.
# As you might notice, the choice of attribute to split data is very important, and it is all about “purity” of the leaves after the split.
# A node in the tree is considered “pure” if, in 100% of the cases, the nodes fall into a specific category of the target field.
# In fact, the method uses recursive partitioning to split the training records into segments by minimizing the “impurity” at each step.

# ”Impurity” of nodes is calculated by “Entropy” of data in the node.
# So, what is “Entropy”?
# Entropy is the amount of information disorder, or the amount of randomness in the data.
# The entropy in the node depends on how much random data is in that node and is calculated for each node.
# In decision trees, we're looking for trees that have the smallest entropy in their nodes.
# The entropy is used to calculate the homogeneity of the samples in that node.
# If the samples are completely homogeneous the entropy is zero and if the samples are equally divided, it has an entropy of one.
# This means, if all the data in a node are either Drug A or Drug B, then the entropy is zero, but if half of the data are Drug A 
# and other half are B, then the entropy is one.
# You can easily calculate the entropy of a node using the frequency table of the attribute through the Entropy formula, 
# where P is for the proportion or ratio of a category, such as Drug A or B. Please remember, though, that you don’t
# have to calculate these, as it’s easily calculated by the libraries or packages that you use.

# As an example, let’s calculate the entropy of the dataset before splitting it.
# We have 9 occurrences of Drug B and 5 of Drug A.
# You can embed these numbers into the Entropy formula to calculate the impurity of the target
# attribute before splitting it.
# In this case, it is 0.94.
# So, what is entropy after splitting?
# Now we can test different attributes to find the one with the most “predictiveness,” which results in two more pure branches.
# Let’s first select the “Cholesterol” of the patient and see how the data gets split, based on its values.

# For example, when it is “normal,” we have 6 for Drug B, and 2 for Drug A.
# We can calculate the Entropy of this node based on the distribution of drug A and B,
# which is 0.8 in this case.
# But, when Cholesterol is “High,” the data is split into 3 for drug B and 3 for drug A.
# Calculating its entropy, we can see it would be 1.0.
# We should go through all the attributes and calculate the “Entropy” after the split, and then chose the best attribute.

# try another field.
# Let’s choose the Sex attribute for the next check.
# As you can see, when we use the Sex attribute to split the data, when its value is “Female,”
# we have 3 patients that responded to Drug B, and 4 patients that responded to Drug A.
# The entropy for this node is 0.98 which is not very promising.
# However, on other side of the branch, when the value of the Sex attribute is Male, the result is more pure with 6 for Drug B and only 1 
# for Drug A. The entropy for this group is 0.59.
# Now, the question is, between the Cholesterol and Sex attributes, which one is a better choice?
# Which one is better as the first attribute to divide the dataset into 2 branches?
# Or, in other words, which attribute results in more pure nodes for our drugs?
# Or, in which tree, do we have less entropy after splitting rather than before splitting?
# The “Sex” attribute with entropy of 0.98 and 0.59, or the “Cholesterol” attribut with entropy of 0.81 and 1.0 in its branches?

# The answer is, “The tree with the higher information gain after splitting."
# So, what is information gain?
# Information gain is the information that can increase the level of certainty after splitting.
# It is the entropy of a tree before the split minus the weighted entropy after the split by an attribute.
# We can think of information gain and entropy as opposites.
# As entropy, or the amount of randomness, decreases, the information gain, or amount of certainty, increases, and vice-versa.
# So, constructing a decision tree is all about finding attributes that return the highest information gain.
# Let’s see how “information gain” is calculated for the Sex attribute.
# As mentioned, the information gain is the entropy of the tree before the split, minus the weighted entropy after the split.

# The entropy of the tree before the split is 0.94.
# The portion of Female patients is 7 out of 14, and its entropy is 0.985.
# Also, the portion of men is 7 out of 14, and the entropy of the Male node is 0.592.
# The result of a square bracket here is the weighted entropy after the split.
# So, the information gain of the tree if we use the “Sex” attribute to split the dataset is 0.151.
# As you can see, we will consider the entropy over the distribution of samples falling under
# each leaf node, and we’ll take a weighted average of that entropy – weighted by the
# proportion of samples falling under that leaf.
# We can calculate the information gain of the tree if we use “Cholesterol” as well.
# It is 0.48.

# Now, the question is, “Which attribute is more suitable?”
# Well, as mentioned, the tree with the higher information gain after splitting.
# This means the “Sex” attribute.
# So, we select the “Sex” attribute as the first splitter.
# Now, what is the next attribute after branching by the “Sex” attribute?
# Well, as you can guess, we should repeat the process for each branch, and test each of the other attributes to continue to reach the 
# most pure leaves. This is the way that you build a decision tree!