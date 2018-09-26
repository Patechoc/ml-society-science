import numpy as np

## amount of data
n_data = 1000

## Firstly X is independent of all else
X = np.random.normal(size=n_data)
Y = np.zeros(n_data)
Z = np.zeros(n_data)
A = np.zeros(n_data)

for t in range(n_data):
    ## This is P(Z | X)
    Z[t] = X[t] + np.random.normal()
    if (Z[t] < 0):
        Z[t] = -1
    else:
        Z[t] = 1

    ## This is P(Y | X)
    Y[t] = Z[t] + np.random.normal()
    if (Y[t] < 0):
        Y[t] = -1
    else:
        Y[t] = 1

    ## This is P(A | X)
    A[t] = Y[t] + np.random.normal()
    if (A[t] < 0):
        A[t] = -1
    else:
        A[t] = 1


## Now measure the distribution of A for each value of Y, for different values of Z
##
for y in [-1, 1]:
    ## P(A | Y, Z = 1)
    positive = (Y==y) & (Z==1)
    total_a1 = sum(A[positive]==1)
    total_a2 = sum(A[positive]==-1)
    positive_ratio = total_a1 / (total_a1 + total_a2)

    ## P(A | Y, Z = - 1)
    negative = (Y==y) & (Z==-1)
    total_a1 = sum(A[negative]==1)
    total_a2 = sum(A[negative]==-1)
    negative_ratio = total_a1 / (total_a1 + total_a2)

    print("y: ", y, abs(positive_ratio - negative_ratio))
