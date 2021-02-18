import requests


def test_get_preps():
    payload = {
            "jsonrpc": "2.0",
        "id": 1234,
        "method": "icx_call",
        "params": {
            "to": "cx0000000000000000000000000000000000000000",
            "dataType": "call",
            "data": {
                "method": "getPReps",
                "params": {
                    "startRanking": "0x1",
                    "endRanking": "0x64"
                }
            }
        }
    }

    # url = "https://zicon.net.solidwallet.io"
    url = "https://ctz.solidwallet.io"
    url = '/'.join([url, "api/v3"])

    response = requests.post(url, json=payload).json()

    assert len(response['result']['preps']) > 50
