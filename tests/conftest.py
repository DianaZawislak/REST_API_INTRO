"""This is for test helper fixtures and configuration as needed"""
import pytest
import app


@pytest.fixture
def run_program():
    """This runs the program for the test"""
    app.setup()
