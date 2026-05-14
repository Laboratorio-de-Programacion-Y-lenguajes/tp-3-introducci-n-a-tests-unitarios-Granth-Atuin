"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


def test_div_decimal():
    assert pytest.approx(div(5, 2)) == 2.5

def test_div_negativos():
    assert div(-6, 2) == -3.0
    assert div(-6, -3) == 2.0

def test_div_por_cero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
