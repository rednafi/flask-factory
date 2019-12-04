from app.api_1.module_main import func_main as func_main_1
from app.api_2.module_main import func_main as func_main_2
import pytest


def test_func_main_1():
    seed = 420
    result = func_main_1(seed)
    assert isinstance(result, dict) is True
    assert result.get("seed") == seed


def test_func_main2():
    seed = 500
    result = func_main_2(seed)
    assert isinstance(result, dict) is True
    assert result.get("seed") == seed
