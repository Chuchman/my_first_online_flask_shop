from webFlaskmarket import app
from flask import render_template
from webFlaskmarket.base_models import Item
from webFlaskmarket.forms import RegisterForm


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route("/register")
def register_page():
    form = RegisterForm()
    return render_template("register.html", form=form)
