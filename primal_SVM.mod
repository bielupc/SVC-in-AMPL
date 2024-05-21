# Read the parameters
param n;
param m;

# Read data and labels
param A {1..m, 1..n};
param y {1..m};

# Define the variables
var w {1..n};
var s {1..m} >= 0;
var gamma;

# Define the optimization problem
minimize fobj_svm_sf:
    1/2 * sum {i in 1..n} w[i] * w[i] + nu * sum {i in 1..m} s[i];

subject to clasif_errors {i in 1..m}:
    y[i] * (sum {j in 1..n} A[i, j] * w[j] + gamma) + s[i] >= 1;
