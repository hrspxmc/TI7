from yachs_webpage import app
from flask import render_template
import yachs_webpage.data_model as data_model


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/yachts")
def yachts():
    return render_template("yachts.html", yachts=data_model.YachtType.query.all())


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("index.html")


@app.route("/calendar")
def calendar():

    rental_dates = data_model.RentalDate.query.all()
    yacht_models = data_model.YachtType.query.all()

    booked_dates = [
        {"id": xi,
        "group": int(x.unit.unit_type.id),
         "start": x.booked_from.strftime('%Y-%m-%d'),
         "end": x.booked_to.strftime('%Y-%m-%d'),
         "type": "range",
         "content": x.unit.unit_name}
        for xi, x in enumerate(rental_dates)
    ]

    groups_list = [
        {"id": int(x.id),
        "content": str(x.name)}
        for x in yacht_models 
    ]


    #return booked_dates
    #return groups_list
    return render_template("calendar.html", dates = booked_dates, groups = groups_list)
