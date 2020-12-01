from flask import json
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# migrate = Migrate(app, db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the database connection
DB = SQLAlchemy(app)

# initialize database migration management
MIGRATE = Migrate(app, DB)

from app.main.model.user import *


@app.route('/users')
def view_registered_guests():
    guests = User.query.all()
    response = app.response_class(response=json.dumps(guests),
                                  status=200,
                                  mimetype='application/json')
    return response


@app.route('/register', methods=['GET'])
def view_registration_form():
    return render_template('guest_registration.html')


if __name__ == '__main__':
    app.run(debug=True)
