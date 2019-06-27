# multiple independent variables are present
# Extension of single linear Extension

# Independent variables effectiveness on prediction
# predicting impacts of changes(dependent var changes when independent var changes)

# MSE mean squared error
# mean of residual error
# minimize MSE for best model

# Estimate theta
# Ordinary Least Squares (OLS)
# OLS is a method for estimating the unknown parameters in a linear regression model. OLS chooses the parameters of a linear function of a set of explanatory variables by minimizing the sum of the squares of the differences between the target dependent variable and those predicted by the linear function. In other words, it tries to minimizes the sum of squared errors (SSE) or mean squared error (MSE) between the target variable (y) and our predicted output ( 𝑦̂  ) over all samples in the dataset.
# OLS can find the best parameters using of the following methods:
# - Solving the model parameters analytically using closed-form equations
# - Using an optimization algorithm (Gradient Descent, Stochastic Gradient Descent, Newton’s Method, etc.)

# -optimization algorithm(gradient descent for large data set)

# prediction
# linear regression model representation for this problem would be: y ̂=θ^T x
# θ0 = 125, θ1 = 6.2, θ2 = 14, and so on

# more variables results in overfit model
# independent var and dependent var should be linearly related
# if not use non linear models

# variance regression score:
# If  𝑦̂   is the estimated target output, y the corresponding (correct) target output, and Var is Variance, the square of the standard deviation, then the explained variance is estimated as follow:

# 𝚎𝚡𝚙𝚕𝚊𝚒𝚗𝚎𝚍𝚅𝚊𝚛𝚒𝚊𝚗𝚌𝚎(𝑦,𝑦̂ )=1−𝑉𝑎𝑟{𝑦−𝑦̂ }𝑉𝑎𝑟{𝑦} 
# The best possible score is 1.0, lower values are worse