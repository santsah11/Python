from flask import Flask # Flask, you importing because you need some WEB FRAME. that's let you generate the URL.
from vsearch import search4letters # this has been created the distribution file and ready to import. you can check the step in book.
app = Flask(__name__)
@app.route('/')
def hello()->str:
           return 'heloo world from flask!'
@app.route('/search4')
def do_search()->str:
    return str(search4letters('life is great in this area','eiou'))


app.run()         
           
