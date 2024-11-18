# For the code to work, create a settings.ini file in the root of the repository using the template:
# [DISK]
# DISK_TOKEN=<your ya.disk token without quotes>


import requests
import configparser
import pytest


config = configparser.ConfigParser()
config.read('settings.ini')

disk_token = config["DISK"]["DISK_TOKEN"]
base_url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': f'OAuth {disk_token}'}

def mkdir_on_disk(dir_name):
    response = requests.put(base_url, params={'path': dir_name}, headers=headers)
    return response.status_code

def check_dir(dir_name):
    response = requests.get(
        f"{base_url}",
        params={'path': f'/{dir_name}'},
        headers=headers
    )
    return 'error' not in response.json()


@pytest.mark.parametrize(
    'dir_name,expected',
    (
        ('d1', 201),
        ('d2', 201),
        ('d2', 409)
    )
)
def test_mkdir_on_disk(dir_name, expected):
    result = mkdir_on_disk(dir_name)
    assert result == expected


@pytest.mark.parametrize(
    'dir_name,expected',
    (
        ('d1', True),
        ('d2', True),
        ('d3', False)
    )
)
def test_check_dir(dir_name, expected):
    result = check_dir(dir_name)
    assert result is expected
