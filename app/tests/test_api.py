from app.api_a.module_main import func_main as func_main_a
from app.api_b.module_main import func_main as func_main_b
import pytest


def test_func_main_1():
    seed = 420
    result = func_main_a(seed)
    assert isinstance(result, dict) is True
    assert result.get("seed") == seed


def test_func_main2():
    seed = 500
    result = func_main_b(seed)
    assert isinstance(result, dict) is True
    assert result.get("seed") == seed
