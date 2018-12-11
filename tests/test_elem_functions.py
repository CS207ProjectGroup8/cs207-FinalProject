# Tests for ElementaryFunctions.py
import numpy as np
import warnings
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
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.sin(x*y)
	assert np.isclose(f.der2['x'], -22.82363126819069);

def test_sin_deriv2_y():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.sin(x*y)
	assert np.isclose(f.der2['y'], -14.607124011642043);

def test_sin_deriv2_xy():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.sin(x*y)
	assert np.isclose(f.der2['xy'], -17.85082295273916);

def test_sin_no_sec_derivative_():
	x = AutoDiff(4, "x")
	with pytest.raises(AttributeError):
		assert ef.sin(x).der2['x'];

def test_sin_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.sin(4).val;

def test_sin_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.sin(4).der;

def test_sin_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.sin("thirty");

def test_illegal_len_varname():
	with pytest.raises(AttributeError):
		assert AutoDiff(4, "variable1")

def test_numeric_value():
	assert np.isclose(ef.sin(4), np.sin(4))

# cos
def test_cos_val():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.cos(x*y)
	assert np.isclose(f.val, 0.40808206181339196);

def test_cos_deriv_x():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.cos(x*y)
	assert np.isclose(f.der['x'], -4.564726253638138);

def test_cos_deriv_y():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.cos(x*y)
	assert np.isclose(f.der['y'], -3.6517810029105107);

def test_cos_deriv2_x():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.cos(x*y)
	assert np.isclose(f.der2['x'], -10.202051545334799);

def test_cos_deriv2_y():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.cos(x*y)
	assert np.isclose(f.der2['y'], -6.529312989014271);

def test_cos_deriv2_xy():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.cos(x*y)
	assert np.isclose(f.der2['xy'], -9.074586486995466);

def test_cos_no_sec_derivative_():
	x = AutoDiff(4, "x")
	with pytest.raises(AttributeError):
		assert ef.cos(x).der2['x'];

def test_cos_no_sec_derivative_xy():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	with pytest.raises(AttributeError):
		assert ef.cos(x).der2['x'];

def test_cos_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.cos(4).val;

def test_cos_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.cos(4).der;

def test_cos_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.cos("thirty");

def test_cos_numeric_value():
	assert np.isclose(ef.cos(4), np.cos(4))

# tan
def test_tan_val():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.tan(x*x*y*y)
	assert np.isclose(f.val, 1.619884429116927);

def test_tan_deriv_x():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.tan(x*x*y*y)
	assert np.isclose(f.der['x'], 724.8051127390946);

def test_tan_deriv_y():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.tan(x*x*y*y)
	assert np.isclose(f.der['y'], 579.8440901912758);

def test_tan_deriv2_x():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.tan(x*x*y*y)
	assert np.isclose(f.der2['x'], 469821.40778634406);

def test_tan_deriv2_y():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.tan(x*x*y*y)
	assert np.isclose(f.der2['y'], 300685.7009832602);

def test_tan_deriv2_xy():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.tan(x*x*y*y)
	assert np.isclose(f.der2['xy'], 376002.08725162304);

def test_tan_no_sec_derivative():
	x = AutoDiff(4, "x")
	with pytest.raises(AttributeError):
		assert ef.tan(x).der2['x'];

def test_tan_no_sec_derivative_xy():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	with pytest.raises(AttributeError):
		assert ef.tan(x*y).der2['xy'];

def test_tan_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.tan(4).val;

def test_tan_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.tan(4).der;

def test_tan_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.tan("thirty");

def test_tan_numeric_value():
	assert np.isclose(ef.tan(4), np.tan(4))

# power
def test_power_val():
	x = AutoDiff(1, "x")
	y = AutoDiff(2, "y")
	f = ef.power(x*y, x*y)
	assert np.isclose(f.val, 4);

def test_power_deriv_x():
	x = AutoDiff(1, "x")
	y = AutoDiff(2, "y")
	f = ef.power(x*y, x*y)
	assert np.isclose(f.der['x'], 13.545177444479563);

def test_power_deriv_y():
	x = AutoDiff(1, "x")
	y = AutoDiff(2, "y")
	f = ef.power(x*y, x*y)
	assert np.isclose(f.der['y'], 6.772588722239782);

def test_power_deriv2_x():
	x = AutoDiff(1, "x", H=True)
	y = AutoDiff(2, "y", H=True)
	f = ef.power(x*y, x*y)
	assert np.isclose(f.der2['x'], 53.86795800060948);

