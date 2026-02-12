from wenex.common.core.utils.httpx import base64_url_encode, get_params


def test_base64_url_encode():
    url_encode = base64_url_encode(str("Wenex Platform").encode())
    assert url_encode == "V2VuZXggUGxhdGZvcm0"


def test_get_params():
    params = get_params()
    assert params == {}

    params = get_params({"brotli": 0})
    assert params == {"q": "iwCAe30D"}

    params = get_params({"brotli": True})
    assert params == {"q": "iwCAe30D"}

    params = get_params({"brotli": False})
    assert params == {}

    params = get_params({"brotli": {}})
    assert params == {"q": "iwCAe30D"}

    params = get_params({"brotli": {"quality": 8}})
    assert params == {"q": "iwCAe30D"}
