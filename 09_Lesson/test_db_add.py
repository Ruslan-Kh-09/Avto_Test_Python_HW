from sqlalchemy import text


def test_add_student(db_connection, clean_student_id):
    """Тест на добавление (INSERT) новой записи в таблицу student."""
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
