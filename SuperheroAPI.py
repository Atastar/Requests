import requests


class Superhero:
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def response(self):
        response = requests.get(self.link)
        id = response.json()['results'][0]['id']
        return id


class Powerstats(Superhero):
    def response(self):
        response = requests.get(self.link)
        intel = response.json()['intelligence']
        return intel


max_stat = {}
"""Поиск id героев"""
hulk = Superhero('Hulk', 'https://superheroapi.com/api/2619421814940190/search/Hulk')
captain_america = Superhero('Captain America', 'https://superheroapi.com/api/2619421814940190/search/Captain America')
thanos = Superhero('Thanos', 'https://superheroapi.com/api/2619421814940190/search/Thanos')


"""Поиск показателя интеллекта"""
hulk_stat = Powerstats('Hulk', 'https://superheroapi.com/api/2619421814940190/332/powerstats')
captain_america_stat = Powerstats('Captain America', 'https://superheroapi.com/api/2619421814940190/149/powerstats')
thanos_stat = Powerstats('Thanos', 'https://superheroapi.com/api/2619421814940190/655/powerstats')

max_stat['Hulk'] = hulk_stat.response()
max_stat['Captain America'] = captain_america_stat.response()
max_stat['Thanos'] = thanos_stat.response()


print(f'Самый умный среди супергероев - {max(max_stat, key=max_stat.get)}')






