from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    # user = api.model('user',
    #                  {'id': fields.Integer(readonly=True, description='user id'),
    #                   'first_name': fields.String(required=True, description='user first name'),
    #                   'job_title': fields.String(required=True, description='user job title'),
    #                   'communication': {}
    #                   })
    #
    # user['communication']['email'] = fields.String(required=True, description='user email address')
    # user['communication']['mobile'] = fields.String(required=True, description='user mobile phone number')

    user = api.model('user', {
        'id': fields.Integer(readonly=True, description='user id'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'job_title': fields.String(required=True, description='user job title'),
        'communication': fields.Nested(api.model('userCommunicationData', {
            'email': fields.String(required=True, description='user email address'),
            'mobile': fields.String(required=True, description='user mobile phone number'),
        }))
    })