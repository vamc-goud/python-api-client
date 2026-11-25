# Python API Client

## Description

A modular Python application that retrieves
task information from a REST API.

## Technologies

- Python
- Requests
- REST API
- JSON
- Git and GitHub

## Features

- Retrieve tasks by ID
- Validate user input
- Handle HTTP errors
- Handle connection timeouts
- Process JSON responses

## Installation

python -m venv .venv

python -m pip install -r requirements.txt

## Run

python -m app.main

## Testing

Run all automated tests using:

python -m unittest discover -v

The test suite checks:

- Successful API responses
- Invalid task IDs
- API timeouts
- HTTP errors
- Invalid JSON
- Unexpected response formats