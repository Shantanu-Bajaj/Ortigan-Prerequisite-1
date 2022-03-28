from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sampledb'
db = SQLAlchemy(app)

class Notices(db.Model):
    '''id date Name Description'''
    id = db.Column(db.Integer, nullable = False)
    date = db.Column(db.String, nullable = False)
    Name = db.Column(db.String, nullable = False)
    Description = db.Column(db.String, primary_key=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/notices", methods =['GET','POST'])
def play_with_notices():
    return render_template('notices.html')

@app.route("/add-notice", methods =['GET','POST'])
def add_notice():
    
    return render_template('add-notice.html')

@app.route("/update-notice", methods =['GET','POST'])
def update_notice():
    return render_template('update-notice.html')

@app.route("/delete-notice", methods =['GET','POST'])
def delete_notice():
    return render_template('delete-notice.html')


app.run(debug=True)