from yachs_webpage import app
from flask import render_template
import yachs_webpage.data_model as data_model

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/yachts')
def yachts():
    return render_template("yachts.html", yachts = data_model.YachtType.query.all()) 

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("index.html")
    
@app.route('/calendar')
def calendar():
    return render_template("calendar.html") 