def test_power_deriv2_y():
	x = AutoDiff(1, "x", H=True)
	y = AutoDiff(2, "y", H=True)
	f = ef.power(x*y, x*y)
	assert np.isclose(f.der2['y'], 13.46698950015237);

def test_power_deriv2_xy():
	x = AutoDiff(1, "x", H=True)
	y = AutoDiff(2, "y", H=True)
	f = ef.power(x*y, x*y)
	assert np.isclose(f.der2['xy'], 33.70656772254452);

def test_power_val2():
	x = AutoDiff(1, "x")
	y = AutoDiff(2, "y")
	f = ef.power(x*y, 3)
	assert np.isclose(f.val, 8);

def test_power_deriv_x2():
	x = AutoDiff(1, "x")
	y = AutoDiff(2, "y")
	f = ef.power(x*y, 3)
	assert np.isclose(f.der['x'], 24);

def test_power_deriv_y2():
	x = AutoDiff(1, "x")
	y = AutoDiff(2, "y")
	f = ef.power(x*y, 3)
	assert np.isclose(f.der['y'], 12);

def test_power_deriv2_x2():
	x = AutoDiff(1, "x", H=True)
	y = AutoDiff(2, "y", H=True)
	f = ef.power(x*y, 3)
	assert np.isclose(f.der2['x'], 48);

def test_power_deriv2_y2():
	x = AutoDiff(1, "x", H=True)
	y = AutoDiff(2, "y", H=True)
	f = ef.power(x*y, 3)
	assert np.isclose(f.der2['y'], 12);

def test_power_deriv2_xy2():
	x = AutoDiff(1, "x", H=True)
	y = AutoDiff(2, "y", H=True)
	f = ef.power(x*y, 3)
	assert np.isclose(f.der2['xy'], 36);

def test_power_val3():
	x = AutoDiff(1, "x")
	y = AutoDiff(2, "y")
	f = ef.power(3, x*y)
	assert np.isclose(f.val, 9);

def test_power_deriv_x3():
	x = AutoDiff(1, "x")
	y = AutoDiff(2, "y")
	f = ef.power(3, x*y)
	assert np.isclose(f.der['x'], 19.775021196025975);

def test_power_deriv_y3():
	x = AutoDiff(1, "x")
	y = AutoDiff(2, "y")
	f = ef.power(3, x*y)
	assert np.isclose(f.der['y'], 9.887510598012987);

def test_power_deriv2_x3():
	x = AutoDiff(1, "x", H=True)
	y = AutoDiff(2, "y", H=True)
	f = ef.power(3, x*y)
	assert np.isclose(f.der2['x'], 43.450162589252955);

def test_power_deriv2_y3():
	x = AutoDiff(1, "x", H=True)
	y = AutoDiff(2, "y", H=True)
	f = ef.power(3, x*y)
	assert np.isclose(f.der2['y'], 10.862540647313239);

def test_power_deriv2_xy3():
	x = AutoDiff(1, "x", H=True)
	y = AutoDiff(2, "y", H=True)
	f = ef.power(3, x*y)
	assert np.isclose(f.der2['xy'], 31.612591892639465);

def test_power_no_sec_derivative():
	x = AutoDiff(4, "x")
	y = AutoDiff(3, "y")
	with pytest.raises(AttributeError):
		assert ef.power(x,y).der2['x'];

def test_power_no_sec_derivative_xy():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	with pytest.raises(AttributeError):
		assert ef.power(x*y,x*y).der2['xy'];

def test_power_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.power(4,5).val;

def test_power_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.power(4,5).der;

def test_power_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.pwer("thirty",2);

def test_power_illegal_arg2():
	with pytest.raises(AttributeError):
		assert ef.pwer(2,"thirty");

def test_power_illegal_arg2():
	x = AutoDiff(2,"x")
	with pytest.raises(AttributeError):
		assert ef.pwer(x,"thirty");

def test_power_illegal_arg2():
	x = AutoDiff(2,"x")
	with pytest.raises(AttributeError):
		assert ef.pwer("thirty",x);

def test_power_numeric_value():
	assert np.isclose(ef.power(4,3), np.power(4,3))

def test_power_illegal_arg3():
	x = AutoDiff(-1,"x")
	with pytest.raises(AttributeError):
		assert ef.pwer(x,2);


# log
def test_log_val():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.log(x*x*y*y)
	assert np.isclose(f.val, 5.991464547107982);

