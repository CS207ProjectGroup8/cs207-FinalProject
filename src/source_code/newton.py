# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 13:33:34 2018

@author: jiayi
"""

import numpy as np
import sys
sys.path.append(r'C:\Users\jiayi\Desktop\Kay\Study\Fall2018\cs207\cs207_jiayin_lu\project\cs207-FinalProject')
import AutoDiffObject as autodiff
import ElementaryFunctions_2 as ef


#Our method J_F that takes in the user defined function and vector list x

def J_F(F, x):              #F as a length n list, x as a length m list 
    n = len(F)
    m = len(x)
    
    #Convert x to AutoDiffObject
    xCal = [0.0] * m
    for i in range(0, m):
        xCal[i] = autodiff.AutoDiff(x[i], "{}".format(i))
        
    J_F = np.zeros((n, m))                     #to store Jacobian matrix information later
    F1 = np.array([0.0]*n)                      #to store function value later

    Fcal = F(xCal)    #This is a list of AutoDiffObjects, [F0(xCal), F1[xCal], ... F(n-1)[xCal]]

    #Fcal[i].val has information of function value of Fi evaluated at input x; it is of a numeric type
    #Fcal[i].der has information of partial derivatives of Fi with respect to each x component; it is of type dictionary

    for i in range(0, n):
        F1[i] = Fcal[i].val        
          
        for j in range(0, m):
            J_F[i, j] = Fcal[i].der["{}".format(j)]

    return [F1, J_F]     

#This returns a list with the function value F(x) and and Jacobian J_F(x)



#Optimization & Root Finding
#full Newton: root-finding
#Require len(F) = len(x)
def Newton(F, x, criteria = 10^(-10)):
    x_k = x
    rel_step = 1
    
    if len(F) != len(x):
        print("Need to be a system of n functions with n unknowns!")
        raise ValueError
        
    else: 
        while rel_step > criteria:
            JF_k = J_F(F, x_k)
            F_k = JF_k[0]
            J_k = JF_k[1]
            deltaX = np.linalg.solve(J_k, -F_k)
            x_k = x_k + deltaX
            rel_step = np.linalg.norm(deltaX)/np.linalg.norm(x_k)
        
        return x_k




#Optimization: Minimization
def Mini(F, x, method = "newton", criteria = 10^(-10), *args):
    #*args can take in as argument a matrix as initial guess of the inverse Hessian matrix; 
    #otherwise, default will use a identity matrix as the initial guess
    
    '''Require implementation of Hessian 
    if method = "newton":
        x_k = x 
        rel_step = 1
        
        while rel_step > criteria:
            JH_k = JH_F(F, x_k)  #Need another function that calcuate both Jacobian and Hessian
        
            J_k = JH_k[1]
            H_k = JH_k[2]   #Need to have Hessian Matrix calculated
        
            deltaX = np.linalg.solve(H_k, -J_k)
            x_k = x_k + deltaX
            rel_step = np.linalg.norm(deltaX)/np.linalg.norm(x_k)
            
        result = {"x_min": x_k, "min F(x)": JH_k[0], "Jcobian F(x_min)": JH_k[1], "Hessian F(x_min)": JH_k[2]}
        return result
    '''    
        
    elif method = "quasi-newton-BFGS":  #H_k is Inverse Hessian approximation
        x_k = x
        rel_step = 1
        I = np.eye(len(x),len(F))
        
        if len(args) != 0:
            H_k = args[0]
        else: 
            H_k = I
        
        JF_k = J_F(F, x_k)
        J_k = JF_k[1]
        while rel_step > criteria: 
            
            deltaX = - np.matmul(H_k, J_k)
            x_k = x_k + deltaX
            
            JF_k2 = J_F(F, x_k)
            J_k2 = JF_k2[1]
            
            yk = J_k2 - J_k    #matrix
            rouk = 1/(yk.T @ deltaX)    #vector
            H_k = np.matmul(np.matmul((I - (deltaX @ rouk) * yk.T ), H_k), (I - (rouk @ yk) @ deltaX.T)) + (rouk @ deltaX) @ deltaX.T 
            
            J_k = J_k2
            rel_step = np.linalg.norm(deltaX)/np.linalg.norm(x_k)
        
        result = {"x_min": x_k, "min F(x)": JF_k2[0], "Jcobian F(x_min)": JF_k2[1], "Hessian approximate": H_k}
        return result
        
    elif method = "steepest-descent":
        
        
    elif method = "": #other methods? 
        
        
    
    
    
    
    
    

        




