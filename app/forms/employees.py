#!/usr/bin/env python3
#-*- coding:utf8 -*-

from wtforms import (
    Form,
    StringField,
    validators
)

class EmployeeForm(Form):
    style = {"style": "width:100%"}
    first_name = StringField("First Name",
                            [validators.InputRequired()], render_kw=style)
    last_name = StringField("Last Name",
                            [validators.InputRequired()], render_kw=style)