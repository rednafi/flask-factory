import httpx
import pytest

from app.api_a.main import func_main as func_main_a
from app.api_b.main import func_main as func_main_b


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


def check_if_server_is_running():
    try:
        _ = httpx.get("http://localhost:4000/")
        return False
    except httpx.ConnectError:
        return True


@pytest.mark.skipif(check_if_server_is_running(), reason="Server isn't running")
def test_api_a_status_code_unauth():
    response = httpx.get("http://localhost:4000/api-a/100")
    assert response.status_code == 401


@pytest.mark.skipif(check_if_server_is_running(), reason="Server isn't running")
def test_api_a_status_code_ok():
    response = httpx.get(
        "http://localhost:4000/api-a/100", headers={"X-Api-Key": "1234ABCD"}
    )
    assert response.status_code == 200


@pytest.mark.skipif(check_if_server_is_running(), reason="Server isn't running")
def test_api_b_status_code_unauth():
    response = httpx.get("http://localhost:4000/api-b/100")
    assert response.status_code == 401


@pytest.mark.skipif(check_if_server_is_running(), reason="Server isn't running")
def test_api_b_status_code_ok():
    response = httpx.get(
        "http://localhost:4000/api-b/100", headers={"X-Api-Key": "1234ABCD"}
    )
    assert response.status_code == 200
