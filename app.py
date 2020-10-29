from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgressql://postgres:Post_Gres@1234@localhost/height_collector'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Post_Gres@1234@localhost:5432/height_collector"
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id=db.Column(db.Integer, primary_key=True)
    email_ =db.Column(db.String(120), unique=True)
    height_ =db.Column(db.Integer)

    def __init__(self, email, height):
        self.email_ = email_
        self.height_ = height_

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['post'])
def success():
    if request.method=='post':
        email=request.form["email_name"]
        height=request.form["height_name"]
        print(email, height)
        print(request.form)
    return render_template("success.html")


# Data()

if __name__ == '__main__':
    app.debug=True
    app.run()