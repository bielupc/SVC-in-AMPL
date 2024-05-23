# Read the parameters
param n_train >= 1, integer;
param m_train >= 1, integer;

# Read data and labels
param y_train {1..m_train};	# classification
param A_train {1..m_train, 1..n_train};

#Kernel
param sigma := sqrt (n_train /2);
param K_train{i in 1..m_train, j in 1..m_train} := exp(-sum{k in 1..n_train} (A_train[i, k] - A_train[j, k])^2 / (2 * sigma^2));

# Define the variables
var la {1..m_train} >= 0, <= nu;

# Define the optimization problem
maximize fobj_svm_dual:
    sum {i in 1..m_train} (la[i]) - 1/2 * sum{i in 1..m_train, j in 1..m_train} (la[i]*y_train[i]*la[j]*y_train[j]*K_train[i, j]);
    
subject to restriction:
   sum {i in 1..m_train} (la[i]*y_train[i]) = 0;
