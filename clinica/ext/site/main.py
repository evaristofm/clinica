from flask import Blueprint, render_template, redirect, url_for
from clinica.ext.db.models import User
from clinica.ext.db.forms import UserForm
from clinica.ext.db import db


bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("site/index.html")


@bp.route("/create_user", methods=["GET", "POST"])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("site.index"))

    return render_template("site/user.html", form=form)

@bp.route("/users")
def users():
    users = User.query.all()
    return render_template("site/users.html", users=users)