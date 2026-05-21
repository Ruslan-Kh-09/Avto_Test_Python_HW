import pytest
from sqlalchemy import create_engine, text, inspect

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"

db = create_engine(db_connection_string)

def test_db_connection():
    # 1. Создаем движок подключения
    db = create_engine(db_connection_string)

    # 2. Используем современный инспектор для получения имен таблиц
    inspector = inspect(db)
    names = inspector.get_table_names()

    # 3. Твоя проверка (assert) — проверяем, что таблица 'company' есть в списке
    assert "company" in names


def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company WHERE id = :company_id")
    result = connection.execute(sql_statement, {"company_id": 1})
    rows = result.mappings().all()

    assert len(rows) == 1
    assert rows[0]["name"] == "QA Студия 'ТестировщикЪ'"

    connection.close()