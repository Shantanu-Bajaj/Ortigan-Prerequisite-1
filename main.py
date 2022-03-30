'''importing required packages'''
from flask import Flask, render_template,request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__,template_folder="templates")                           #creating a Flask app object
app.secret_key = "Secret Key"                                               #providing a secret key for session
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sampledb'  #configuring Database Parameters
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                        #Disabling Track modifications of objects

db = SQLAlchemy(app)                #Creating SQLAlchemy object
today = date.today()                #Retrieving system date

class Notices(db.Model):                                    #creating class for database Table
    id = db.Column(db.Integer, primary_key=True)            #creating DM for id attribute
    date = db.Column(db.String, nullable = False)           #creating DM for date attribute
    Name = db.Column(db.String, nullable = False)           #creating DM for Name attribute
    Description = db.Column(db.String, nullable = False)    #creating DM for Description attribute

@app.route("/")                     #creating route for index page
def home():
    all_data = Notices.query.all()              #retrieving all data from Notices Table
    today_data = Notices.query.filter_by(date=today.strftime("%Y-%m-%d"))           #retrieving system dates' data from Notices Table
    return render_template('index.html',notices = all_data,Today_notices = today_data)  #rendering index page with all Notices data and current dates' notices

@app.route("/notices", methods =['GET','POST'])             #route for notices page
def play_with_notices():
    return render_template('notices.html')              #rendering notices page

@app.route("/add-notice", methods =['GET','POST'])          #route for adding a notice
def add_notice():                                   #function to perfrom create operation
    if request.method == 'POST':                    #checking if a request is POST or GET
        DATE = request.form.get('date')                #retrieving date entered by user in form
        NAME = request.form.get('name')                #retrieving name entered by user in form
        DESC = request.form.get('description')                      #retrieving description entered by user in form
        data = Notices(date = DATE, Name = NAME, Description = DESC)   #adding user's entered data in Database Table
        db.session.add(data)
        db.session.commit()                     #commiting session

        flash("New Notice added")               #adding a flash message to prompt the user
    return render_template('add-notice.html')       #rendering add notice page

@app.route("/update-notice", methods =['GET','POST'])   #route for updating a notice
def update_notice():                    #function to perfrom update operation
    if request.method== 'POST':          #checking if a request is POST or GET
        ID = request.form.get('id')         #retrieving id entered by user in form to update the details
        NAME = request.form.get('noticename')   #retrieving new Name entered by user in form
        DATE = request.form.get('noticedate')      #retrieving new Date entered by user in form
        DESC =  request.form.get('noticedescription')     #retrieving new Description entered by user in form
        data = Notices.query.filter_by(id=ID).first()     #retrieving the data of Id entered by user
        data.Name = NAME                    #updating new Name in database
        data.date = DATE                    #updating new Date in database
        data.Description = DESC             #updating new Description in database
        db.session.commit()                 #commiting session
        flash("Notice Updated Successfully")            #prompting the user by putting a flash message
    return render_template('update-notice.html')        #rendering update notice html page

@app.route("/delete-notice", methods =['GET','POST'])               #route for deleting a notice
def delete_notice():                       #function to perfrom delete operation
    if request.method == 'POST':            #checking if a request is POST or GET
        ID = request.form.get('noticeid')           #retrieving id entered by user in form to delete the record
        Notices.query.filter_by(id=ID).delete()             #deleting the data of Id entered by user
        db.session.commit()                                #commiting session
        flash("Notice Deleted Successfully")                #prompting the user by putting a flash message
    return render_template('delete-notice.html')        #rendering delete notice html page

app.run(debug=True)         #enabling debug mode so that changes are reflected in terminal