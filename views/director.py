from flask_restx import Resource, Namespace
from flask import request

from app.container import director_service
from app.dao.model.director import DirectorSchema

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorViews(Resource):
    def get(self):
        all_genres = director_service.get_all()
        return directors_schema.dump(all_genres), 200


@director_ns.route('/<int:uid>')
class DirectorViews(Resource):
    def get(self, uid: int):
        director = director_service.get_one(uid)
        return director_schema.dump(director), 200