
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired


class CalculatorForm(FlaskForm):
    num1 = IntegerField('Enter First Number', validators=[DataRequired()])
    num2 = IntegerField('Enter Second Number', validators=[DataRequired()])
    operator = SelectField('Operator',
                           choices=[('Multiply', 'Multiply: x'), ('Add', 'Add: +'), ('Divide',
                                                                                     'Divide: /'), ('Subtract', 'Subtract: -'), ('Reminder', 'Reminder: %')]
                           )
    submit = SubmitField('calculate')
