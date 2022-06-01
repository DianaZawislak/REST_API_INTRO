# REST API Introduction

### Name: Diana Zawislak

### UCID: DZ29

## Introduction

The purpose of this unit is to introduce you to what an API is and to signup for a RapidAPI account.

## Assignment Tasks

For this assignment you need to read a few articles, pick an API to make a request, and save the response into a log
file called "api_response.log" .

## Steps to Complete the Assignment

1. Put your name and UCID at the top of this file where indicated
2. Clone this repo and run pip install -r requirements.txt to install the dependencies
3. Signup for RapidAPI - [here](https://rapidapi.com/auth/sign-up)
4. Subscribe to the Hotels api here - [here](https://rapidapi.com/apidojo/api/hotels4)
5. Put that Hotels API key in the .env file
6. Run pytest to see that the response is saved in logs/hotels_api_response.log
7. Look around at the different API and subscribe to at least one other API (some are free and some cost money) and
   create a new function in the program to make a request and save the information into its own log file called the name
   of the api.  I used Burgers
8. Write a test in that tests/test_task1.py file for your new function and check that log file you will save your api
   response in exists like I check in my test
9. Write a test in that tests/test_task2.py file for your new function to check that the contents of the file contain
   what you expect like I did in my test
10. When you are satisfied commit and push the repo back and then submit a link to your repository in the Canvas assignment.

NOTE: The tests won't automatically pass because my tests are looking for a 4th file to be created, which is the api log
file you will create

You get 50 points for each task test.

### Unit Video - [Watch Here](https://youtu.be/MDC43ksUwEc)*
* In the video the problem was I didn't have a .env file, you won't have this problem

## Required Readings

1. Read this article to introduce you to what a REST API is [here](https://blog.hubspot.com/website/what-is-rest-api)
2. HTTP Basic Guide from Steve - This is good [here](http://www.steves-internet-guide.com/http-basics/)
3. HTTP Request Method [here](https://rapidapi.com/blog/api-glossary/http-request-methods/)

### References and Articles used for Assignment - Good articles and required if you don't understand what unit tests or logging is. Logging and unit testing are fundamental skills for development and Devops

1. [Python dotenv file reading library](https://pypi.org/project/python-dotenv/)
2. [Python reference for HTTP client library that we are using](https://docs.python.org/3/library/http.client.html)
3. [The article on logging I use for the assignment](https://realpython.com/python-logging/)
4. [TopTotal - Developoer Testing Tutorial on Logging](https://www.toptal.com/python/in-depth-python-logging)
5. [Logging Tutorial in Python - Another one I Used](https://www.loggly.com/ultimate-guide/python-logging-basics/)
6. [Python Logging Handlers Explained](https://docs.python.org/3/library/logging.handlers.html)
7. [Read the documentation on logging from Python](https://docs.python.org/3/library/logging.html)
8. [Pytest - Python Unit Test Framework we Use](https://docs.pytest.org/en/7.1.x/how-to/index.html)
9. [Python File Operations](https://www.programiz.com/python-programming/file-operation)
10. [Python Directory Operations](https://www.journaldev.com/14417/python-directory-create-rename-delete)
11. [Read this article on logging](https://machinelearningmastery.com/logging-in-python/)
12. [Pylint Tutorial - Coding Standards](https://pylint.pycqa.org/en/latest/tutorial.html)
13. [PEP-8 Python Coding Standards](https://realpython.com/python-pep8/)
14. Read this article about how automated tests are used at
    Google [here](https://itrevolution.com/case-study-automated-testing-google/)
15. Read this article from Fowler on Continuous Delivery [here](https://martinfowler.com/bliki/ContinuousDelivery.html)
16. Read this article from one of the luminaries in software
    engineering [here](https://martinfowler.com/articles/continuousIntegration.html)  this article is the foundation of
    devops and started the revolution in coding.
17. Read this on AAA testing [here](https://freecontent.manning.com/making-better-unit-tests-part-1-the-aaa-pattern/)