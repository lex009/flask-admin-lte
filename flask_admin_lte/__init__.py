__author__ = 'Alex Belyaev'
__email__ = 'lex@alexbelyaev.com'

from flask import Flask, Blueprint
from flask.helpers import get_root_path
import jinja2
import os

def lte(app: Flask):
    for blueprint in app.blueprints.values():
        original = blueprint.jinja_loader
        choices = [jinja2.FileSystemLoader(os.path.join(get_root_path("flask_admin_lte"), "templates/lte"))]
        # `original` loader may be None, which is unacceptable.
        if original:
            choices.append(blueprint.jinja_loader)
        blueprint.jinja_loader = jinja2.ChoiceLoader(choices)

    @app.template_filter('vars')
    def _vars(obj):
        return vars(obj)

    app.register_blueprint(Blueprint('admin_lte', __name__, static_folder='static', static_url_path='/static/lte'))
