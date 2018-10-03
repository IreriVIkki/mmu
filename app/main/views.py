from flask import render_template, request, redirect, url_for, abort
from . import main
from .calc import Calc
from .forms import CalculatorForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = CalculatorForm()
    answer = 0.00
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        # using try except to catch errors where the input is not a number

        operator = form.operator.data
        print(operator)
        calc = Calc(num1, num2)
        if operator == 'Multiply':
            answer = calc.multiply()
        elif operator == 'Add':
            answer = calc.addition()
        elif operator == 'Divide':
            answer = calc.divide()
        elif operator == 'Subtract':
            answer = calc.subtraction()
        elif operator == 'Reminder':
            answer = calc.reminder()

    return render_template('index.html', form=form, answer=answer)
