"""These tests should not be changed because I am using them for evaluation.
If you change these tests I will fail you
for the assignment.  If you change these tests a second time I will fail you for the course """
import logging
import os
from os.path import exists

import app
from tests.helpers import search_str_in_file


def test_always_passes():
    """This always passes"""
    assert True


def test_count_log_files(run_program):
    """Testing the number of files in the logs directory"""
    # pylint: disable=unused-argument
    action = len(os.listdir(app.Config.LOG_DIR))
    assert action == 4


def test_logger_for_debug_file(run_program):
    """Checks for the debug log file"""
    # pylint: disable=unused-argument
    debug_log_file_location = os.path.join(app.Config.LOG_DIR, "errors.log")
    assert exists(debug_log_file_location)


def test_logger_for_api_response_file(run_program):
    """Checks for the debug log file"""
    # pylint: disable=unused-argument
    debug_log_file_location = os.path.join(app.Config.LOG_DIR, "hotels_api_response.log")
    assert exists(debug_log_file_location)


def test_logger_running_program(run_program):
    """This tests that that logger of the program that is running
     is created with the correct name"""
    # pylint: disable=unused-argument
    assert id(logging.getLogger("errors")) == id(logging.getLogger("errors"))
    assert id(logging.getLogger("information")) == id(logging.getLogger("information"))


def test_hotels_api_response(run_program):
    # pylint: disable=unused-argument, singleton-comparison, line-too-long
    """checks if the string is found in the Hotels API Response"""
    assert search_str_in_file(os.path.abspath(os.path.join(app.Config.BASE_DIR, '..', 'logs', 'hotels_api_response.log')), 'new') == True
