# Здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# Сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace
from implemented import director_dao, director_schema

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_dao.get_all()
        return director_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_dao.create(req_json)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = director_dao.get_one(did)
        return director_schema.dump(director), 200

    def put(self, did):
        req_json = request.json
        req_json["id"] = did

        director_dao.update(req_json)

        return "", 204

    def patch(self, did):
        req_json = request.json
        req_json["id"] = did

        director_dao.update_partial(req_json)
        return "", 204

    def delete(self, did: int):
        director_dao.delete(did)
        return "", 204
