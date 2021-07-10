from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cars.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'secret key'
db = SQLAlchemy(app)
from app.database import Car
from app.forms.cars import CarForm
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/cars")
def get_all_vehicles():
    cars = Car.query.filter_by(active=True)
    return render_template("cars.html", car_list=cars)

@app.route("/inactive")
def get_inactive_vehicles():
    cars = Car.query.filter_by(active=False)
    return render_template("cars.html", car_list=cars)

@app.route("/cars/<int:cid>")
def get_car_detail(cid):
    car = Car.query.filter_by(carId=cid).first()
    return render_template("cardetail.html", car=car)

@app.route("/cars/create")
def create_car_form(): 
    car_form = CarForm()
    return render_template("create_form.html", form=car_form)

@app.route("/cars/update/<int:cid>")
def update_car_form(cid):
    car_form = CarForm()
    car = Car.query.filter_by(carId=cid).first()
    return render_template("update_form.html", form=car_form, car=car)

@app.route("/cars/<int:cid>", methods=["POST"])
def update_car(cid):
    form = CarForm(request.form)
    print("Validating data")
    if form.validate():
        print("Data validated")
        car = Car.query.filter_by(carId=cid).first()
        car.make = form.make.data
        car.model = form.model.data
        car.mileage = form.mileage.data
        car.color = form.color.data
        car.vin = form.vin.data
        car.condition = form.condition.data
        car.cost = form.cost.data
        car.price = form.price.data
        car.description = form.description.data
        car.pic1 = form.pic1.data
        car.pic2 = form.pic2.data
        car.pic3 = form.pic3.data
        car.sold = form.sold.data
        car.sold_by = form.sold_by.data
        db.session.commit()
        flash("Car Updated!")
        return redirect(url_for('get_all_vehicles'))
    print(form.errors)
    flash("Invalid data on update!")
    return redirect(url_for('get_all_vehicles'))

@app.route("/cars/delete/<int:cid>")
def delete_car(cid):
    car = Car.query.filter_by(carId=cid).first()
    car.active = False
    db.session.commit()
    flash("Car deleted!")
    return redirect(url_for('get_all_vehicles'))

@app.route("/cars/activate/<int:cid>")
def activate_car(cid):
    car = Car.query.filter_by(carId=cid).first()
    car.active = True
    db.session.commit()
    flash("Car activated!")
    return redirect(url_for('get_all_vehicles'))



@app.route("/cars", methods=["POST"])
def create_car():
    form = CarForm(request.form)
    print("Form created")
    if form.validate():
        print("Form validated")
        car = Car()
        car.make = form.make.data
        car.model = form.model.data
        car.mileage = form.mileage.data
        car.color = form.color.data
        car.vin = form.vin.data
        car.condition = form.condition.data
        car.cost = form.cost.data
        car.price = form.price.data
        car.description = form.description.data
        car.pic1 = form.pic1.data
        car.pic2 = form.pic2.data
        car.pic3 = form.pic3.data
        car.sold = form.sold.data
        car.sold_by = form.sold_by.data
        db.session.add(car)
        db.session.commit()
        flash("Product created!")
        return redirect(url_for('get_all_vehicles'))
    flash("Invalid data!")
    return redirect(url_for('get_all_cars'))