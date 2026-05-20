from sqlalchemy import text


def test_delete_student(db_connection, clean_student_id):
    """Тест на удаление (DELETE) записи внутри сценария."""
    test_id = clean_student_id

    # 1. Добавляем студента
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

    # 2. Удаляем его
    delete_query = text("DELETE FROM student WHERE user_id = :user_id")
    db_connection.execute(delete_query, {"user_id": test_id})
    db_connection.commit()

    # 3. Проверяем, что запись стёрта
    select_query = text("SELECT * FROM student WHERE user_id = :user_id")
    result = db_connection.execute(
        select_query, {"user_id": test_id}
    ).fetchone()

    assert result is None, "Студент не был удален из базы данных"
