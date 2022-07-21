from flask import json, request
from setup_db import db

from models import MovieModel, MovieSchema

movie_schema = MovieSchema(many=True)  # создание экземпляра схемы


def get_movie_by_director_id(director_id):
    """Получение фильмов с определенным режиссером"""
    movie = MovieModel.query.filter(MovieModel.director_id == director_id)
    res = movie_schema.dump(movie), 200
    return res


def get_movie_by_genre_id(genre_id):
    """Получение фильмов с определенным жанром"""
    movie = MovieModel.query.filter(MovieModel.genre_id == genre_id)
    res = movie_schema.dump(movie), 200
    return res


def get_movie_by_year(year):
    """Получение фильмов за год"""
    movie = MovieModel.query.filter(MovieModel.year == year)
    res = movie_schema.dump(movie), 200
    return res


def get_all_records(model, schema):
    """Получение всех записей"""
    all_records = db.session.query(model).paginate(page=1, per_page=5).items
    res = schema.dump(all_records), 200
    return res


def insert_record(model):
    """Добавление новой записи"""
    new_record = model(**json.loads(request.data))
    db.session.add(new_record)
    db.session.commit()

    return "Новая запись добавлена", 201


def get_record_by_pk(model, schema, pk):
    """Получение записи по определенному ид"""
    movie = db.session.query(model).filter(model.id == pk)
    res = schema.dump(movie)
    return res, 200


def update_record(model, pk):
    """Обновление записи по ид"""
    movie = json.loads(request.data)
    updates_record = db.session.query(model).filter(model.id == pk)
    updates_record.update(movie)
    db.session.commit()

    return "Запись обновлена"


def delete_record(model, pk):
    """Удаление записи по ид"""
    delete_mv = model.query.get(pk)
    db.session.delete(delete_mv)
    db.session.commit()

    return "Запись удалена"
