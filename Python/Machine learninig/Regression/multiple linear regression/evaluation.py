# train and test on the same dataset, and train/test split.

# select a small portion of the dataset,but without the labels
# This set, is called a test set, which has the labels, but the labels are not used for prediction, and is used only as ground truth.
# The labels are called “Actual values” of the test set.

# Now, we pass the feature set of the testing portion to our built model, and predict the target values.
# Finally, we compare the predicted values by our model with the actual values in the test set.
# This indicates how accurate our model actually is
# we just compare the actual values, y, with the predicted values, which is noted as y ̂ for the testing set.

# The error of the model is calculated as the average difference between the predicted and actual values for all the rows.
# We can write this error as an equation.

# a high training accuracy isn’t necessarily a good thing.
# For instance, having a high training accuracy may result in an ‘over-fit’ of the data.
# This means that the model is overly trained to the dataset, which may capture noise and produce a non-generalized model.
# Out-of-sample accuracy is the percentage of correct predictions that the model makes on data that the model has NOT been trained on.

# It’s important that our models have high, out-of-sample accuracy, because the purpose of our model is, of course,
# to make correct predictions on unknown data.
# The issue with train/test split is that it’s highly dependent on the datasets on which the data was trained and tested.
# The variation of this causes train/test split to have a better out-of-sample predictionthan training and testing on the same dataset, 
# but it still has some problems due to this dependency.

# Another evaluation model, called "K-Fold Cross-validation," resolves most of these issues

# fix a high variation that results from a dependency by averainge it.
# the basic concept of “k-fold cross-validation” 

# If we have k=4 folds, then we split up The entire dataset to 4 parts
# In the first fold, for example, we use the first 25 percent of the dataset for testing, and the rest for training.
# The model is built using the training set, and is evaluated using the test set.
# Then, in the next round (or in the second fold), the second 25 percent of the dataset
# is used for testing and the rest for training the model.
# Again the accuracy of the model is calculated.
# We continue for all folds.
# Finally the result of all 4 evaluations are averaged.
# That is, the accuracy of each fold is then averaged, keeping in mind that each fold is distinct, where no training data in one fold is used in another.
# K-fold cross-validation, in its simplest form, performs multiple train/test splits using the same dataset where each split is different.
# Then, the result is averaged to produce a more consistent out-of-sample accuracy.
