from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

auth = Blueprint('auth', __name__,)

from . import routes