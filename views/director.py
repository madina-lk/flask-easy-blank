
from flask_restx import Resource, Namespace
from utils import *
from models import DirectorModel, DirectorSchema

director_schema = DirectorSchema(many=True)
director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):

    def get(self):
        """
        Получение всего списка сущностей,
        """
        return get_all_records(DirectorModel, director_schema)

    def post(self):
        """
         Создание новой записи
        """
        return insert_record(DirectorModel)


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):

    def get(self, director_id: int):
        """
        Получение конкретной сущности по идентификатору
        """
        try:
            return get_record_by_pk(DirectorModel, director_schema, director_id)
        except Exception as e:
            return "", 404

    def put(self, director_id: int):
        """
        Полное обновление (всех полей) сущности по ID
        """
        return update_record(DirectorModel, director_id)

    def delete(self, director_id: int):
        """
        Удаление сущности по ID
        """
        return delete_record(DirectorModel, director_id)