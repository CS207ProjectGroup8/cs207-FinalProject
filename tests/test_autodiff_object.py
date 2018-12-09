# Tests for AutoDiffObject.py
import numpy as np
import pytest
from hotAD.AutoDiffObject import AutoDiff
from hotAD.ElementaryFunctions import ElementaryFunctions

def test_autodiff_string_args():
	with pytest.raises(TypeError):
		assert AutoDiff("two", "x");

def test_autodiff_numeric_args():
	with pytest.raises(TypeError):
		assert AutoDiff(5, 3);