def test_log_deriv_x():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.log(x*x*y*y)
	assert np.isclose(f.der['x'], 0.5);

def test_log_deriv_y():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	f = ef.log(x*x*y*y)
	assert np.isclose(f.der['y'], 0.4);

def test_log_deriv2_x():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.log(x*x*y*y)
	assert np.isclose(f.der2['x'], -0.125);

def test_log_deriv2_y():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.log(x*x*y*y)
	assert np.isclose(f.der2['y'], -0.08);

def test_log_deriv2_xy():
	x = AutoDiff(4, "x", H=True)
	y = AutoDiff(5, "y", H=True)
	f = ef.log(x*x*y*y)
	assert np.isclose(f.der2['xy'], 0);

def test_log_no_sec_derivative_():
	x = AutoDiff(4, "x")
	with pytest.raises(AttributeError):
		assert ef.log(x).der2['x'];

def test_log_no_sec_derivative_xy():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	with pytest.raises(AttributeError):
		assert ef.log(x*x*y*y).der2['x'];

def test_log_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.log(30).val;

def test_log_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.log(30).der;

def test_log_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.log("thirty");

def test_log_numeric_value():
	assert np.isclose(ef.log(4), np.log(4))

# exp
def test_exp_val():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(1.1, "y")
	f = ef.exp(x*x*y*y)
	assert np.isclose(f.val, 1.3532376764211722);

def test_exp_deriv_x():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(1.1, "y")
	f = ef.exp(x*x*y*y)
	assert np.isclose(f.der['x'], 1.6374175884696187);

def test_exp_deriv_y():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(1.1, "y")
	f = ef.exp(x*x*y*y)
	assert np.isclose(f.der['y'], 0.7442807220316447);

def test_exp_deriv2_x():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(1.1, "y", H=True)
	f = ef.exp(x*x*y*y)
	assert np.isclose(f.der2['x'], 5.256110458987476);

def test_exp_deriv2_y():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(1.1, "y", H=True)
	f = ef.exp(x*x*y*y)
	assert np.isclose(f.der2['y'], 1.0859732353279907);

def test_exp_deriv2_xy():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(1.1, "y", H=True)
	f = ef.exp(x*x*y*y)
	assert np.isclose(f.der2['xy'], 3.877702561784869);

def test_exp_no_sec_derivative_():
	x = AutoDiff(4, "x")
	with pytest.raises(AttributeError):
		assert ef.exp(x).der2['x'];

def test_exp_no_sec_derivative_xy():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	with pytest.raises(AttributeError):
		assert ef.exp(x*x*y*y).der2['x'];

def test_exp_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.exp(30).val;

def test_log_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.exp(30).der;

def test_exp_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.exp("thirty");

def test_exp_illegal_arg2():
	with pytest.raises(AttributeError):
		assert ef.exp(" ");

def test_exp_numeric_value():
	assert np.isclose(ef.exp(4), np.exp(4))


# sqrt
def test_sqrt_val():
	x = AutoDiff(1.5, "x")
	y = AutoDiff(2.5, "y")
	f = ef.sqrt(x*x*y*y)
	assert np.isclose(f.val, 3.75);

def test_sqrt_deriv_x():
	x = AutoDiff(1.5, "x")
	y = AutoDiff(2.5, "y")
	f = ef.sqrt(x*x*y*y)
	assert np.isclose(f.der['x'], 2.5);

def test_sqrt_deriv_y():
	x = AutoDiff(1.5, "x")
	y = AutoDiff(2.5, "y")
	f = ef.sqrt(x*x*y*y)
	assert np.isclose(f.der['y'], 1.5);

def test_sqrt_deriv2_x():
	x = AutoDiff(1.5, "x", H=True)
	y = AutoDiff(2.5, "y", H=True)
	f = ef.sqrt(x*x*y*y)
	assert np.isclose(f.der2['x'], 0);

def test_sqrt_deriv2_y():
	x = AutoDiff(1.5, "x", H=True)
	y = AutoDiff(2.5, "y", H=True)
	f = ef.sqrt(x*x*y*y)
	assert np.isclose(f.der2['y'], 0);

def test_sqrt_deriv2_xy():
	x = AutoDiff(1.5, "x", H=True)
	y = AutoDiff(2.5, "y", H=True)
	f = ef.sqrt(x*x*y*y)
	assert np.isclose(f.der2['xy'], 1.0);

def test_sqrt_no_sec_derivative():
	x = AutoDiff(4, "x")
	with pytest.raises(AttributeError):
		assert ef.sqrt(x).der2['x'];

