import requests


class YougileAvtoApi:
    def __init__(self, token: str):
        # Базовый URL для запросов
        self.base_url = "https://ru.yougile.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str):
        """[POST] Создание проекта"""
        url = f"{self.base_url}/api-v2/projects"
        # Передаем обязательное поле title
        payload = {"title": title}
        return requests.post(url, json=payload, headers=self.headers)

    def get_project(self, project_id: str):
        """[GET] Получение проекта по ID"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id: str, new_title: str):
        """[PUT] Изменение проекта по ID"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {"title": new_title}
        return requests.put(url, json=payload, headers=self.headers)
