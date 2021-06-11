from flask import Flask, render_template

from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('request.html')


@app.route("/login", methods=["post"])
def login():

    id = request.form.get('id')
    info = {"name":"이재선", "age":30, "생년월일":971203}

    return render_template('response.html', idencore=id, userinfo=info)





if __name__ == '__main__':
    app.run(debug=True)