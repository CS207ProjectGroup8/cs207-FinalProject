# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:42:15 2018

@author: jiayi
"""

class AutoDiff():
    def __init__(self, val, varName, *args):
        self.val = val
        if varName != "dummy":
            self.der = {varName:1}
        else:
            self.der = args[0]    
    
    def __mul__(self, other):
        try:
        #if isinstance(other, AutoDiffToy):
            derDict = {}
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)
            
            for key in setSelfDer.union(setOtherDer):
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = self.der[key]*other.val + other.der[key]*self.val
                elif key in setSelfDer:
                    derDict[key] = self.der[key]*other.val
                else: 
                    derDict[key] = other.der[key]*self.val
            
            return AutoDiff(self.val * other.val, "dummy", derDict)
        
        except AttributeError:
        #elif isinstance(other, (int,float, etc numeric types)):
            derDict = {}
            for key in self.der:
                derDict[key] = other.real * self.der[key]
            return AutoDiff(self.val * other.real, "dummy", derDict)
    
    def __rmul__(self, other):                       #reversed multiplication
        try:
        #if isinstance(other, AutoDiffToy):
            derDict = {}
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)
            
            for key in setSelfDer.union(setOtherDer):
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = self.der[key]*other.val + other.der[key]*self.val
                elif key in setSelfDer:
                    derDict[key] = self.der[key]*other.val
                else: 
                    derDict[key] = other.der[key]*self.val
            
            return AutoDiff(self.val * other.val, "dummy", derDict)
        
        except AttributeError:
        #elif isinstance(other, (int,float, etc numeric types)):
            derDict = {}
            for key in self.der:
                derDict[key] = other.real * self.der[key]
            return AutoDiff(self.val * other.real, "dummy", derDict)
        
        
    def __add__(self, other):
        try:
        #if isinstance(other, AutoDiffToy):
            derDict = {}
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)
            
            for key in setSelfDer.union(setOtherDer):
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = self.der[key] + other.der[key]
                elif key in setSelfDer:
                    derDict[key] = self.der[key]
                else: 
                    derDict[key] = other.der[key]
            
            return AutoDiff(self.val + other.val, "dummy", derDict)
        
        except AttributeError:
        #elif isinstance(other, (int,float, etc numeric types)):
            return AutoDiff(self.val + other.real, "dummy", self.der)
        
    
    def __radd__(self, other):
        try:
        #if isinstance(other, AutoDiffToy):
            derDict = {}
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)
            
            for key in setSelfDer.union(setOtherDer):
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = self.der[key] + other.der[key]
                elif key in setSelfDer:
                    derDict[key] = self.der[key]
                else: 
                    derDict[key] = other.der[key]
            
            return AutoDiff(self.val + other.val, "dummy", derDict)
        
        except AttributeError:
        #elif isinstance(other, (int,float, etc numeric types)):
            return AutoDiff(self.val + other.real, "dummy", self.der)
        
        



x = AutoDiff(2, "x")
y = AutoDiff(3, "y")
z = AutoDiff(4, "z")


f = 5*x + 7*y +4*x*y*z + 3.0*z + 4

print(f.val, f.der)






'''
Notes

test = {"x":1, "y":2}
test2 = {"y":3, "z":4}

    
for key in test:
    print(test[key])
    
set1 = set(test)
set2 = set(test2)

new = {}
for key in set1.union(set2):
    if key in set1 and key in set2:
        new[key] = test[key] + test2[key]
    elif key in set1:
        new[key] = test[key]
    else: 
        new[key] = test2[key]
new
'''