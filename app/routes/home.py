from flask import Blueprint, render_template, flash
from flask import request, redirect, url_for, session
from uuid import uuid4
# from App.routes.jwt_session import auth_require


home_bp = Blueprint('home', __name__, url_prefix="/")

@home_bp.get('/')
def index():
    return render_template("index.html")
