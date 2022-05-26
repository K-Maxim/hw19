from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service


user_ns = Namespace('users')

@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        return UserSchema(many=True).dump(users)

    def post(self):
        data = request.json
        user = user_service.create(data)
        return UserSchema().dump(user), 200


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        return UserSchema().dump(user), 200

    def delete(self, uid):
        user_service.delete(uid)
        return '', 204
