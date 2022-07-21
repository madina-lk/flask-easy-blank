
from flask_restx import Resource, Namespace
from models import GenreModel, GenreSchema
from utils import *

genre_schema = GenreSchema(many=True)           # создание экземпляра схемы

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        """
        Получение всего списка сущностей,
        """
        return get_all_records(GenreModel, genre_schema)

    def post(self):
        """
         Создание новой записи
        """
        return insert_record(GenreModel)


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        try:
            return get_record_by_pk(GenreModel, genre_schema, genre_id)
        except Exception as e:
            return "", 404

    def put(self, genre_id: int):
        """
        Полное обновление (всех полей) сущности по ID
        """
        return update_record(GenreModel, genre_id)

    def delete(self, genre_id: int):
        """
        Удаление сущности по ID
        """
        return delete_record(GenreModel, genre_id)

