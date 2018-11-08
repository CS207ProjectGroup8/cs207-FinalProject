# Tests for AutoDiffObject.py
import numpy as np
import pytest
from src.source_code.AutoDiffObject import AutoDiff
from src.source_code.ElementaryFunctions import ElementaryFunctions as ef

def test_autodiff_string_args():
	with pytest.raises(TypeError):
		assert AutoDiff("two", "x");

def test_autodiff_numeric_args():
	with pytest.raises(TypeError):
		assert AutoDiff(5, 3);