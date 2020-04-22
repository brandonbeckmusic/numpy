"""
Tests related to the ``symbol`` attribute of the ABCPolyBase class.
"""

import pytest
import numpy.polynomial as poly
from numpy.polynomial._polybase import ABCPolyBase
from numpy.testing import assert_equal, assert_raises

class TestInit:
    """
    Test polynomial creation with symbol kwarg.
    """
    c = [1, 2, 3]
    def test_default_symbol(self):
        p = poly.Polynomial(self.c)
        assert_equal(p.symbol, 'x')

    @pytest.mark.parametrize(('bad_input', 'exception'), (
        ('', ValueError),
        ('3', ValueError),
        (None, TypeError),
        (1, TypeError),
    ))
    def test_symbol_bad_input(self, bad_input, exception):
        with pytest.raises(exception):
            p = poly.Polynomial(self.c, symbol=bad_input)

    # TODO: Add support for latex symbols, e.g. symbol='\\beta'
    @pytest.mark.parametrize('symbol', (
        'x',
        'x_1',
        'A',
        'xyz',
    ))
    def test_valid_symbols(self, symbol):
        """
        Values for symbol that should pass input validation.
        """
        p = poly.Polynomial(self.c, symbol=symbol)
        assert_equal(p.symbol, symbol)
