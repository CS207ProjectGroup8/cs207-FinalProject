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
	with pytest.raises(AttributeError):
		assert AutoDiff(6, 'xy', H=True)

def test_autodiff_variable_name_args_notAlpha_space():
	with pytest.raises(AttributeError):
		assert AutoDiff(6, ' ')	

def test_autodiff_variable_name_args_notAlpha_symbol():
	with pytest.raises(AttributeError):
		assert AutoDiff(6, '&')

# Equality
def test_autodiff_eq():
	a = AutoDiff(2, "a")
	b = AutoDiff(4, "b")
	assert ef.power(a, 2).val == b.val

def test_autodiff_neq_ad_and_num():
	a = AutoDiff(4, "a")
	b = 4
	assert a != b

def test_autodiff_neq_ad_and_num2():
	a = AutoDiff(4, "a")
	b = "four"
	assert a != b

def test_autodiff_neq():
	a = AutoDiff(2, "a")
	b = AutoDiff(4, "b")
	assert a.val != b.val

# Negation
def test_autodiff_negation_val():
	a = AutoDiff(3, "a")
	b = AutoDiff(1.5, "b")
	f = a*b
	assert -1*f.val == -4.5

def test_autodiff_negation_firstDer():
	a = AutoDiff(3, "a")
	b = AutoDiff(1.5, "b")
	f = a*b
	assert -1*f.der['a'] == -b.val

def test_autodiff_negation_secondDer():
	a = AutoDiff(3, "a", H=True)
	b = AutoDiff(1.5, "b", H=True)
	f = a*a*b
	assert -1*f.der2['a'] == -3.0

# Multiplication
def test_autodiff_mul_val():
	a = AutoDiff(3, "a")
	b = AutoDiff(2, "b")
	f = (a*a)*(b*b)
	assert f.val == 36

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
	assert f.der['a'] == 1/b.val

def test_autodiff_div_zerodiv():
	a = AutoDiff(3, "a")
	b = AutoDiff(0, "b")
	with pytest.raises(ZeroDivisionError):
		assert a/b

def test_autodiff_div_illegal_args():
	a = AutoDiff(2, "a")
	with pytest.raises(AttributeError):
		assert a/"AutoDiff(2, 'b')"	

# Addition
def test_autodiff_add():
	a = AutoDiff(13, "a")
	b = AutoDiff(22, "b")
	f = a + b
	assert f.der['b'] == 0

def test_autodiff_add_illegal_args():
	a = AutoDiff(9, "a")
	with pytest.raises(AttributeError):
		assert a + "AutoDiff(5, 'b')"

# Subtraction
def test_autodiff_add():
	a = AutoDiff(10, "a")
	b = AutoDiff(22, "b")
	f = a - b
	assert f.val == -12

def test_autodiff_sub_illegal_args():
	a = AutoDiff(9, "a")
	with pytest.raises(AttributeError):
		assert "AutoDiff(11, 'b')" - a



