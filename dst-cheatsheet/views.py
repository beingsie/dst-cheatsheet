from flask import Blueprint, render_template
import json

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/')
def index():
    # Load the JSON data
    with open('data/dst_commands.json', 'r') as json_file:
        data = json.load(json_file)

    return render_template('index.html', title='Don\'t Starve Commands', data=data)