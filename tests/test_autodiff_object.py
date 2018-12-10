# Tests for AutoDiffObject.py
import numpy as np
import pytest
from hotAD.AutoDiffObject import AutoDiff
from hotAD.ElementaryFunctions import ElementaryFunctions as ef

# Input args
def test_autodiff_string_args():
	with pytest.raises(TypeError):
		assert AutoDiff("two", "x");

def test_autodiff_numeric_args():
	with pytest.raises(TypeError):
		assert AutoDiff(5, 3);

def test_autodiff_hessian_args():
	with pytest.raises(TypeError):
		assert AutoDiff(5, 'x', H=3)

def test_autodiff_variable_name_args():
	with pytest.raises(TypeError):
		assert AutoDiff(6, 'xy', H=T)

# Equality
def test_autodiff_eq():
	a = AutoDiff(2, "a")
	b = AutoDiff(4, "b")
	assert ef.power(a, 2) == b.val

def test_autodiff_neq():
	a = AutoDiff(2, "a")
	b = AutoDiff(4, "b")
	assert a.val == b.val

# Negation
def test_autodiff_negation():
	a = AutoDiff(3, "a")
	b = AutoDiff(1.5, "b")
	f = a*b
	assert f.der['a'] == -b.val

# Multiplication
def test_autodiff_mul_der1():
	a = AutoDiff(3, "a")
	b = AutoDiff(1.5, "b")
	f = (a*a)*(b*b)
	assert f.der['a'] == (2*a.val*b.val**2)

def test_autodiff_mul_der2():
	a = AutoDiff(3, "a", H=True)
	b = AutoDiff(1.5, "b", H=True)
	f = (a*a)*(b*b)
	assert f.der2['a'] == (2*b.val*b.val)

def test_autodiff_mul_illegal_arg():
	a = AutoDiff(3, "a")
	with pytest.raises(AttributeError):
		assert "AutoDiff(4, 'b')"*a

# Division
def test_autodiff_div():
	a = AutoDiff(2, "a")
	b = AutoDiff(5, "b")
	f = a/b
	assert f.der['a'] == 2