def test_sqrt_no_sec_derivative_xy():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	with pytest.raises(AttributeError):
		assert ef.sqrt(x*x*y*y).der2['x'];

def test_sqrt_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.sqrt(30).val;

def test_sqrt_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.sqrt(30).der;

def test_sqrt_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.sqrt("thirty");

def test_sqrt_illegal_arg2():
	with pytest.raises(AttributeError):
		assert ef.sqrt(" ");

def test_sqrt_numeric_value():
	assert np.isclose(ef.sqrt(4), np.sqrt(4))

# logit
def test_logit_val():
	x = AutoDiff(1.1, "x")
	y = AutoDiff(2.2, "y")
	f = ef.logit(x*x*y*y)
	assert np.isclose(f.val, 0.9971466383123472);

def test_logit_deriv_x():
	x = AutoDiff(1.1, "x")
	y = AutoDiff(2.2, "y")
	f = ef.logit(x*x*y*y)
	assert np.isclose(f.der['x'], 0.03029590271687);

def test_logit_deriv_y():
	x = AutoDiff(1.1, "x")
	y = AutoDiff(2.2, "y")
	f = ef.logit(x*x*y*y)
	assert np.isclose(f.der['y'], 0.015147951358435);

def test_logit_deriv2_x():
	x = AutoDiff(1.1, "x", H=True)
	y = AutoDiff(2.2, "y", H=True)
	f = ef.logit(x*x*y*y)
	assert np.isclose(f.der2['x'], -0.2932081060866549);

def test_logit_deriv2_y():
	x = AutoDiff(1.1, "x", H=True)
	y = AutoDiff(2.2, "y", H=True)
	f = ef.logit(x*x*y*y)
	assert np.isclose(f.der2['y'], -0.07330202652166372);

def test_logit_deriv2_xy():
	x = AutoDiff(1.1, "x", H=True)
	y = AutoDiff(2.2, "y", H=True)
	f = ef.logit(x*x*y*y)
	assert np.isclose(f.der2['xy'], -0.1328331881720229);

def test_logit_no_sec_derivative_():
	x = AutoDiff(4, "x")
	with pytest.raises(AttributeError):
		assert ef.logit(x).der2['x'];

def test_logit_no_sec_derivative_xy():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	with pytest.raises(AttributeError):
		assert ef.logit(x*x*y*y).der2['x'];

def test_logit_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.logit(30).val;

def test_logit_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.logit(30).der;

def test_logit_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.logit("thirty");

def test_logit_numeric_value():
	assert np.isclose(ef.logit(4), 1/(1+np.exp(-4)))


# arcsin
def test_arcsin_val_error():
	x = AutoDiff(1.1, "x")
	y = AutoDiff(2.2, "y")
	with pytest.warns(RuntimeWarning):
		assert ef.arcsin(x*x*y*y);

def test_arcsin_val():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.6, "y")
	f = ef.arcsin(x*x*y*y)
	assert np.isclose(f.val, 0.09012194501459525);

def test_arcsin_deriv_x():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.6, "y")
	f = ef.arcsin(x*x*y*y)
	assert np.isclose(f.der['x'], 0.3614669175639658);

def test_arcsin_deriv_y():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.6, "y")
	f = ef.arcsin(x*x*y*y)
	assert np.isclose(f.der['y'], 0.30122243130330484);

def test_arcsin_deriv2_x():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(0.6, "y", H=True)
	f = ef.arcsin(x*x*y*y)
	assert np.isclose(f.der2['x'], 0.7347410013030223);

def test_arcsin_deriv2_y():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(0.6, "y", H=True)
	f = ef.arcsin(x*x*y*y)
	assert np.isclose(f.der2['y'], 0.5102368064604322);

def test_logit_deriv2_xy():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(0.6, "y", H=True)
	f = ef.arcsin(x*x*y*y)
	assert np.isclose(f.der2['xy'], 1.2147290303591283);

def test_arcsin_no_sec_derivative_():
	x = AutoDiff(0.5, "x")
	with pytest.raises(AttributeError):
		assert ef.arcsin(x).der2['x'];

def test_arcsin_no_sec_derivative_xy():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.4, "y")
	with pytest.raises(AttributeError):
		assert ef.arcsin(x*x*y*y).der2['x'];

def test_arcsin_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.arcsin(0.2).val;

def test_arcsin_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.arcsin(-0.2).der;

