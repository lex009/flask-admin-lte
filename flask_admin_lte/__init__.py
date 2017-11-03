__author__ = 'Alex Belyaev'
__email__ = 'lex@alexbelyaev.com'

from flask import Flask, Blueprint, url_for, request
from flask.helpers import get_root_path
import jinja2
import os


def lte(app: Flask):
    for blueprint in app.blueprints.values():
        blueprint.jinja_loader = jinja2.ChoiceLoader([
            jinja2.FileSystemLoader(os.path.join(get_root_path('flask_admin_lte'), 'templates/lte')),
            blueprint.jinja_loader,
        ])

    @app.template_filter('if_exists')
    def if_exists(filename):
        if os.path.isfile('{}{}'.format(app.root_path, filename)):
            return filename

    app.register_blueprint(Blueprint('admin_lte', __name__, static_folder='static', static_url_path='/static/lte'))
