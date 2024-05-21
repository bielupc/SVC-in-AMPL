# Read the parameters
param n_train;
param m_train;

# Read data and labels
param A_train {1..m_train, 1..n_train};
param y_train {1..m_train};

# Define the variables
var w {1..n_train};
var s {1..m_train} >= 0;
var gamma;

# Define the optimization problem
minimize fobj_svm_sf:
    1/2 * sum {i in 1..n_train} w[i] * w[i] + nu * sum {i in 1..m_train} s[i];

subject to clasif_errors {i in 1..m_train}:
    y_train[i] * (sum {j in 1..n_train} A_train[i, j] * w[j] + gamma) + s[i] >= 1;
