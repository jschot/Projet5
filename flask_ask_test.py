from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def start():
    return question("Voulez-vous jouez ?")


@ask.intent('VraiFaux')
def vraifaux():
    return statement("ok")

@ask.intent('NonIntent')
def non() :
    return statement("Tant pis")


if __name__ == '__main__':
    app.run()