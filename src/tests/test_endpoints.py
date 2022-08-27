#!/usr/bin/env python3

"""
Test suitcase for endpoints:
    - /file/<uuid>/stat
    - /file/<uuid>/read
    - /health
Test cases:
    - expected status codes
    - expected keys
    - expected values
    - unexpected values
    - expected content type
    - unexpected content type
    - expected length
    - health endpoint - status + text

"""
import pytest
import requests

from ..file_client.api.flask_config.api_setup import add_resources

# Running function to add api endpoints
add_resources()

HOST = 'http://localhost'
PORT = 5000


# Testing stat and read endpoint - STATUS CODE
@pytest.mark.parametrize('uuid, specify_endpoint, expected_response', [
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'stat', 200),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'read', 200),
    ('041f844f-bce7-4ad7-819e-bb0408f3b8de', 'stat', 404),
    ('041f844f-bce7-4ad7-819e-bb0408f3b8de', 'read', 404),
])
def test_if_endpoints_response_with_expected_status_codes(
        uuid: str,
        specify_endpoint: str,
        expected_response: int
        ):
    response = requests.get(f'{HOST}:{PORT}/file/{uuid}/{specify_endpoint}/')
    assert response.status_code == expected_response


# Testing stat and read endpoint - CONTENT TYPE - VALID/INVALID
@pytest.mark.parametrize('uuid, specify_endpoint, content_type', [
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'stat', 'application/json'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'read', 'application/json'),
])
def test_if_content_type_equals_json(
        uuid: str,
        specify_endpoint: str,
        content_type: str
        ):
    response = requests.get(f'{HOST}:{PORT}/file/{uuid}/{specify_endpoint}/')
    assert response.headers['Content-Type'] == content_type


@pytest.mark.parametrize('uuid, specify_endpoint, content_type', [
    (
        '7f8b6891-defc-475d-9c67-b8eca4cd23b4',
        'stat', 'text/html; charset=UTF-8'
    ),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'read', 'multipart/form-data'),
])
def test_unexpected_content_types(
        uuid: str,
        specify_endpoint: str,
        content_type: str
        ):
    response = requests.get(f'{HOST}:{PORT}/file/{uuid}/{specify_endpoint}/')
    assert response.headers['Content-Type'] != content_type


# Testing read endpoint - VALID KEYS
@pytest.mark.parametrize('uuid, key', [
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'id'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'name'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'age'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'gender'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'income'),
])
def test_if_json_from_response_has_valid_keys_read_endpoint(
        uuid: str,
        key: str
        ):
    response = requests.get(f'{HOST}:{PORT}/file/{uuid}/read/')
    response_body = response.json()
    assert response_body[0][key]


# Testing stat endpoint - VALID KEYS
@pytest.mark.parametrize('uuid, key', [
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'create_datetime'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'size'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'mimetype'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'name'),

])
def test_if_json_from_response_has_valid_keys_stat_endpoint(
        uuid: str,
        key: str
        ):
    response = requests.get(f'{HOST}:{PORT}/file/{uuid}/stat/')
    response_body = response.json()
    assert response_body[key]


# Testing read endpoint - VALID VALUES
@pytest.mark.parametrize('uuid, key, values', [
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'id', 'a2a6d5a2'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'gender', 'f'),
])
def test_if_json_from_response_has_valid_values_read_endpoint(
        uuid: str,
        key: str,
        values: str
        ):
    response = requests.get(f'{HOST}:{PORT}/file/{uuid}/read/')
    response_body = response.json()
    assert response_body[0][key] == values


# Testing read endpoint - INVALID VALUES
@pytest.mark.parametrize('uuid, key, values', [
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'id', 'a3a6d5a2'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'gender', 'm'),
])
def test_if_json_from_response_has_unexpected_values_read_endpoint(
        uuid: str,
        key: str,
        values: str
        ):
    response = requests.get(f'{HOST}:{PORT}/file/{uuid}/read/')
    response_body = response.json()
    assert response_body[0][key] != values


# Testing read endpoint - VALID VALUES
@pytest.mark.parametrize('uuid, key, values', [
    (
        '7f8b6891-defc-475d-9c67-b8eca4cd23b4',
        'create_datetime',
        '2022-08-27T17:13:45.827660'
    ),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'mimetype', 'application/json'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'name', 'stat_people_stats.json'),
])
def test_if_json_from_response_has_valid_values_stat_endpoint(
        uuid: str,
        key: str,
        values: str
        ):
    response = requests.get(f'{HOST}:{PORT}/file/{uuid}/stat/')
    response_body = response.json()
    assert response_body[key] == values


# Testing read endpoint - INVALID VALUES
@pytest.mark.parametrize('uuid, key, values', [
    (
        '7f8b6891-defc-475d-9c67-b8eca4cd23b4',
        'create_datetime',
        '2022-08-27T17:14:45.827660'
    ),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'mimetype', 'multipart/form-data'),
    ('7f8b6891-defc-475d-9c67-b8eca4cd23b4', 'name', 'stat_pet_stats.json'),
])
def test_if_json_from_response_has_unexpected_values_stat_endpoint(
        uuid: str,
        key: str,
        values: str
        ):
    response = requests.get(f'{HOST}:{PORT}/file/{uuid}/stat/')
    response_body = response.json()
    assert response_body[key] != values


# Checking valid len
def test_if_json_from_response_has_valid_length_read_endpoint():
    response = requests.get(
        f'{HOST}:{PORT}/file/7f8b6891-defc-475d-9c67-b8eca4cd23b4/read/'
    )
    response_body = response.json()
    assert len(response_body[0]) == 5


def test_if_json_from_response_has_valid_length_stat_endpoint():
    response = requests.get(
        f'{HOST}:{PORT}/file/7f8b6891-defc-475d-9c67-b8eca4cd23b4/stat/'
    )
    response_body = response.json()
    assert len(response_body) == 4


# Testing health endpoint - STATUS CODE + RESPONSE TEXT
def test_if_health_check_response_with_expected_values():
    response = requests.get(f'{HOST}:{PORT}/health')
    assert response.status_code == 200


def test_if_health_check_response_with_expected_text():
    response = requests.get(f'{HOST}:{PORT}/health')
    assert response.text == 'OK...'


def test_if_health_check_response_with_unexpected_text():
    response = requests.get(f'{HOST}:{PORT}/health')
    assert response.text != 'Not OK...'
