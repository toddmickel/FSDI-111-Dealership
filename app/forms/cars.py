#!/usr/bin/env python3
#-*- coding:utf8 -*-

from wtforms import (
    Form,
    StringField,
    FloatField,
    IntegerField,
    TextField,
    SelectField,
    BooleanField,
    validators
)


class CarForm(Form):
    style = {"style": "width:100%"}
    make = StringField("Make",
                        [validators.InputRequired(), validators.Length(min=3, max=15)], 
                        render_kw=style)
    model = StringField("Model",
                        [validators.InputRequired()], render_kw=style)
    mileage = FloatField("Mileage", 
                        [validators.InputRequired()], render_kw=style)
    color = StringField("Color",
                        [validators.InputRequired()], render_kw=style)
    vin = StringField("VIN",
                        [validators.InputRequired(), validators.Length(min=11, max=17)],
                        render_kw=style)
    condition = SelectField("Condition",
                            choices=[('excellent', 'Excellent'), ('good', 'Good'), ('fair', 'Fair'), ('bad', 'Bad'), ('verybad', 'Very Bad')],
                            render_kw=style)
    cost = FloatField("Cost",
                        [validators.InputRequired()], render_kw=style)
    price = FloatField("Price",
                        [validators.InputRequired()], render_kw=style)
    description = TextField("Description (Optional)",
                        [validators.Optional()], render_kw=style)
    pic1 = StringField("Picture 1 URL:",
                        [validators.InputRequired()], render_kw=style)
    pic2 = StringField("Picture 2 URL (Optional)",
                        [validators.Optional()], render_kw=style)
    pic3 = StringField("Picture 3 URL (Optional)",
                        [validators.Optional()], render_kw=style)
    sold = BooleanField("Sold?", render_kw=style, false_values=('False', 'false', ''))
    sold_by = IntegerField("Sold By (ID number)",
                        [validators.Optional()], render_kw=style)
    sales_price = FloatField("Sales Price",
                        [validators.Optional()], render_kw=style)