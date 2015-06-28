# -*- coding: utf-8 -*-
"""
Weighted Linear Regression , Expert in HME model

   m - dimensionality of input (i.e. length of row in matrix X)
   n - number of observations
"""

import numpy as np

def cholesky_solver_least_squares(part_one, part_two):
    '''
    Solves least squares problem using cholesky decomposition
    
    part_one - numpy array of size 'm x m', equals X.T * X
    part_two - numpy array of size 'm x 1', equals X.T * Y
    
    '''
    # R*R.T*Theta = part_two
    R = np.linalg.cholesky(part_one)
    # R*Z = part_two
    Z     = np.linalg.solve(R,part_two)
    # R.T*Theta = Z
    Theta = np.linalg.solve(R.T,Z)
    return Theta
    
    
def norm_pdf(theta,y,x,sigma_2):
    '''
    Calculates probability of observing Y given Theta and sigma
    
    
    Input:
    ------
    
    Theta    -  numpy array of size 'm x k', matrix of parameters
    Y        -  numpy array of size 'n x 1', vector of dependent variables
    X        -  numpy array of size 'n x m', matrix of inputs 
    sigma_2  -  numpy array of size 'm x 1', vector of variances
    
    Output:
    -------
    
             - int
    
    '''
    normaliser = 1.0/np.sqrt(2*np.pi*sigma_2)
    u          = y - np.dot(x,theta)
    return normaliser* np.exp( -0.5 * u*u / sigma_2 )
    
    


class WeightedLinearRegression(object):
    '''
    Weighted Linear Regression
    
    Fits weighted  regression 
        
    Input:
    ------
    
    Y                        - numpy array of size 'n x 1', vector of dependent variables
    X                        - numpy array of size 'n x m', matrix of inputs
    weights                  - numpy array of size 'n x 1', vector of observation weights
    
    '''
    
    def __init__(self,X,Y,weights):
        self.theta        = 0             # coefficients excluding bias term
        self.mse          = 0             # mean squared error
        self.var          = 0             # fitted variance
        self.Y            = Y
        self.X            = X
        self.weights      = weights

    def fit(self):
        ''' Fits weighted regression '''
        n,m         =  np.shape(self.X)
        W           =  np.diagflat(self.weights)
        part_one    =  np.dot(np.dot(self.X.T,W),self.X)
        part_two    =  np.dot(np.dot(self.X.T,W),self.Y)
        self.theta  =  cholesky_solver_least_squares(part_one, part_two)
        vec_1       =  (self.Y - np.dot(self.X,self.theta))
        self.var    =  np.dot(vec_1,np.dot(vec_1,W))/np.sum(W)
        
        

    def predict(self,X_test):
        '''
        Predicts target values for X_test
        '''
        fitted = np.dot(X_test,)
        return fitted

