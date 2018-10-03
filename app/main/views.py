from flask import render_template, request, redirect, url_for,abort
from . import main
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField

class Calc():
    def addition(num1, num2):
        return num1 + num2

    def subtraction(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2

    def reminder(num1, num2):
        return num1 % num2



class CalculatorForm(FlaskForm):
    num1 = IntegerField('Enter First Number')
    num2 = IntegerField('Enter Second Number')
    operator = SelectField('Operator',
        choices = [('Multiply', 'Multiply: x'), ('Add', 'Add: +'), ('Divide', 'Divide: /'), ('Subtract', 'Subtract: -'), ('Reminder', 'Reminder: %')]
    )
    submit = SubmitField('calculate')

@main.route('/', methods=['GET','POST'])
def index():
    form = CalculatorForm()
    answer = 0.00
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        operator = form.operator.data
        print(operator)

        if operator == 'Multiply':
            answer = Calc.multiply(num1, num2)
        elif operator == 'Add':
            answer = Calc.addition(num1, num2)
        elif operator == 'Divide':
            answer = Calc.divide(num1, num2)
        elif operator == 'Subtract':
            answer = Calc.subtraction(num1, num2)
        elif operator == 'Reminder':
            answer = Calc.reminder(num1, num2)    
    
    return render_template('index.html', form=form, answer=answer)

