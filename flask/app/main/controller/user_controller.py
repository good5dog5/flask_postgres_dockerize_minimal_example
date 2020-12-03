from flask import request
from flask_restplus import Resource
from app.main.service.user_service import get_all_users, \
    get_user, \
    update_user, \
    delete_user, \
    save_new_user

from app.main.util.dto import UserDto

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<int:user_id>')
@api.response(404, 'User not found')
@api.doc(params={'user_id': 'The User Id'})
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_with(_user, envelope='data')
    def get(self, user_id):
        """Retrive a registered users"""
        user = get_user(user_id)
        if not user:
            api.abort(404)
        else:
            return user

    @api.doc('delete user by id')
    def delete(self, user_id):
        return delete_user(user_id)

    @api.expect(_user, validate=True)
    @api.marshal_with(_user, envelope='data')
    def put(self, user_id):
        """Update a user"""
        data = request.json
        return update_user(user_id, data=data)

