""" Write your test for the task here"""
import os
from os.path import exists

import app


def test_logger_for_world_cities_api_response_file(run_program):
    """Checks for the world_cities_api_response log file"""
    # pylint: disable=unused-argument
    debug_log_file_location = os.path.join(app.Config.LOG_DIR, "world_cities_api_response.log")
    assert exists(debug_log_file_location)
