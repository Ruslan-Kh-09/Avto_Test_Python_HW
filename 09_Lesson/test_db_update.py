from sqlalchemy import text


def test_update_student(db_connection, clean_student_id):
    """Тест на изменение (UPDATE) существующей записи."""
    test_id = clean_student_id

    # 1. Создаем запись для теста
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

    # 2. Обновляем уровень на Middle
    update_query = text(
        "UPDATE student SET level = :new_level WHERE user_id = :user_id"
    )
    db_connection.execute(
        update_query, {"new_level": "Middle", "user_id": test_id}
    )
    db_connection.commit()

    # 3. Проверяем результат
    select_query = text("SELECT level FROM student WHERE user_id = :user_id")
    updated_level = db_connection.execute(
        select_query, {"user_id": test_id}
    ).scalar()

    assert updated_level == "Middle", "Уровень студента не обновился в БД"
