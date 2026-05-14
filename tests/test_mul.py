"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


@pytest.mark.parametrize("a,b,expected", [
    (5, 0, 0),
    (0, 5, 0),
    (-2, -3, 6),
    (2, -3, -6),
    (-4, 5, -20),
    (7, 1, 7),
    (1, -5, -5),
    (1.5, 2.0, 3.0),
])
def test_mul_parametrizado(a, b, expected):
    assert pytest.approx(mul(a, b)) == expected
