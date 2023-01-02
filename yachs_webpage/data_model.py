from yachs_webpage import db, app
import datetime

class YachtType(db.Model):
    __tablename__ = "YachtTypes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    hull_type = db.Column(db.String)
    rigging_type = db.Column(db.String)
    length_overall = db.Column(db.Float)
    beam = db.Column(db.Float)
    draft = db.Column(db.Float)
    first_built = db.Column(db.DateTime)

class Yacht(db.Model):
    __tablename__ = "Yachts"
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey("YachtTypes.id"))
    unit_type = db.relationship('YachtType', foreign_keys = type_id)
    unit_name = db.Column(db.String)
    built_date = db.Column(db.DateTime)

class RentalDate(db.Model):
    __tablename__ = "RentalDates"
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey("Yachts.id"))
    unit = db.relationship('Yacht', backref=db.backref('rental_date'))
    booked_from = db.Column(db.DateTime)
    booked_to = db.Column(db.DateTime)

yacht_1 = YachtType(
    name = "ALLURES 51.9",
    description = "fine yacht",
    hull_type = "Keel/CB w/dual rudders",
    rigging_type = "Cutter",
    length_overall = 16.67,
    beam = 4.82,
    draft = 2.92,
    first_built = datetime.date(2021, 1, 1)
)

unit_1 = Yacht(
    unit_type = yacht_1,
    unit_name = "Titanic3",
    built_date = datetime.date(2022, 1, 1)
)

unit_2 = Yacht(
    unit_type = yacht_1,
    unit_name = "Titanic5",
    built_date = datetime.date(2022, 2, 1)
)

rt_date = RentalDate(
    unit= unit_1,
    booked_from = datetime.date(2021, 1, 1),
    booked_to = datetime.date(2021, 2, 1)
)

with app.app_context():
    db.create_all()
    db.session.add(yacht_1)
    db.session.add(unit_1)
    db.session.add(unit_2)
    db.session.add(rt_date)
    db.session.commit()