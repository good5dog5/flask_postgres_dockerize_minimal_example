from app.main import db
from app.main.model.user import User
import json


def get_all_users():
    return User.query.all()


def get_user(id):
    user = User.query.filter_by(id=id).first()
    return user


def save_new_user(data):
    user = User.query.filter_by(email=data['communication']['email']).first()
    if not user:
        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            job_title=data['job_title'],
            mobile=data['communication']['mobile'],
            email=data['communication']['email'],
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'new user created',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def update_user(_id, data):
    user = User.query.filter_by(id=_id).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User id not exists',
        }
        return response_object, 409
    else:
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.job_title = data['job_title']
        user.email = data['communication']['email']
        user.mobile = data['communication']['mobile']

        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'user data updated',
        }
        return response_object, 200


def delete_user(_id):
    user = User.query.filter_by(id=_id).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User id not exists',
        }
        return response_object, 409
    else:
        db.session.delete(user)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'user {_id} is deleted'.format(_id=_id),
        }
        return response_object, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()
