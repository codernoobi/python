# Logistic regression is a statistical and machine learning technique for classifying recordsof a dataset, based on the values 
# of the input fields.

# Let’s say we have a telecommunication dataset that we’d would like to analyze, in orderto understand which customers might leave us next month.
# This is historical customer data where each row represents one customer.
# Imagine that you’re an analyst at this company and you have to find out who is leaving and why.
# You’ll use the dataset to build a model based on historical records and use it to predict the future churn within the customer group.
# The data set includes information about: - Services that each customer has signed up for, - Customer account information,
# - Demographic information about customers, like gender and age-range,- And also Customers who’ve left the company within the last month.

# The column is called Churn.
# We can use logistic regression to build a model for predicting customer churn, using the given features.
# In logistic regression, we use one or more independent variables such as tenure, age and income to predict an outcome, such as churn,
# which we call a dependent variable, representing whether or not customers will stop using the service.
# Logistic regression is analogous to linear regression but tries to predict a categorical or discrete target field instead of a numeric one.
# In linear regression, we might try to predict a continuous value of variables, such as the price of a house, blood pressure of patient, 
# or fuel consumption of a car.
# But, in logistic regression, we predict a variable which is binary, such as, Yes/No,
# TRUE/FALSE, successful or Not successful, pregnant/Not pregnant, and so on, all of which can all be coded as 0 or 1.

# In logistic regression, dependent variables should be continuous; if categorical, they should be dummy or indicator-coded.
# This means we have to transform them to some continuous value.
# Please note that logistic regression can be used for both binary classification and multiclass classification, but for simplicity, 
# in this video, we’ll focus on binary classification.
# Let’s examine some applications of logistic regression before we explain how they work.
# As mentioned, logistic regression is a type of classification algorithm, so it can be used in different situations, 
# for example: - To predict the probability of a person having a heart attack within a specified time period, based on 
# our knowledge of the person's age, sex, and body mass index.
# - Or to predict the chance of mortality in an injured patient, or to predict whether a patient has a given disease, such as diabetes, 
# based on observed characteristics of that patient, such as weight, height, blood pressure, and results of various blood tests, and so on.

# - In a marketing context, we can use it to predict the likelihood of a customer purchasing a product or halting a subscription, 
# as we’ve done in our churn example.
# - We can also use logistic regression to predict the probability of failure of a given process, system, or product.
# - We can even use it to predict the likelihood of a homeowner defaulting on a mortgage.
# These are all good examples of problems that can be solved using logistic regression.
# Notice that in all of these examples, not only do we predict the class of each case, we also measure the probability of a case 
# belonging to a specific class.
# There are different machine algorithms which can classify or estimate a variable.

# The question is, when should we use Logistic Regression?
# Here are four situations in which Logistic regression is a good candidate:
# First, when the target field in your data is categorical, or specifically, is binary, such as 0/1, yes/no, churn or no churn, 
# positive/negative, and so on.
# Second, you need the probability of your prediction, for example, if you want to know what the probability is, of a customer buying a product.
# Logistic regression returns a probability score between 0 and 1 for a given sample of data.
# In fact, logistic regressing predicts the probability of that sample, and we map the cases to a discrete class based on that probability.
# Third, if your data is linearly separable.
# The decision boundary of logistic regression is a line or a plane or a hyper-plane.
# A classifier will classify all the points on one side of the decision boundary as belonging to one class and all those on the other 
# side as belonging to the other class.

# For example, if we have just two features (and are not applying any polynomial processing), we can obtain an inequality 
# like θ_0+ θ_1 x_1+ θ_2 x_2 > 0, which is a half-plane, easily plottable.
# Please note that in using logistic regression, we can also achieve a complex decision boundary using polynomial processing as well, 
# which is out of scope here.
# You’ll get more insight from decision boundaries when you understand how logistic regression works.
# Fourth, you need to understand the impact of a feature.
# You can select the best features based on the statistical significance of the logistic regression model coefficients or parameters.
# That is, after finding the optimum parameters, a feature x with the weight θ_1 close to 0, has a smaller effect on the prediction, 
# than features with large absolute values of θ_1.
# Indeed, it allows us to understand the impact an independent variable has on the dependent variable while controlling other independent variables.

# Let’s look at our dataset again.
# We define the independent variables as X, and dependent variable as Y.
# Notice that, for the sake of simplicity, we can code the target or dependent values to 0 or 1.
# The goal of logistic regression is to build a model to predict the class of each sample (which in this case is a customer) as well as 
# the probability of each sample belonging to a class.
# Given that, let's start to formalize the problem.
# X is our dataset, in the space of real numbers of m by n, that is, of m dimensions or features and n records.
# And y is the class that we want to predict, which can be either zero or one.
# Ideally, a logistic regression model, so called y^ (y-hat), can predict that the class of a customer is 1, given its features x.
# It can also be shown quite easily, that the probability of a customer being in class 0
# can be calculated as 1 minus the probability that the class of the customer is 1.