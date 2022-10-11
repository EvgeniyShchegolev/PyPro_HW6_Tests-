import requests
import configparser


def _get_token_from_config(path_config: str) -> str:
    """Берёт из заданного файла ini токен и передаёт на выход"""
    config = configparser.ConfigParser()
    config.read(path_config)
    return config['TOKENS']['yadisk']


class YaLoader:
    """Класс для работы с api Яндекс.диска"""
    def __init__(self) -> None:
        """Инициализация атрибутов класса"""
        self.token = _get_token_from_config('config.ini')
        self.url = 'https://cloud-api.yandex.net/v1/disk'
        self.headers = {"Authorization": f"OAuth {self.token}",
                        "Content-Type": "application/json"}

    def create_folder(self, path: str) -> int:
        """Создаёт папку на Яндекс.диске"""
        response_put = requests.put(url=f'{self.url}/resources',
                                    params={"path": f'/{path}'},
                                    headers=self.headers)
        return response_put.status_code

    def get_status_folder(self, path: str) -> int:
        """Проверяет наличие папки на Яндекс.диске"""
        response_get = requests.get(url=f'{self.url}/resources',
                                    params={"path": f'{path}'},
                                    headers=self.headers)
        return response_get.status_code

    def delete_folder(self, path: str) -> int:
        """Удаляет папку на Яндекс.диске"""
        response_get = requests.delete(url=f'{self.url}/resources',
                                       params={"path": f'{path}'},
                                       headers=self.headers)
        return response_get.status_code


if __name__ == '__main__':
    yd = YaLoader()
    print(yd.create_folder('new'))
    print(yd.get_status_folder('new'))
    print(yd.delete_folder('new'))
