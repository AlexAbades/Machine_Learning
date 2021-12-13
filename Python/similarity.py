from toolbox_02450.similarity import similarity
'''
    SIMILARITY Computes similarity matrices

    Usage:
        sim = similarity(X, Y, method)

    Input:
    X   N1 x M matrix
    Y   N2 x M matrix 
    method   string defining one of the following similarity measure
           'SMC', 'smc'             : Simple Matching Coefficient
           'Jaccard', 'jac'         : Jaccard coefficient 
           'ExtendedJaccard', 'ext' : The Extended Jaccard coefficient
           'Cosine', 'cos'          : Cosine Similarity
           'Correlation', 'cor'     : Correlation coefficient

    Output:
    sim Estimated similarity matrix between X and Y
        If input is not binary, SMC and Jaccard will make each
        attribute binary according to x>median(x)

    Copyright, Morten Morup and Mikkel N. Schmidt
    Technical University of Denmark '''

X=[1,0,1,0,1,0,1,0]
q=[1,0,1,0,0,1,1,0]
sim = similarity(X, q, 'cos');

print(sim)
