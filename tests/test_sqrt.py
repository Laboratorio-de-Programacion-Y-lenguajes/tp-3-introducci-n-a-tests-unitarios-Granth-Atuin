"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


def test_sqrt_cero():
    assert sqrt(0) == 0.0

def test_sqrt_decimal():
    assert pytest.approx(sqrt(2)) == 1.4142135623730951

def test_sqrt_negativo():
    with pytest.raises(ValueError):
        sqrt(-4)
