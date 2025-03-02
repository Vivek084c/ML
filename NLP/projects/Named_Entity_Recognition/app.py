from flask import Flask, request, render_template
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')


app = Flask(__name__)

#creating the route
@app.route('/')
def home():
    return render_template('index.html')
#creating the route

@app.route('/entity', methods=['POST', 'GET'])
def entity():
    html = None
    text = None

    if request.method=='POST':
        #if the requested method is post the perform processing
        file = request.files.get('file')

        #checking if file content is present
        if file:
            text  = file.read().decode('utf-8', errors='ignore')
            docs = nlp(text)

            #rendering to html 
            html = displacy.render(docs, style='ent')

            #returing the data to render on the html page
    return render_template('index.html', html=html, text = text)
        
#creating a main point
if __name__ == "__main__":
    app.run(debug=True)