def test_arcsin_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.arcsin("thirty");

def test_arcsin_numeric_value():
	assert np.isclose(ef.arcsin(0.2), np.arcsin(0.2));

def test_arcsin_illegal_arg2():
	with pytest.warns(RuntimeWarning):
		assert np.arcsin(2);


# arccos
def test_arccos_val_error():
	x = AutoDiff(1.1, "x")
	y = AutoDiff(2.2, "y")
	with pytest.warns(RuntimeWarning):
		assert ef.arccos(x*x*y*y);

def test_arccos_val():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.6, "y")
	f = ef.arccos(x*x*y*y)
	assert np.isclose(f.val, 1.4806743817803012);

def test_arccos_deriv_x():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.6, "y")
	f = ef.arccos(x*x*y*y)
	assert np.isclose(f.der['x'], -0.3614669175639658);

def test_arccos_deriv_y():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.6, "y")
	f = ef.arccos(x*x*y*y)
	assert np.isclose(f.der['y'], -0.30122243130330484);

def test_arccos_deriv2_x():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(0.6, "y", H=True)
	f = ef.arccos(x*x*y*y)
	assert np.isclose(f.der2['x'], -0.7347410013030223);

def test_arccos_deriv2_y():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(0.6, "y", H=True)
	f = ef.arccos(x*x*y*y)
	assert np.isclose(f.der2['y'], -0.5102368064604322);

def test_arccos_deriv2_xy():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(0.6, "y", H=True)
	f = ef.arccos(x*x*y*y)
	assert np.isclose(f.der2['xy'], -1.2147290303591283);

def test_arccos_no_sec_derivative_():
	x = AutoDiff(0.2, "x")
	with pytest.raises(AttributeError):
		assert ef.arccos(x).der2['x'];

def test_arccos_no_sec_derivative_xy():
	x = AutoDiff(0.1, "x")
	y = AutoDiff(0.3, "y")
	with pytest.raises(AttributeError):
		assert ef.arccos(x*x*y*y).der2['x'];

def test_arccos_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.arccos(0).val;

def test_arccos_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.arccos(-0.9).der;

def test_arccos_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.arccos("thirty");

def test_arccos_numeric_value():
	assert np.isclose(ef.arccos(0.4), np.arccos(0.4))

def test_arccos_illegal_arg2():
	with pytest.warns(RuntimeWarning):
		assert np.arccos(2);

# arctan
def test_arctan_val():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.6, "y")
	f = ef.arctan(x*x*y*y)
	assert np.isclose(f.val, 0.08975817418995052);

def test_arctan_deriv_x():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.6, "y")
	f = ef.arctan(x*x*y*y)
	assert np.isclose(f.der['x'], 0.3571074298184704);

def test_arctan_deriv_y():
	x = AutoDiff(0.5, "x")
	y = AutoDiff(0.6, "y")
	f = ef.arctan(x*x*y*y)
	assert np.isclose(f.der['y'], 0.2975895248487253);

def test_arctan_deriv2_x():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(0.6, "y", H=True)
	f = ef.arctan(x*x*y*y)
	assert np.isclose(f.der2['x'], 0.6912602306792611);

def test_arctan_deriv2_y():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(0.6, "y", H=True)
	f = ef.arctan(x*x*y*y)
	assert np.isclose(f.der2['y'], 0.480041826860598);

def test_arctan_deriv2_xy():
	x = AutoDiff(0.5, "x", H=True)
	y = AutoDiff(0.6, "y", H=True)
	f = ef.arctan(x*x*y*y)
	assert np.isclose(f.der2['xy'], 1.1712292419301682);

def test_arctan_no_sec_derivative_():
	x = AutoDiff(4, "x")
	with pytest.raises(AttributeError):
		assert ef.arctan(x).der2['x'];

def test_arctan_no_sec_derivative_xy():
	x = AutoDiff(4, "x")
	y = AutoDiff(5, "y")
	with pytest.raises(AttributeError):
		assert ef.arctan(x*x*y*y).der2['x'];

def test_arctan_numeric_input_no_val():
	with pytest.raises(AttributeError):
		assert ef.arctan(30).val;

def test_arctan_numeric_input_no_deriv():
	with pytest.raises(AttributeError):
		assert ef.arctan(30).der;

def test_arctan_illegal_arg():
	with pytest.raises(AttributeError):
		assert ef.arctan("thirty");

def test_arctan_numeric_value():
	assert np.isclose(ef.arctan(4), np.arctan(4))

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
