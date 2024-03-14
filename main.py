from flask import Flask

from data import db_session
from data.users import User

db_session.global_init("db/mars_explore.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    # app.run()
    user = User(surname='Scott',
                name='Ridley',
                age=21,
                position='captain',
                speciality='research engineer',
                address='module_1',
                email='scott_chief@mars.org')
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User(surname='Scott',
                name='Ridley',
                age=21,
                position='captain',
                speciality='research engineer',
                address='module_1',
                email='scott_chief2@mars.org')
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User(surname='Scott',
                name='Ridley',
                age=21,
                position='captain',
                speciality='research engineer',
                address='module_1',
                email='scott_chief3@mars.org')
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
