from logging import FileHandler, WARNING
from flask import Flask, render_template,request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__,template_folder="templates")
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sampledb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
today = date.today()

class Notices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable = False)
    Name = db.Column(db.String, nullable = False)
    Description = db.Column(db.String, nullable = False)

@app.route("/")
def home():
    all_data = Notices.query.all()
    return render_template('index.html',notices = all_data)

@app.route("/notices", methods =['GET','POST'])
def play_with_notices():
    return render_template('notices.html')

@app.route("/add-notice", methods =['GET','POST'])
def add_notice():
    if request.method == 'POST':
        DATE = request.form.get('date')
        NAME = request.form.get('name')
        DESC = request.form.get('description')
        data = Notices(date = DATE, Name = NAME, Description = DESC)
        db.session.add(data)
        db.session.commit()

        flash("New Notice added")
    return render_template('add-notice.html')

@app.route("/update-notice", methods =['GET','POST'])
def update_notice():
    if request.method== 'POST':
        ID = request.form.get('id')
        NAME = request.form.get('noticename')
        DATE = request.form.get('noticedate')
        DESC =  request.form.get('noticedescription')
        data = Notices.query.filter_by(id=ID).first()
        data.Name = NAME
        data.date = DATE
        data.Description = DESC
        db.session.commit()
        flash("Notice Updated Successfully")
    return render_template('update-notice.html')

@app.route("/delete-notice", methods =['GET','POST'])
def delete_notice():
    if request.method == 'POST':
        ID = request.form.get('noticeid')
        Notices.query.filter_by(id=ID).delete()
        db.session.commit()
        flash("Notice Deleted Successfully")
    return render_template('delete-notice.html')

app.run(debug=True)