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


######## TESTING NEWTON ROOT FINDING METHOD Newton()
   
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
    with pytest.raises(TypeError):
        assert Newton(F, [2, 3], "a");


def test_Newton_check_eq_len_F_x():
    F = lambda x:[x[0]*x[0], x[0]+x[0]]
    with pytest.raises(ValueError):
        assert Newton(F, [2]);
        
#Test output values
def test_Newton_output_x_min():
	F = lambda x:[x[0] * x[0] +4 * x[1], x[1] + x[0]*x[1]]
	assert np.isclose(Newton(F, [3, 2])['x_min: '][0], 0);
    
def test_Newton_output_f_root_value():
	F = lambda x:[x[0] * x[0] +4 * x[1], x[1] + x[0]*x[1]]
	assert np.isclose(Newton(F, [3, 2])['F(x_min): '][0], 0);
    
def test_Newton_output_n_iter():
	F = lambda x:[x[0] * x[0] +4 * x[1], x[1] + x[0]*x[1]]
	assert np.isclose(Newton(F, [3, 2])['number of iter: '], 541);
    

######## TESTING MINIMIZATION METHODS Mini()

#Test optimization input validity
    
def test_Mini_F_valid():
    F = 3
    with pytest.raises(TypeError):
        assert  Mini(F, [1, 0.5]);

def test_Mini_F_length_valid():
    F = lambda x:[x[0], x[1]]
    with pytest.raises(ValueError):
        assert  Mini(F, [1, 0.5]);

def test_Mini_x_valid():
    F = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
    with pytest.raises(TypeError):
        assert  Mini(F, 3);

def test_Mini_method_valid():
    F = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
    with pytest.raises(ValueError):
        assert  Mini(F, [1, 0.5], method = "apple" );
        
def test_Mini_criteria_valid():
    F = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
    with pytest.raises(TypeError):
        assert  Mini(F, [1, 0.5], method = "newton", criteria = "hi");

def test_Mini_rate_valid():
    F = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
    with pytest.raises(TypeError):
        assert  Mini(F, [1, 0.5], method = "newton", rate = "hi");

def test_Mini_x_plot_valid():
    F = lambda x:[x[0]+x[1]+x[2]]
    with pytest.raises(ValueError):
        assert  Mini(F, [1, 0.5, 0], plot = True);

def test_Mini_plot_valid():
    F = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
    with pytest.raises(ValueError):
        assert  Mini(F, [1, 0.5], plot = 99);      
        
#Test optimization output validity

## BFGS Method
    
def test_Mini_BFGS_output_x_min():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.5])['x_min'][0], 1.);

def test_Mini_BFGS_output_f_root_value():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.5])['min F(x)'][0], 0);

def test_Mini_BFGS_output_hessian_approx():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.5])['Hessian approximate'][0][0], 0.49616688);
    
def test_Mini_BFGS_output_n_iter():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.5])['number of iter'], 31);



## Full Newton Method
    
def test_Mini_Newton_output_x_min():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.5], method = "newton")['x_min'][0], 1.);

def test_Mini_Newton_output_f_root_value():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.5], method = "newton")['min F(x)'][0], 0);

def test_Mini_Newton_output_hessian_approx():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.5], method = "newton")['Hessian F(x_min)'][0][0],802);
    
def test_Mini_Newton_output_n_iter():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.5], method = "newton")['number of iter'], 2);
    

## Gradient Descent

def test_Mini_GD_output_x_min():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.9],method = "gradient-descent")['x_min'][0], 0.96727347);

def test_Mini_GD_output_f_root_value():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.9], method = "gradient-descent")['min F(x)'][0], 0.00107281);
    
def test_Mini_GD_output_n_iter():
	F3 = lambda x:[100*(x[1]-x[0]*x[0])*(x[1]-x[0]*x[0]) + (1-x[0])*(1-x[0])]
	assert np.isclose(Mini(F3, [1, 0.9], method = "gradient-descent")['number of iter'], 5000);