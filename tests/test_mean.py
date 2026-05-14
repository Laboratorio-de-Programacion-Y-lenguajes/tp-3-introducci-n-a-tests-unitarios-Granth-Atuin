"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


def test_mean_un_elemento():
    assert mean([5]) == 5.0

def test_mean_negativos():
    assert mean([-2, -4, -6]) == -4.0

def test_mean_decimales():
    assert pytest.approx(mean([1.5, 2.5, 3.5])) == 2.5

def test_mean_lista_vacia():
    with pytest.raises(ValueError):
        mean([])
