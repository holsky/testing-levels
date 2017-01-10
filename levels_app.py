from flask import Flask
app = Flask(__name__)

# template with actual IDs so Selenium can find it
template = """
<html>
<body>
<div>And the answer is: <div id="answer">{}</div></div>
</body>
</html>"""

# entry for help message on empty call
@app.route('/')
def index():
	return "Enter a number as parameter to get its fizzbuzzed name"

# entry for /1 call
@app.route('/<int:number>')
def answer_fizzbuzz(number):
    return template.format(fizzbuzz(number))

# actual business logic
def fizzbuzz(number):
	return "1"