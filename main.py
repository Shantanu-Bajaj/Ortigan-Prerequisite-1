from flask import Flask, render_template,request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sampledb'

db = SQLAlchemy(app)
today = date.today()

class Notices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable = False)
    Name = db.Column(db.String, nullable = False)
    Description = db.Column(db.String, nullable = False)

@app.route("/")
def index():
    all_data = Notices.query.all()
    '''today_data = Notices.query.get(request.form.get('date'))
    for data in today_data:
        if data.equals(today.strftime("%Y-%m-%d")):
            return render_template('index.html', Today_notices = data)'''
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
        #data = Notices.query.get(request.form.get(''))
        pass
    return render_template('update-notice.html')

@app.route("/delete-notice", methods =['GET','POST'])
def delete_notice():
    return render_template('delete-notice.html')


app.run(debug=True)