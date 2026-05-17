import random
import pytest
from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:123@localhost:5432/QA"


@pytest.fixture(scope="function")
def db_connection():

    engine = create_engine(DB_URL)
    connection = engine.connect()

    yield connection

    connection.close()


@pytest.fixture
def clean_student_id(db_connection):

    random_user_id = random.randint(500000, 999000)

    yield random_user_id

    delete_query = text("DELETE FROM student WHERE user_id = :user_id")
    db_connection.execute(delete_query, {"user_id": random_user_id})
    db_connection.commit()
