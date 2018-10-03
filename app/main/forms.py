
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField


class CalculatorForm(FlaskForm):
    num1 = IntegerField('Enter First Number')
    num2 = IntegerField('Enter Second Number')
    operator = SelectField('Operator',
                           choices=[('Multiply', 'Multiply: x'), ('Add', 'Add: +'), ('Divide',
                                                                                     'Divide: /'), ('Subtract', 'Subtract: -'), ('Reminder', 'Reminder: %')]
                           )
    submit = SubmitField('calculate')
