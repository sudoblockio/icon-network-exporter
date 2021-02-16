"""Test the icon-prometheus-exporter package."""

import requests
import pytest


@pytest.fixture()
def setup():
    # Run the app
    yield


def test_get_team_names():
    r = requests.get('http://localhost:6100/metrics')
    assert b"ICON Foundation" in r.content
    assert b"Spartan Node" in r.content
    assert r.status_code == 200
