"""This is the app demonstrates logging configuration and unit testing"""

import http.client
import logging
import logging.config
import os
import traceback

from dotenv import load_dotenv


class Config(object):
    """This provides configuration information"""
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
    LOG_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'logs'))


def hotels_api_request():
    """This makes a request to hotels on rapid api and saves the request to the hotels_api_response logger"""
    # This creates and HTTP connection to make a request

    conn = http.client.HTTPSConnection('hotels4.p.rapidapi.com')

    # this sets up an HTTP Request
    headers = {
        'X-RapidAPI-Host': 'hotels4.p.rapidapi.com',
        'X-RapidAPI-Key': os.getenv('HOTEL_API_KEY')  # gets the rapid API key from the .env file
    }

    # this makes the actual request.
    conn.request("GET", '/locations/v2/search?query=new%20york&locale=en_US&currency=USD', headers=headers)
    # this gets the response data

    res = conn.getresponse()
    # this reads the response data and stores it in a data variable
    data = res.read()
    # this gets the logger to use to store the output
    info_logger = logging.getLogger("hotels_api_response")
    info_logger.info(data.decode("utf-8"))

def world_cities_api_request():
    """This makes a request to world cities on rapid api and saves the request to the hotels_api_response logger"""
    # This creates and HTTP connection to make a request

    conn = http.client.HTTPSConnection('andruxnet-world-cities-v1.p.rapidapi.com')

    # this sets up an HTTP Request
    headers = {
        'X-RapidAPI-Host': 'andruxnet-world-cities-v1.p.rapidapi.com',
        'X-RapidAPI-Key': os.getenv('WORLD_CITIES_API_KEY')  # gets the rapid API key from the .env file
    }

    # this makes the actual request.
    conn.request("GET", "/?query=paris&searchby=city", headers=headers)
    # this gets the response data

    res = conn.getresponse()
    # this reads the response data and stores it in a data variable
    data = res.read()
    # this gets the logger to use to store the output
    info_logger = logging.getLogger("world_cities_api_response")
    info_logger.info(data.decode("utf-8"))

def main():
    """This is the main function that is run"""
    # this loads the info from the .env file
    #this is my hotels api request that stores the response in the hotels_api_reponse_logger
    hotels_api_request()
    world_cities_api_request()


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'just_message': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file.handler.errors': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'errors.log'),
            'maxBytes': 10000000,
            'encoding': 'utf-8',
            'backupCount': 5,
        },
        'file.handler.hotels_api_response': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'just_message',
            'filename': os.path.join(Config.LOG_DIR, 'hotels_api_response.log'),
            'encoding': 'utf-8',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.world_cities_api_response': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'just_message',
            'filename': os.path.join(Config.LOG_DIR, 'world_cities_api_response.log'),
            'encoding': 'utf-8',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.default_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'root_logger_default.log'),
            'maxBytes': 10000000,
            'encoding': 'utf-8',
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default', 'file.handler.default_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default', 'file.handler.default_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'hotels_api_response': {
            'handlers': ['file.handler.hotels_api_response'],
            'level': 'INFO',
            'propagate': False
        },

        'world_cities_api_response': {
            'handlers': ['file.handler.world_cities_api_response'],
            'level': 'INFO',
            'propagate': False
        },
        'errors': {  # if __name__ == '__main__'
            'handlers': ['default', 'file.handler.errors'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}


def setup_logs():
    # set the name of the apps log folder to logs
    logdir = Config.LOG_DIR
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    # this loads the log configuration
    logging.config.dictConfig(LOGGING_CONFIG)


def setup():
    """This is used to run the program and setup logging to print exceptions to the logs/errors.log file"""
    setup_logs()
    load_dotenv()
    try:
        main()
    except Exception as e:
        app_log = logging.getLogger("errors")
        app_log.debug(traceback.format_exc())


if __name__ == '__main__':
    """This causes the setup function to be called if this is the __main__ top level of code This makes this file a 
    script that can be run from the command line"""
    setup()
