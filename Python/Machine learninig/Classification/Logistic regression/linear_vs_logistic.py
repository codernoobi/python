# Step 1. Initialize 𝜃 vector with random values, as with most machine learning algorithms, for example −1 or 2.

# Step 2. Calculate the model output, which is σ(θ^T X), for a sample customer in your training set. X in θ^T X is the feature vector values 
# -- for example, the age and income of the customer, for instance [2,5].
# And θ is the confidence or weight that you’ve set in the previous step.
# The output of this equation is the prediction value … in other words, the probability that the customer belongs to class 1.

# Step 3. Compare the output of our model, y^, which could be a value of, let’s say, 0.7, with the actual label of the customer, which is 
# for example, 1 for churn. Then, record the difference as our model’s error for this customer, which would be 1-0.7,
# which of course equals 0.3. This is the error for only one customer out of all the customers in the training set.

# Step. 4. Calculate the error for all customers as we did in the previous steps, and add up these errors. The total error is the 
# cost of your model, and is calculated by the model’s cost function. The cost function, by the way, basically represents how to calculate 
# the error of the model, which is the difference between the actual and the model’s predicted values. So, the cost shows how poorly 
# the model is estimating the customer’s labels. Therefore, the lower the cost, the better the model is at estimating the customer’s 
# labels correctly.
# And so, what we want to do is to try to minimize this cost.

# Step 5. But, because the initial values for θ were chosen randomly, it’s very likely that the cost function is very high. So, 
# we change the 𝜃 in such a way to hopefully reduce the total cost.

# Step 6. After changing the values of θ, we go back to step 2.
# Then we start another iteration, and calculate the cost of the model again.
# And we keep doing those steps over and over, changing the values of θ each time, until the cost is low enough. 

# So, this brings up two questions: 
# first, "How can we change the values of θ so that the cost is reduced across iterations?"
# And second, "When should we stop the iterations?" There are different ways to change the values of θ, but one of the most 
# popular ways is gradient descent.
# Also, there are various ways to stop iterations, but essentially you stop training by calculating the accuracy of your model, 
# and stop it when it’s satisfactory.
#------------------------------------------------------------------------------------------------------

# To change the parameters of the model, so as to be the best estimation of the labels of the samples in the dataset, for example, 
# the customer churn. "How do we do that?"
# In brief, first we have to look at the cost function and see what the relation is between the cost function and the parameters θ. 
# So, we should formulate the cost function. Then, using the derivative of the cost function, we can find how to change the parameters to
# reduce the cost, or rather, the error. Let’s dive into it to see how it works.
# But before I explain it, I should highlight for you that it needs some basic mathematical background to understand it. 
# However, you shouldn’t worry about it as most data science languages like Python, R and Scala have some packages or libraries
# that calculate these parameters for you. So, let’s take a look at it.

# Let’s first find the cost function equation for a sample case.
# To do this, we can use one of the customers in the churn problem.
# There’s normally a general equation for calculating the cost.
# The cost function is the difference between the actual values of y and our model output, y^.
# This is a general rule for most cost functions in machine learning. We can show this as the “Cost of our model
# comparing it with actual labels,” which is the “difference between the predicted value of our model and actual value of the 
# target field,” where the predicted value of our model is is σ(θ^T X). Usually, the square of this equation is used
# because of the possibility of the negative result, and for the sake of simplicity, half of this value is considered as the cost function, 
# through the derivative process. Now, we can write the cost function for all the samples in our training set; for example, 
# for all customers, we can write it as the average sum of the cost functions of all cases. 

# It is also called the mean squared error, and, as it is a function of a parameter vector θ, it is shown as J(θ).
# Ok, good. We have the cost function. Now, how do we find or set the best weight  or parameters that minimize this cost function? 
# The answer is, “We should calculate the minimum point of this cost function and it’ll show us the best parameters for our model.”
# Although we can find the minimum point of a function using the derivative of a function, there’s not an easy way to find 
# the global minimum point for such an equation.
# Given this complexity, describing how to reach the global minimum for this equation, is outside the scope of this video. 
# So, what is the solution? Well, we should find another cost function instead; one which has the same behavior but
# is easier to find its minimum point. Let’s plot the desirable cost function for our model.

# Recall that our model is y^. Our actual value is y, which equals 0 or 1, and our model tries to estimate it, 
# as we want to find a simple cost function for our model. For a moment, assume that our desired value for y is 1. 
# This means our model is best if it estimates y=1. In this case, we need a cost function that returns 0 if the outcome of our model is 1, 
# which is same as the actual label. And the cost should keep increasing as the outcome of our model gets farther from 1.
# And cost should be very large, if the outcome of our model is close to 0.
# We can see that the –log() function provides such a cost function for us.
# It means, if the actual value is 1, and the model also predicts 1, the –log() function returns 0 cost, but, if the prediction 
# is smaller than 1, the –log() function returns a larger cost value. So, we can use the –log() function for calculating
# the cost of our logistic regression model. So, if you recall, we previously noted that, in general, it is difficult to calculate the
# derivative of the cost function.
# 
# Well, we can now change it with the -log of our model. We can easily prove that in the case that desirable y is 1, \the cost can be calculated as -log(y^), and in the case that desirable
# y is 0, the cost can be calculated as -log(1-y^). Now we can plug it into our total cost function and rewrite it as this function.
# So, this is the logistic regression cost function. As you can see for yourself, it penalizes situations in which the class is 0 
# and the model output is 1, and vice versa. Remember, however, that y^ does not return a class as output, but it’s a value of (0,1),
# which should be assumed as a probability. Now we can easily use this function to find the parameters of our model in such a way as 
# to minimize the cost. OK, let’s recap what we’ve done. Our objective was to find a model that best
# estimates the actual labels. Finding the best model means finding the best parameters θ, for that model. 
# 
# So, the first question was, "How do we find the best parameters for our model?" Well, by finding and minimizing the cost function
# of our model. In other words, to minimize the J(θ) that we just defined. The next question is: "How do we minimize
# the cost function?" The answer is, using an optimization approach. There are different optimization approaches, 
# but we use one of the most famous and effective approaches here, gradient descent. The next question is: "What is gradient descent?"
# Generally, gradient descent is an iterative approach to finding the minimum of a function.
# Specifically, in our case, gradient descent is a technique to use the derivative of a cost function to change the parameter values, 
# to minimize the cost or error. Let’s see how it works.

