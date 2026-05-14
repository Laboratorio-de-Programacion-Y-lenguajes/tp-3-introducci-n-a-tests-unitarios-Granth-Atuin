"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


def test_pow_elevado_a_cero():
    assert pow_(5, 0) == 1
    assert pow_(-2, 0) == 1

def test_pow_elevado_a_uno():
    assert pow_(7, 1) == 7

def test_pow_base_negativa_exponente_par():
    assert pow_(-2, 2) == 4
    assert pow_(-3, 4) == 81

def test_pow_exponente_decimal():
    assert pytest.approx(pow_(9, 0.5)) == 3.0
