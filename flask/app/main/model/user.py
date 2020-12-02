from .. import db


class User(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    mobile = db.Column(db.String(40), nullable=False)
    job_title = db.Column(db.String(40), nullable=False)

    def __init__(self, first_name, last_name, email, mobile, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.job_title = job_title

    def __repr__(self):
        return "<User '{}'>".format(self.first_name + " " + self.last_name)
