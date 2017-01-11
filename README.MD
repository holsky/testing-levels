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

 ## References

 https://martinfowler.com/bliki/TestPyramid.html

 ## Central insights from non-technical users

    * Proper testing requires effort and discipline
    * Seperating layers is hard and requires effort and discipline
    * TDD feels quite natural for domain problems
    * The got me that I directly went to "divisible by 5" instead of going via the cases "equals 5" and "divisible by 5"
    * Finding the right amont of tests is hard
    * Writing integration tests, that only test the integration but not the logic and do not break easily is hard
