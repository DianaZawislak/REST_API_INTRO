""" Write your test for the task here"""
import os

import app
from tests.helpers import search_str_in_file


def test_world_cities_api_response(run_program):
    # pylint: disable=unused-argument, singleton-comparison, line-too-long
    """checks if the string is found in the Worlds Cities API Response"""
    assert search_str_in_file(os.path.abspath(os.path.join(app.Config.BASE_DIR, '..', 'logs', 'world_cities_api_response.log')), 'new') == True