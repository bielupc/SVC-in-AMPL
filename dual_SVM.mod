# Read the parameters
param n_train >= 1, integer;
param m_train >= 1, integer;

# Read data and labels
param y_train {1..m_train};	# classification
param A_train {1..m_train, 1..n_train};

#Kernel
param K {i in 1..m_train, j in 1..m_train} :=
    sum {k in 1..n_train} A[i, k] * A[j, k];

# Define the variables
var la {1..m_train} >= 0, <= nu;

# Define the optimization problem
maximize fobj_svm_dual:
    sum {i in 1..m_train} (la[i]) - 1/2 * sum{i in 1..m_train, j in 1..m_train} (la[i]*y[i]*la[j]*y[j]*K[i, j]);
    
subject to restriction:
   sum {i in 1..m_train} (la[i]*y[i]) = 0;
