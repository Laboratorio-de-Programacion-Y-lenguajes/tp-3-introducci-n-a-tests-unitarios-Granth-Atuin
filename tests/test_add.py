"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


@pytest.mark.parametrize("a,b,expected", [
    (-2, -3, -5),
    (5, -3, 2),
    (-4, 7, 3),
    (0, 5, 5),
    (5, 0, 5),
    (1.5, 2.5, 4.0),
])
def test_add_parametrizado(a, b, expected):
    assert add(a, b) == expected
