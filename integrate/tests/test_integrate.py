"""
Unit and regression test for the integrate package.
"""

# Import package, test suite, and other packages as needed
import integrate
import pytest
import sys

def test_integrate_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "integrate" in sys.modules
