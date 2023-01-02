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
    unit_type = db.relationship("YachtType", foreign_keys=type_id)
    unit_name = db.Column(db.String)
    built_date = db.Column(db.DateTime)


class RentalDate(db.Model):
    __tablename__ = "RentalDates"
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey("Yachts.id"))
    unit = db.relationship("Yacht", backref=db.backref("rental_date"))
    booked_from = db.Column(db.DateTime)
    booked_to = db.Column(db.DateTime)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


yachts = [
    YachtType(
        name="Verne",
        description="fine yacht",
        hull_type="Keel/CB w/dual rudders",
        rigging_type="Kuter",
        length_overall=16.67,
        beam=3.82,
        draft=2.92,
        first_built=datetime.date(2021, 1, 1),
    ),
    YachtType(
        name="Supremator",
        description="fine yacht",
        hull_type="Keel/CB w/dual rudders",
        rigging_type="Galera",
        length_overall=11.67,
        beam=4.62,
        draft=2.22,
        first_built=datetime.date(2021, 1, 1),
    ),
    YachtType(
        name="Papaj",
        description="fine yacht",
        hull_type="Keel/CB w/dual rudders",
        rigging_type="Krążownik",
        length_overall=12.67,
        beam=4.62,
        draft=2.73,
        first_built=datetime.date(2021, 1, 1),
    ),
    YachtType(
        name="Nemo",
        description="fine yacht",
        hull_type="Keel/CB w/dual rudders",
        rigging_type="Lotniskowiec",
        length_overall=26.67,
        beam=8.82,
        draft=6.92,
        first_built=datetime.date(2021, 1, 1),
    ),
    YachtType(
        name="Marszałek",
        description="fine yacht",
        hull_type="Keel/CB w/dual rudders",
        rigging_type="Fregata",
        length_overall=22.67,
        beam=21.82,
        draft=5.92,
        first_built=datetime.date(2021, 1, 1),
    ),
]

units = [
    Yacht(unit_type=yachts[0], unit_name="Karol I", built_date=datetime.date(2021, 1, 1)),
    Yacht(unit_type=yachts[0], unit_name="Jan II", built_date=datetime.date(2021, 1, 1)),
    Yacht(unit_type=yachts[1], unit_name="Agata IV", built_date=datetime.date(2021, 1, 1)),
    Yacht(unit_type=yachts[1], unit_name="Wojtek X", built_date=datetime.date(2021, 1, 1)),
    Yacht(unit_type=yachts[2], unit_name="Zosia V", built_date=datetime.date(2021, 1, 1)),
    Yacht(unit_type=yachts[3], unit_name="Asia VI", built_date=datetime.date(2021, 1, 1)),
    Yacht(
        unit_type=yachts[4], unit_name="Borubar IX", built_date=datetime.date(2021, 1, 1)
    ),
    Yacht(unit_type=yachts[4], unit_name="Wojnar XI", built_date=datetime.date(2021, 1, 1)),
]

rental_dates = [
    RentalDate(
        unit=units[0],
        booked_from=datetime.date(2021, 2, 3),
        booked_to=datetime.date(2021, 2, 8),
    ),
    RentalDate(
        unit=units[1],
        booked_from=datetime.date(2021, 1, 3),
        booked_to=datetime.date(2021, 2, 8),
    ),
    RentalDate(
        unit=units[2],
        booked_from=datetime.date(2021, 1, 3),
        booked_to=datetime.date(2021, 1, 23),
    ),
    RentalDate(
        unit=units[3],
        booked_from=datetime.date(2021, 1, 13),
        booked_to=datetime.date(2021, 3, 2),
    ),
    RentalDate(
        unit=units[4],
        booked_from=datetime.date(2021, 2, 3),
        booked_to=datetime.date(2021, 2, 22),
    ),
    RentalDate(
        unit=units[5],
        booked_from=datetime.date(2021, 2, 3),
        booked_to=datetime.date(2021, 3, 1),
    ),
    RentalDate(
        unit=units[6],
        booked_from=datetime.date(2021, 1, 3),
        booked_to=datetime.date(2021, 2, 6),
    ),
    RentalDate(
        unit=units[7],
        booked_from=datetime.date(2021, 2, 3),
        booked_to=datetime.date(2021, 2, 8),
    ),
    RentalDate(
        unit=units[7],
        booked_from=datetime.date(2021, 3, 3),
        booked_to=datetime.date(2021, 4, 8),
    ),
    RentalDate(
        unit=units[1],
        booked_from=datetime.date(2021, 3, 31),
        booked_to=datetime.date(2021, 5, 1),
    ),
    RentalDate(
        unit=units[0],
        booked_from=datetime.date(2021, 3, 13),
        booked_to=datetime.date(2021, 4, 8),
    ),
    RentalDate(
        unit=units[1],
        booked_from=datetime.date(2021, 3, 5),
        booked_to=datetime.date(2021, 3, 10),
    ),
    RentalDate(
        unit=units[2],
        booked_from=datetime.date(2021, 3, 13),
        booked_to=datetime.date(2021, 3, 28),
    ),
    RentalDate(
        unit=units[3],
        booked_from=datetime.date(2021, 3, 11),
        booked_to=datetime.date(2021, 3, 18),
    ),
    RentalDate(
        unit=units[4],
        booked_from=datetime.date(2021, 3, 16),
        booked_to=datetime.date(2021, 4, 18),
    ),
    RentalDate(
        unit=units[5],
        booked_from=datetime.date(2021, 3, 3),
        booked_to=datetime.date(2021, 4, 18),
    ),
    RentalDate(
        unit=units[6],
        booked_from=datetime.date(2021, 3, 1),
        booked_to=datetime.date(2021, 5, 12),
    )
]


with app.app_context():
    db.create_all()
    [db.session.add(x) for x in yachts]
    [db.session.add(x) for x in units]
    [db.session.add(x) for x in rental_dates]
    db.session.commit()
