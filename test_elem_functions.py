# Tests for Elementary_Functions.py
from ElementaryFunctions import ElementaryFunctions
import AutoDiffObject as autodiff
import math
import pytest

ef = ElementaryFunctions()

# sin
def test_sin_val():
	x = autodiff.AutoDiff(2, "x")
	f = ef.sin(x)
	assert f.val == math.sin(2);

def test_sin_deriv():
	x = autodiff.AutoDiff(2, "x")
	f = ef.sin(x)
	assert f.der['x'] == math.cos(2);

# cos
def test_cos_val():
	x = autodiff.AutoDiff(0.3, "x")
	f = ef.cos(x)
	assert f.val == math.cos(0.3);

def test_cos_deriv():
	x = autodiff.AutoDiff(0.3, "x")
	f = ef.cos(x)
	assert f.der['x'] == -math.sin(0.3);

# tan
def test_tan_val():
	x = autodiff.AutoDiff(12, "x")
	f = ef.tan(x)
	assert f.val == math.tan(12);

def test_tan_deriv():
	x = autodiff.AutoDiff(12, "x")
	f = ef.tan(x)
	assert f.der['x'] == 1/(math.cos(12)**2);

# for general tests
# passing illegal objects
# passing null objects
# passing no element
# passing 1 element
# passing matrix

# for root finding
# check Jacobian size 

# from Timothy
# 3-4 tests for every elem function
# 70-80% coverage
# need doctests and docstrings
# for regular ad objects: multiple examples and edge cases

