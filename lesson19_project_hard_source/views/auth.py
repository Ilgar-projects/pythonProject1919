from flask import request
from flask_restx import Resource, Namespace

from implemented import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get('username')
        password = req_json.get('password')

        if not username and not password:
            return {'error': 'Нет данных'}, 400

        token = user_service.auth_user(username, password)

        if not token:
            return {"error": "Ошибка в логине или в пароле"}, 401
        return token, 201
    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token')
        if refresh_token is None:
            return {'error': 'Токен стух'}, 400

        tokens = user_service.check_refresh_token(refresh_token)
        return tokens, 201