# The main objective of gradient descent is to change the parameter values so as to minimize the cost. "How can gradient descent do that?"
# Think of the parameters or weights in our model to be in a 2-dimensional space, for example, θ1, θ2, for 2 feature sets, age and income.
# Recall the cost function, J, that we discussed in the previous slides. We need to minimize the cost function J, 
# which is a function of variables 𝜃1, 𝜃2. So, let’s add a dimension for the observed cost or error, J function.
# Let’s assume that if we plot the cost function based on all possible values of 𝜃1, 𝜃2,
# we can see something like this. It represents the error value for different values of parameters, that is, Error, 
# which is a function of the parameters. This is called your “error curve” or “error bowl” of your cost function.

# Recall that we want to use this error bowl to find the best parameter values that result in minimizing the cost value. Now,
# the question is, “Which point is the best point for your cost function?” Yes, you should try to minimize your position
# on the “error curve.” So, what should you do? You have to find the minimum value of the cost by changing the parameters … but which
# way? Will you add some value to your weights, or deduct some value? And how much would that value be?
# You can select random parameter values that locate a point on the bowl.

# You can think of our starting point being the yellow point. You change the parameters by Δ𝜃1 and Δ𝜃2, and take one step on the surface.
# Let’s assume we go down one step in the bowl. As long as we're going downwards we can go one more step.
# The steeper the slope, the further we can step. And we can keep taking steps. As we approach the lowest point, the slope
# diminishes, so we can take smaller steps until we reach a flat surface. This point is the minimum point of our curve, and the optimum 𝜃1, 𝜃2.
# What are these steps really? I mean in which direction should we take these steps to make sure we descend, and how big should the steps be?
# To find the direction and size of these steps, in other words, to find how to update the parameters, you should calculate the 
# gradient of the cost function at that point. The gradient is the slope of the surface at every point.

# And, the direction of the gradient is the direction of the greatest uphill. Now the question is, 
# “How do we calculate the gradient of a cost function at a point?” If you select a random point on this surface, for example, 
# the yellow point, and take the partial derivative of J(θ) with respect to each parameter at that point, it gives you
# the slope of the move for each parameter at that point. Now, if we move in the opposite direction of that slope, it guarantees that we go down
# in the error curve. For example, if we calculate the derivative of J with respect to 𝜃1, we find out that it is a positive number.
# This indicates that function is increasing as 𝜃1 increases. So, to decrease J, we should move in the opposite direction.
# This means to move in the direction of the negative derivative for 𝜃1, i.e. slope. We have to calculate it for other parameters as well, 
# at each step. The gradient value also indicates how big of a step to take.

# If the slope is large, we should take a large step because we’re far from the minimum. If the slope is small we should to take a smaller step.
# Gradient descent takes increasingly smaller steps towards the minimum with each iteration.
# The partial derivative of the cost function J, is calculated using this expression. If you want to know how the derivative of the J 
# function is calculated, you need to know the derivative concept, which is beyond our scope here.
# But to be honest, you don’t really need to remember all the details about it, as you can easily use this equation to calculate the gradients.
# So, in a nutshell, this equation returns the slope of that point, and we should update the parameter in the opposite direction of the slope.
# A vector of all these slopes is the gradient vector, and we can use this vector to change or update all the parameters. 
# We take the previous values of the parameters and subtract the Error derivative. This results in the new parameters for θ
# that we know will decrease the cost. Also, we multiply the gradient value by a constant value Mu, which is called the learning rate.

# Learning rate gives us additional control on how fast we move on the surface. In sum, we can simply say, Gradient descent is like 
# taking steps in the current direction of the slope, and the learning rate is like the length of the step you take.
# So, these would be our new parameters. Notice that it’s an iterative operation and, in each iteration, we update the parameters 
# and minimize the cost, until the ‘algorithm converge’ is on an acceptable minimum. OK, let’s recap what we’ve done to this point, 
# by going through the training algorithm again, step-by-step. Step 1. We initialize the parameters with
# random values. Step 2. We feed the cost function with the training set, and calculate the cost. 
# We expect a high error rate as the parameters are set randomly. Step 3. We calculate the gradient of the cost
# function, keeping in mind that we have to use a partial derivative.

# So, to calculate the gradient vector, we need all the training data to feed the equation for each parameter. Of course, 
# this is an expensive part of the algorithm, but there are some solutions for this. Step 4. We update the weights with new parameter values.
# Step 5. Here we go back to step 2 and feed the cost function again, which has new parameters.
# As was explained earlier, we expect less error as we’re going down the error surface.
# We continue this loop until we reach a short value of cost, or some limited number of iterations.
# Step 6. The parameters should be roughly found after some iterations.N This means the model is ready. And we can use it to predict the probability
# of a customer staying or leaving.