# test_roots.py
import pytest
import roots

def test_quadroots_result():
    assert roots.quad_roots(1.0, 1.0, -12.0) == ((3+0j), (-4+0j))

def test_quadroots_types():
    with pytest.raises(TypeError):
        roots.quad_roots("", "green", "hi")

def test_quadroots_zerocoeff():
    with pytest.raises(ValueError):
        roots.quad_roots(a=0.0)

def test_linearoots_result():
    assert roots.linear_roots(2.0, -3.0) == 1.5

def test_linearroots_types():
    with pytest.raises(TypeError):
        roots.linear_roots("ocean", 6.0)

def test_linearroots_zerocoeff():
    with pytest.raises(ValueError):
        roots.linear_roots(a=0.0)

test_quadroots_result()
test_quadroots_types()
test_quadroots_zerocoeff()
test_linearoots_result()
test_linearroots_types()
test_linearroots_zerocoeff()