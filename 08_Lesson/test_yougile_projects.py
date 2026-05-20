import pytest
import uuid
from yougile_avto_api import YougileAvtoApi


@pytest.fixture
def api_client():
    token = "Мой токен надо вставить сюда"
    return YougileAvtoApi(token)


# 1. МЕТОД [POST] /api-v2/projects (Создание)
# Позитивный: Создание проекта с валидным именем
def test_create_project_positive(api_client):
    unique_title = f"Руслан Тест {uuid.uuid4()}"
    response = api_client.create_project(title=unique_title)

    assert response.status_code == 201, (
        f"Ожидали код 201, получили {response.status_code}"
    )
    # Проверяем, что в ответе нам вернулся ID созданного проекта
    assert "id" in response.json(), (
        "В ответе сервера отсутствует 'id' нового проекта"
    )


# Негативный: Создания проекта с пустым именем
def test_create_project_negative_empty_title(api_client):
    response = api_client.create_project(title="")

    assert response.status_code == 400, (
        f"Ожидали ошибку 400, но сервер вернул {response.status_code}"
    )


# 2. МЕТОД [GET] /api-v2/projects/{id} (Получение)
# Позитивный: Получение существующего проекта по его реальному ID

def test_get_project_positive(api_client):
    # Создаем проект, чтобы получить валидный ID
    unique_title = f"Для удаления {uuid.uuid4()}"
    create_res = api_client.create_project(title=unique_title)
    project_id = create_res.json()["id"]

    # Теперь запрашиваем этот проект по ID
    response = api_client.get_project(project_id)

    assert response.status_code == 200, (
        f"Ожидали код 200, получили {response.status_code}"
    )
    assert response.json()["title"] == unique_title


# Негативный: Попытка получить проект по несуществующему ID

def test_get_project_negative_invalid_id(api_client):
    fake_id = "несуществующий-id-12345"
    response = api_client.get_project(fake_id)

    # Сервер должен ответить, что ресурс не найден
    assert response.status_code == 404, (
        f"Ожидали ошибку 404, но сервер вернул {response.status_code}"
    )


# 3. МЕТОД [PUT] /api-v2/projects/{id} (Обновление)
# Позитивный: Успешное изменение названия существующего проекта

def test_update_project_positive(api_client):
    # 1. Создаем проект
    unique_title = f"Старое имя {uuid.uuid4()}"
    create_res = api_client.create_project(title=unique_title)
    project_id = create_res.json()["id"]

    # 2. Обновляем его имя
    new_title = f"Новое имя {uuid.uuid4()}"
    response = api_client.update_project(project_id, new_title)

    assert response.status_code == 200, (
        f"Ожидали код 200, получили {response.status_code}"
    )

    # 3. Проверяем через GET, что имя на бэкенде действительно изменилось
    get_res = api_client.get_project(project_id)
    assert get_res.json()["title"] == new_title


# Негативный: Попытка обновить проект, стерев его имя (передав пустую строку)
def test_update_project_negative_blank_name(api_client):
    # 1. Создаем проект
    create_res = api_client.create_project(
        title=f"Проект под перезапись {uuid.uuid4()}"
    )
    project_id = create_res.json()["id"]

    # 2. Пробуем обновить на пустое имя
    response = api_client.update_project(project_id, new_title="")

    assert response.status_code == 400, (
        f"Ожидали ошибку 400, но сервер вернул {response.status_code}"
    )
