"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


@pytest.mark.parametrize("a,b,expected", [
    (2, 5, -3),
    (5, 0, 5),
    (0, 5, -5),
    (-3, -2, -1),
    (-2, -5, 3),
    (5.5, 2.2, 3.3),
])
def test_sub_parametrizado(a, b, expected):
    assert pytest.approx(sub(a, b)) == expected
