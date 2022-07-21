from flask_restx import Resource, Namespace
from utils import *
from models import MovieModel, MovieSchema

movie_schema = MovieSchema(many=True)
movie_ns = Namespace("movies")


@movie_ns.route("/")
@movie_ns.param("director_id", "id Режиссера")
@movie_ns.param("genre_id", "id жанра")
@movie_ns.param("year", "год")
class MoviesView(Resource):
    def get(self):
        """
        Получение всего списка сущностей,
        списка по director_id,
        списка по genre_id
        """
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)

        if director_id:
            return get_movie_by_director_id(director_id)
        if genre_id:
            return get_movie_by_genre_id(genre_id)
        if year:
            return get_movie_by_year(year)

        return get_all_records(MovieModel, movie_schema)

    def post(self):
        """
        Создание новой записи
        """
        return insert_record(MovieModel)


@movie_ns.route("/<int:movie_id>")
class MovieView(Resource):
    def get(self, movie_id: int):
        """
        Получение конкретной сущности по идентификатору
        """
        try:
            return get_record_by_pk(MovieModel, movie_schema, movie_id)
            # return get_movie_by_id(movie_id)
        except Exception as e:
            return "", 404

    def put(self, movie_id: int):
        """
        Полное обновление (всех полей) сущности по ID
        """
        return update_record(MovieModel, movie_id)

    def delete(self, movie_id: int):
        """
        Удаление сущности по ID
        """
        return delete_record(MovieModel, movie_id)
