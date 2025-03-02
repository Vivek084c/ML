from flask import Flask, request, render_template
import spacy
from spacy import displacy

app = Flask(__name__)

#creating the route
@app.route('/')
def home():
    return render_template('index.html')
#creating the route

@app.route('/entity', methods=['POST', 'GET'])
def entity():
    if request.method=='POST':
        #if the requested method is post the perform processing
        file = request.files['file']

        #checking if file content is present
        if file:
            readable_file  = file.read().deocde('utf-8', errors = 'ignore')
