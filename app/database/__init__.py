from app.routes import db

class Car(db.Model):
    carId = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    mileage = db.Column(db.Numeric(precision=7, scale=1), nullable=False)
    color = db.Column(db.String, nullable=False)
    vin = db.Column(db.String(17), nullable=False)
    condition = db.Column(db.String(9), nullable=False)
    cost = db.Column(db.Numeric(precision=7, scale=2), nullable=False)
    price = db.Column(db.Numeric(precision=7, scale=2), nullable=False)
    description = db.Column(db.String, nullable=True, default=None)
    pic1 = db.Column(db.String, nullable=False)
    pic2 = db.Column(db.String, nullable=True, default=None)
    pic3 = db.Column(db.String, nullable=True, default=None)
    sold = db.Column(db.Boolean, nullable=False, default=0)
    sold_by = db.Column(db.Integer, nullable=True, default=None)
    sales_price = db.Column(db.Numeric(precision=7, scale=2), nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=1)

    def __repr__(self):
        return "<Vehicle %r> %r %r VIN: %r" % (
            self.carId, self.make, self.model, self.vin
            )

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=1)

    def __repr__(self):
        return "Employee #%r: %r %r" % (
            self.id, self.first_name, self.last_name
        )

def scan():
    cursor = db.query.all()
    print(cursor)