# if we assume that the model for data points are exponential functions,
# such as y ̂ = θ_0 + θ_1 〖θ_2〗^x, our job is to estimate the parameters of the model,
# i.e. θs, and use the fitted model to predict GDP for unknown or future cases.
# In fact, many different regressions exist that can be used to fit whatever the dataset
# looks like.
# we can call all of these "polynomial regression," where the relationship between
# the independent variable x and the dependent variable y is modelled as an nth degree polynomial
# in x
# With many types of regression to choose from, there’s a good chance that one will fit
# your dataset well.
# Remember, it’s important to pick a regression that fits the data the best.
# Polynomial regression fits a curved line to your data.
# A simple example of polynomial, with degree 3, is shown as y ̂ = θ_0 + θ_1x + θ_2x^2
# + θ_3x^3 or to the power of 3, where θs are parameters to be estimated that makes the model fit perfectly
# to the underlying data.
# Though the relationship between x and y is non-linear here, and polynomial regression can fit them, 
# a polynomial regression model can still be expressed as linear regression.

# Given the 3rd degree polynomial equation, by defining x_1 = x and x_2 = x^2 or x to the power of 2 and so on,
# the model is converted to a simple linear regression with new variables, as y ̂ = θ_0+θ_1x_1 + θ_2x_2 + θ_3x_3. 
# This model is linear in the parameters to be estimated, right?
# Therefore, this polynomial regression is considered to be a special case of traditional multiple linear regression.
# So, you can use the same mechanism as linear regression to solve such a problem.

# Therefore, polynomial regression models CAN fit using the model of least squares.
# Least squares is a method for estimating the unknown parameters in a linear regression model, by minimizing the sum of the
# squares of the differences between the observed dependent variable in the given dataset and those predicted by the linear function.
# So, what is “non-linear regression” exactly?
# First, non-linear regression is a method to model a non-linear relationship between the dependent variable and a set of independent variables.
# Second, for a model to be considered non-linear, y ̂ must be a non-linear function of the parameters θ, not necessarily the features x.

# When it comes to non-linear equation, it can be the shape of exponential, logarithmic, and logistic, or many other types.
# As you can see, in all of these equations, the change of y ̂ depends on changes in the parameters θ, not necessarily on x only.
# That is, in non-linear regression, a model is non-linear by parameters.
# In contrast to linear regression, we cannot use the ordinary "least squares" method to fit the data in non-linear regression, and in general, 
# estimation of the parameters is not easy.

# “How can I know if a problem is linear or non-linear in an easy way?”
# To answer this question, we have to do two things:
# The first is to visually figure out if the relation is linear or non-linear.
# It’s best to plot bivariate plots of output variables with each input variable.
# Also, you can calculate the correlation coefficient between independent and dependent variables, and if for all variables it is 0.7 or
# higher there is a linear tendency, and, thus, it’s not appropriate to fit a non-linear regression.

# The second thing we have to do is to use non-linear regression instead of linear regression when we cannot accurately model the
# relationship with linear parameters.
# The second important questions is, “How should I model my data, if it displays non-linear on a scatter plot?”
# Well, to address this, you have to use either a polynomial regression, use a non-linear regression model, or "transform" your data, 
# which is not in scope for this course.