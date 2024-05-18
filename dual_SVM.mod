# Read the parameters
param n >= 1, integer;
param m >= 1, integer;
param nu;

# Read data and labels
param K {1..m, 1..m}; # kernel = AA^t 
param y {1..m};	# classification

# Define the variables
var la {1..m} >= 0, <= nu;

# Define the optimization problem
minimize fobj_svm_dual:
    sum {i in 1..m} (la[i]) - 1/2 * sum{i in 1..m, j in 1..m}(la[i]*y[i]*la[j]*y[j]*K[i,j]));

subject to restriction:
   sum {i in 1..m} (la[i]*y[i]) = 0;
