# Tests for ElementaryFunctions.py
import numpy as np
import pytest
from hotAD.AutoDiffObject import AutoDiff
from hotAD.ElementaryFunctions import ElementaryFunctions as ef

# sin
def test_sin_val():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.sin(x*y)
	assert np.isclose(f.val, 0.9129452507276277);

def test_sin_deriv_x():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.sin(x*y)
	assert np.isclose(f.der['x'], 2.0404103090669596);

def test_sin_deriv_y():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.sin(x*y)
	assert np.isclose(f.der['y'], 1.6323282472535678);

def test_sin_deriv2_x():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.sin(x*y)
	assert np.isclose(f.der2['x'], -22.82363126819069);

def test_sin_deriv2_y():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.sin(x*y)
	assert np.isclose(f.der2['y'], -14.607124011642043);

def test_sin_deriv2_xy():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.sin(x*y)
	assert np.isclose(f.der2['xy'], -17.85082295273916);

def test_sin_numeric_input_val():
	assert ef.sin(4) == -0.7568024953079282;

def test_sin_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.sin(4).val;

def test_sin_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.sin(4).der;

def test_sin_illegal_arg():
	with pytest.raises(AttributeError):
		ef.sin("thirty");

# cos
def test_cos_val():
	x = AutoDiff(0.3, "x")
	f = ef.cos(x)
	assert f.val == 0.955336489125606;

def test_cos_deriv():
	x = AutoDiff(0.3, "x")
	f = ef.cos(x)
	assert f.der['x'] == -0.29552020666133955;

def test_cos_numeric_input_val():
	assert ef.cos(0.5) == 0.8775825618903728;

def test_cos_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.cos(0.5).val;

def test_cos_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.sin(0.5).der;

def test_cos_illegal_arg():
	with pytest.raises(AttributeError):
		ef.cos("two");

# tan
def test_tan_val():
	x = AutoDiff(12, "x")
	f = ef.tan(x)
	assert np.isclose(f.val, -0.63585992866158081);

def test_tan_deriv():
	x = AutoDiff(12, "x")
	f = ef.tan(x)
	assert f.der['x'] == 1.4043178488775105;

def test_tan_numeric_input_val():
	assert ef.tan(3) == -0.1425465430742778;

def test_tan_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.tan(3).val;

def test_tan_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.tan(3).der;

def test_tan_illegal_arg():
	with pytest.raises(AttributeError):
		ef.tan("four");

# power
def test_power_val():
	x = AutoDiff(20, "x")
	f = ef.power(x, 3)
	assert f.val == 8000;

def test_power_deriv():
	x = AutoDiff(20, "x")
	f = ef.power(x, 3)
	assert f.der['x'] == 1200;

def test_power_numeric_input_val():
	assert ef.power(2, 3) == 8;

def test_power_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.power(2, 4).val;

def test_power_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.power(20, 1).der;

def test_power_illegal_arg():
	with pytest.raises(AttributeError):
		ef.power("base", "power");


# log

# exp
def test_exp_val():
	x = AutoDiff(5.5, "x")
	f = ef.exp(x)
	assert f.val == 244.69193226422038;

def test_exp_deriv():
	x = AutoDiff(5.5, "x")
	f = ef.exp(x)
	assert f.der['x'] == 244.69193226422038;

def test_exp_numeric_input_val():
	assert ef.exp(3) == 20.085536923187668;

def test_exp_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.exp(3).val;

def test_exp_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.exp(3).der;

def test_exp_illegal_arg():
	with pytest.raises(AttributeError):
		ef.exp("");

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
