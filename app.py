from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
@app.route('/report')
def report():  # put application's code here
    return render_template("report.html")


@app.route('/drivers')
def drivers():  # put application's code here
    return render_template("drivers.html")


@app.route('/driver_id')
def driver_id():  # put application's code here
    return render_template("driver_id.html")


@app.route('/about')
def about():  # put application's code here
    return render_template("about.html")


@app.route('/faqs')
def faqs():  # put application's code here
    return render_template("faqs.html")


if __name__ == '__main__':
    app.run()
