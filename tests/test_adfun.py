# Tests for ADfun.py
import numpy as np
import pytest
from hotAD.AutoDiffObject import AutoDiff
from hotAD.ElementaryFunctions import ElementaryFunctions as ef
from hotAD.ADfun import *


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

#        >>> F2 = lambda x: [x[0] * 3 + x[1] * x[2] + x[3]*x[3]]
#        >>> print(J_F(F2, [2, 3, 4, 8], H = True)[2][0])
#        [0. 0. 0. 0.]
#        >>> print(J_F(F2, [2, 3, 4, 8], H = True)[2][1])
#        [0. 0. 1. 0.]
#        >>> print(J_F(F2, [2, 3, 4, 8], H = True)[2][2])
#        [0. 1. 0. 0.]
#        >>> print(J_F(F2, [2, 3, 4, 8], H = True)[2][3])
#        [0. 0. 0. 2.]
#
#
#        F = lambda x: [x[0] * 3 + x[1] * x[2], x[2] - x[0] * x[1] + x[0]]
#        print(J_F(F, [2, 3, 4])[0])
#        [18.  0.]
#        >>> print(J_F(F, [2, 3, 4])[1][0])
#        [3. 4. 3.]
#        >>> print(J_F(F, [2, 3, 4])[1][1])
#        [-2. -2.  1.]