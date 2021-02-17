"""Test the icon-prometheus-exporter package."""

import requests


def test_get_team_names():
    r = requests.get('http://localhost:6100/metrics')
    assert b"ICON Foundation" in r.content
    assert b"Spartan Node" in r.content
    assert r.status_code == 200


def test_assert_metrcis():
    r = requests.get('http://localhost:6100/metrics')
    assert b"icon_prep_node_block_height" in r.content
    assert b"icon_prep_node_state" in r.content
    assert b"icon_prep_node_version_loopchain_minor" in r.content
    assert b"icon_prep_node_unconfirmed_tx" in r.content
    assert b"icon_prep_node_peer_count" in r.content
    assert b"icon_prep_node_audience_count" in r.content
    assert b"icon_prep_node_rank" in r.content
    assert b"icon_prep_node_block_time" in r.content
    assert b"icon_prep_node_latency" in r.content
    assert b"icon_prep_reference_block_height" in r.content
    assert b"icon_prep_reference_block_time" in r.content
    assert b"icon_total_tx" in r.content
    assert b"icon_blocks_left_in_term" in r.content
    assert b"icon_total_active_main_preps" in r.content
    assert b"icon_total_active_sub_preps" in r.content
    assert b"icon_total_inactive_sub_preps" in r.content
