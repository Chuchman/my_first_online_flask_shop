from webFlaskmarket import app
from flask import render_template, redirect, url_for, request, flash, get_flashed_messages
from webFlaskmarket import forms
from webFlaskmarket.base_models import F_back, Item, User
from webFlaskmarket.forms import FeedbackForm, RegisterForm
from webFlaskmarket import db


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)
 

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_adress=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category="danger")

    return render_template("register.html", form=form)


@app.route("/feedback", methods=['GET', 'POST'])
def feedback_page():
    form = FeedbackForm(request.form)
    print(form.validate_on_submit())
    print(form.errors)
    if request.method == 'POST' and form.validate_on_submit():
        F_back_to_create = F_back(username=form.username.data,
                                email_adress=form.email_adress.data,
                                message=form.message.data)
        db.session.add(F_back_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a feedback: {err_msg}', category="danger")

    return render_template("feedback.html", form=form)
