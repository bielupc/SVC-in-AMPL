# Read the parameters
param n >= 1, integer;
param m >= 1, integer;
param nu;

# Read data and labels
param y {1..m};	# classification
param A {1..m, 1..n};

#Kernel
param K{1..m, 1..m} := exp(-sum{k in 1..n} (A[i, k] - A[j, k])^2 / (2 * sigma^2));

# Define the variables
var la {1..m} >= 0, <= nu;

# Define the optimization problem
maximize fobj_svm_dual:
    sum {i in 1..m} (la[i]) - 1/2 * sum{i in 1..m, j in 1..m} (la[i]*y[i]*la[j]*y[j]*K[i, j]);
    
subject to restriction:
   sum {i in 1..m} (la[i]*y[i]) = 0;
