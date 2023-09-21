from typing import Callable
from functools import wraps
import psycopg2


def decorator(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)

    return wrapper


class DataBase:
    def __init__(self, host, port, database, user, password):
        self._connect = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )
        self._cursor = self._connect.cursor()

    @decorator
    def add_user(self, user_id: int, language: str = 'en') -> None:
        print(user_id)
        with self._connect:
            self._cursor.execute(f"INSERT INTO users(id, language) VALUES({user_id}, '{language}')")
        self._connect.commit()
        print('success')

    @decorator
    def get_language(self, user_id: int):
        with self._connect:
            self._cursor.execute(f"SELECT language FROM users WHERE id={user_id}")
            return self._cursor.fetchone()

    @decorator
    def update_user_data(self, user_id: int, language: str) -> None:
        with self._connect:
            self._cursor.execute(f"UPDATE users SET language='{language}' WHERE id={user_id}")
        self._connect.commit()



