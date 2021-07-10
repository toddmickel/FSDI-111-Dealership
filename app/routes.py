from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cars.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'secret key'
db = SQLAlchemy(app)
from app.database import Car
from app.database import Employee
from app.forms.cars import CarForm
from app.forms.employees import EmployeeForm
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/cars")
def get_all_vehicles():
    cars = Car.query.filter_by(active=True)
    return render_template("cars.html", car_list=cars)

@app.route("/employees")
def get_all_employees():
    employees = Employee.query.filter_by(active=True)
    cars = Car.query.filter_by(sold=True)
    return render_template("employees.html", employee_list=employees, car_list=cars)

@app.route("/cars/inactive")
def get_inactive_vehicles():
    cars = Car.query.filter_by(active=False)
    return render_template("cars.html", car_list=cars)

@app.route("/employees/inactive")
def get_inactive_employees():
    employees = Employee.query.filter_by(active=False)
    cars = Car.query.filter_by(sold=True)
    return render_template("employees.html", employee_list=employees, car_list=cars)    

@app.route("/cars/<int:cid>")
def get_car_detail(cid):
    car = Car.query.filter_by(carId=cid).first()
    employee = Employee.query.filter(Employee.id==car.sold_by).first()
    return render_template("cardetail.html", car=car, employee=employee)

@app.route("/employees/<int:id>")
def get_employee_detail(id):
    employee = Employee.query.filter_by(id=id).first()
    cars = Car.query.filter_by(sold=True)
    return render_template("employee_detail.html", employee=employee, car_list=cars)

@app.route("/cars/create")
def create_car_form(): 
    car_form = CarForm()
    return render_template("create_form.html", form=car_form)

@app.route("/employees/create")
def create_employee_form():
    employee_form = EmployeeForm()
    return render_template("create_employee_form.html", form=employee_form)

@app.route("/cars/update/<int:cid>")
def update_car_form(cid):
    car = Car.query.filter_by(carId=cid).first()
    car_form = CarForm(obj=car)
    return render_template("update_car_form.html", form=car_form, car=car)

@app.route("/emplorees/update/<int:id>")
def update_employee_form(id):
    employee = Employee.query.filter_by(id=id).first()
    employee_form = EmployeeForm(obj=employee)
    return render_template("update_employee_form.html", form=employee_form, employee=employee)

@app.route("/cars/<int:cid>", methods=["POST"])
def update_car(cid):
    form = CarForm(request.form)
    if form.validate():
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
        if car.sold == True:
            car.sold_by = form.sold_by.data
            car.sales_price = form.sales_price.data
        else:
            car.sold_by = ""
            car.sales_price = 0
        db.session.commit()
        flash("Car Updated!")
        return redirect(url_for('get_all_vehicles'))
    print(form.errors)
    flash("Invalid data on update!")
    return redirect(url_for('get_all_vehicles'))

@app.route("/employees/<int:id>", methods=["POST"])
def update_employee(id):
    form = EmployeeForm(request.form)
    if form.validate():
        employee = Employee.query.filter_by(id=id).first()
        employee.first_name = form.first_name.data
        employee.last_name = form.last_name.data
        db.session.commit()
        flash("Employee updated!")
        return redirect(url_for('get_all_employees'))
    print(form.errors)
    flash("Invalid data on update!")
    return redirect(url_for('get_all_employees'))

@app.route("/cars/delete/<int:cid>")
def delete_car(cid):
    car = Car.query.filter_by(carId=cid).first()
    car.active = False
    db.session.commit()
    flash("Car deleted!")
    return redirect(url_for('get_inactive_vehicles'))

@app.route("/employees/delete/<int:id>")
def deactivate_employee(id):
    employee = Employee.query.filter_by(id=id).first()
    employee.active = False
    db.session.commit()
    flash("Employee disabled!")
    return redirect(url_for('get_inactive_employees'))

@app.route("/cars/activate/<int:cid>")
def activate_car(cid):
    car = Car.query.filter_by(carId=cid).first()
    car.active = True
    db.session.commit()
    flash("Car activated!")
    return redirect(url_for('get_all_vehicles'))

@app.route("/employees/activate/<int:id>")
def activate_employee(id):
    employee = Employee.query.filter_by(id=id).first()
    employee.active = True
    db.session.commit()
    flash("Employee enabled!")
    return redirect(url_for('get_all_employees'))

@app.route("/cars", methods=["POST"])
def create_car():
    form = CarForm(request.form)
    if form.validate():
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

@app.route("/employees", methods=["POST"])
def create_employee():
    form = EmployeeForm(request.form)
    if form.validate():
        employee = Employee()
        employee.first_name = form.first_name.data
        employee.last_name = form.last_name.data
        db.session.add(employee)
        db.session.commit()
        flash("Employee created!")
        return redirect(url_for('get_all_employees'))
    flash("Invalid data for new employee!")
    return redirect(url_for('get_all_employees'))