# Testing Levels Example

This is a small application to illustrate to non-technical people what different testing levels look and feel like.

The application implements the FizzBuzz challenge as a HTTP endpoint, */<number>*, that returns the correct answer.

Different testing levels are

    * unit, where we test the actual FizzBuzz logic
    * integration, where we test the wiring of the flask app and that all endpoints are present
    * system, where we execute a selenium test to test the whole system

## Setup

I needed to install the following tools & libraries:

   * virtualenv, add this to venv/bin/activate to enable flask and import from tests
   		export FLASK_APP=levels_app.py
		export PYTHONPATH="/path/to/app:$PYTHONPATH"
   * chromedriver: https://chromedriver.storage.googleapis.com/, add the executable to ~/bin
   * via pip: selenium flask