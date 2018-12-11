# Tests for ADfun.py
import numpy as np
import pytest
from hotAD.AutoDiffObject import AutoDiff
from hotAD.ElementaryFunctions import ElementaryFunctions as ef
from hotAD.ADfun import *

######## TESTING JACOBIAN

# Input args
def test_J_F_valid_H():
    F = lambda x: [x[0] * 3 + x[1] * x[2] + x[3]*x[3]]
    with pytest.raises(ValueError):
        assert J_F(F, [2,3,4,8], H=3);
        
# Test if length of function is one, i.e. not a vector valued function for Hessian
def test_J_F_len_function_invalid():
    F = lambda x: [x[0] * 3 + x[1] * x[2] + x[3]*x[3], x[0]]
    with pytest.raises(ValueError):
        assert J_F(F, [2,3,4,8], H=True);

# Check that F is a list
def test_J_F_F_list():
    F = lambda x: x[0] * 3 + x[1] * x[2] + x[3]*x[3]
    with pytest.raises(TypeError):
        assert J_F(F, [2,3,4,8]);
        
# Check that x is a list
def test_J_F_F_list():
    F = lambda x: [x[0] * 3 + x[1]]
    with pytest.raises(TypeError):
        assert J_F(F, 1);

# Testing J_F produces the correct values in the function evaluation
def test_J_F_fnval():
	F = lambda x: [x[0] * 3 + x[1] * x[2], x[2] - x[0] * x[1] + x[0]]
	x = [2, 3, 4]
	Jac = J_F(F, x)
	assert np.isclose(Jac[0][0], 18);

# Testing J_F produces the correct values in the Hessian
def test_J_F_jacval():
	F = lambda x: [x[0] * 3 + x[1] * x[2] + x[3]*x[3]]
	x = [2, 3, 4, 8]
	Jac = J_F(F, x, H = True)
	assert np.isclose(Jac[2][3][3], 2.0);


#Test for Newton()
   
#Test input validity
def test_Newton_F_valid():
    with pytest.raises(TypeError):
        assert Newton(3, [0, 1]);
        
def test_Newton_x_valid():
    F = lambda x:[x[0]*x[1], x[0]*x[0]]
    with pytest.raises(TypeError):
        assert Newton(F, 3);
        
def test_Newton_criteria_valid():
    F = lambda x:[x[0]*x[1], x[0]*x[0]]
    with pytest.raises(ValueError):
        assert Newton(F, [2, 3], "a");

#Test output values
def test_Newton_output_x_min():
	F = lambda x:[x[0] * x[0] +4 * x[1], x[1] + x[0]*x[1]]
	assert np.isclose(Newton(F, [3, 2])['x_min: '][0], 0);
    
def test_Newton_output_f_root_value():
	F = lambda x:[x[0] * x[0] +4 * x[1], x[1] + x[0]*x[1]]
	assert np.isclose(Newton(F, [3, 2])['F(x_min): '][0], 0);
    
def test_Newton_output_f_root_value():
	F = lambda x:[x[0] * x[0] +4 * x[1], x[1] + x[0]*x[1]]
	assert np.isclose(Newton(F, [3, 2])['number of iter: '], 541);
    

##### TESTS FOR MINIMIZATION YEAH YEAH
    



	
