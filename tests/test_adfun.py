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
