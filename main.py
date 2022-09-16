from flask import Flask
from flask_restx import Api
from app.config import Config
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie
from setup_db import db
from views.director import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


# функция создания основного объекта app
def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx)
def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    # create_data()


def create_data(app, db):
    with app.app_context():
        m1 = Movie(title="Чикаго",
                   description="Рокси Харт мечтает о песнях и танцах и о том, как сравняться с самой Велмой Келли, примадонной водевиля. И Рокси действительно оказывается с Велмой в одном положении, когда несколько очень неправильных шагов приводят обеих на скамью подсудимых.",
                   trailer="https://www.youtube.com/watch?v=YxzS_LzWdG8", year=2002, rating=7.2, genre_id=2,
                   director_id=3)
        m2 = Movie(title="Бурлеск",
                   description="Али - молодая амбициозная девушка из маленького городка с чудесным голосом, совсем недавно потеряла своих родителей.",
                   trailer="https://www.youtube.com/watch?v=sgOhxneHkiE", year=2010, rating=6.4, genre_id=1,
                   director_id=2)
        m3 = Movie(title="Рокетмен",
                   description="История превращения застенчивого парня Реджинальда Дуайта, талантливого музыканта из маленького городка, в суперзвезду.",
                   trailer="https://www.youtube.com/watch?v=sgOhxghHkiE", year=2007, rating=8.4, genre_id=3,
                   director_id=1)

        g1 = Genre(name="Комедия")
        g2 = Genre(name="Драма")
        g3 = Genre(name="Фантастика")

        d1 = Director(name="Тейлор Шеридан")
        d2 = Director(name="Стив Энтин")
        d3 = Director(name="Пит Доктер")

        db.create_all()

        with db.session.begin():
            db.session.add_all([m1, m2, m3])
            db.session.add_all([g1, g2, g3])
            db.session.add_all([d1, d2, d3])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    register_extensions(app)
    create_data(app, db)
    app.run()
