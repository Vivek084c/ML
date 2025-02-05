from flask import Flask, render_template, request

# create a flask app
app = Flask(__name__)

@app.route('/')
def index():
    return """
     <html>
        <body>
            <form action="/greet" method="POST">
                Enter your name: <input type="text" name="username">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    """

@app.route('/greet', methods=['POST'] )
def greete():
    user_input = request.form['username']
    return f" hellow {user_input}, wecome here!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8889)
