import requests
import click
from click.testing import CliRunner
import json
import pytest

from hackernews import hackernews


BASE_URL = 'https://hacker-news.firebaseio.com/v0/'

@pytest.fixture(scope="module")
def runner():
    return CliRunner()

def test_string_arg(runner):
    result = runner.invoke(hackernews, ['--posts', 'a'])
    assert result.exit_code == 2

@pytest.mark.parametrize("posts", [0, 110, -4])
def test_invalid_int(runner, posts):
    result = runner.invoke(hackernews, ['--posts', posts])

    assert 'Please select a number between 1 and 100' in result.output

def test_no_arg(runner):
    result = runner.invoke(hackernews)
    json_result = json.loads(result.output)

    assert len(json_result) == 1

@pytest.mark.parametrize("posts", [3, 5, 10])
def test_number_of_posts(runner, posts):
    result = runner.invoke(hackernews, ['--posts', posts])
    json_result = json.loads(result.output)

    assert len(json_result) == posts

def test_get_topstories():
    response = requests.get(url=f'{BASE_URL}topstories.json')

    assert response.status_code == 200

def test_get_post():
    post_id = 20924667
    response = requests.get(url=f'{BASE_URL}item/{post_id}.json')

    assert response.status_code == 200
