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
    # Генерируем случайный ID, чтобы тесты не пересекались по данным
    random_user_id = random.randint(500000, 999000)

    yield random_user_id  # Отдаем ID в тест

    # Чистим за собой созданного студента по его user_id
    delete_query = text("DELETE FROM student WHERE user_id = :user_id")
    db_connection.execute(delete_query, {"user_id": random_user_id})
    db_connection.commit()

# ТЕСТ 1: ДОБАВЛЕНИЕ (INSERT)


def test_add_student(db_connection, clean_student_id):
    test_id = clean_student_id

    insert_query = text(
        "INSERT INTO student (user_id, level, education_form, subject_id) "
        "VALUES (:user_id, :level, :education_form, :subject_id)"
    )
    db_connection.execute(
        insert_query,
        {
            "user_id": test_id,
            "level": "Junior",
            "education_form": "online",
            "subject_id": 1
        }
    )
    db_connection.commit()

    select_query = text("SELECT * FROM student WHERE user_id = :user_id")
    result = db_connection.execute(
        select_query, {"user_id": test_id}
    ).fetchone()

    assert result is not None, f"Студент с ID {test_id} не найден в БД"
    assert result.level == "Junior"

# ТЕСТ 2: ИЗМЕНЕНИЕ (UPDATE)


def test_update_student(db_connection, clean_student_id):
    test_id = clean_student_id

    insert_query = text(
        "INSERT INTO student (user_id, level, education_form, subject_id) "
        "VALUES (:user_id, :level, :education_form, :subject_id)"
    )
    db_connection.execute(
        insert_query,
        {
            "user_id": test_id,
            "level": "Junior",
            "education_form": "online",
            "subject_id": 1
        }
    )
    db_connection.commit()

    update_query = text(
        "UPDATE student SET level = :new_level WHERE user_id = :user_id"
    )
    db_connection.execute(
        update_query, {"new_level": "Middle", "user_id": test_id}
    )
    db_connection.commit()

    select_query = text("SELECT level FROM student WHERE user_id = :user_id")
    updated_level = db_connection.execute(
        select_query, {"user_id": test_id}
    ).scalar()

    assert updated_level == "Middle", "Уровень студента не обновился в БД"

# ТЕСТ 3: УДАЛЕНИЕ (DELETE)


def test_delete_student(db_connection, clean_student_id):
    test_id = clean_student_id

    insert_query = text(
        "INSERT INTO student (user_id, level, education_form, subject_id) "
        "VALUES (:user_id, :level, :education_form, :subject_id)"
    )
    db_connection.execute(
        insert_query,
        {
            "user_id": test_id,
            "level": "Senior",
            "education_form": "offline",
            "subject_id": 2
        }
    )
    db_connection.commit()

    delete_query = text("DELETE FROM student WHERE user_id = :user_id")
    db_connection.execute(delete_query, {"user_id": test_id})
    db_connection.commit()

    select_query = text("SELECT * FROM student WHERE user_id = :user_id")
    result = db_connection.execute(
        select_query, {"user_id": test_id}
    ).fetchone()

    assert result is None, "Студент не был удален из базы данных"
