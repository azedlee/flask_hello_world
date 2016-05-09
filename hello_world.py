from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!!!"

#@app.route("/hello/<name>")
#def hi_person(name):
#    return "Hello {}!".format(name.title())

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
@app.route("/jedi/<first>/<last>")
def jedi(first, last):
    first = first[0:2]
    last = last[0:3]
    return "Welcome, Young {1}{0}!".format(first.title(), last.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))