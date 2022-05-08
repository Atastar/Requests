import requests


class YaUploader:
    url: str = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_link(self, file_path: str):
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.url, params=params, headers=self.get_headers())
        print(response.json())
        return response.json()

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_link(file_path).get('href')
        response = requests.put(href, data=open(file_path, 'rb'))
        if response.status_code == 201:
            print('файл загружен')



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
#

