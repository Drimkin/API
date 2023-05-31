from pprint import pprint
import requests


url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url)
hero_json = response.json()

hero_dict = {}
for hero in hero_json:
    if hero["name"] in ['Hulk', 'Captain America', 'Thanos']:
        hero_dict[hero['name']] = hero['powerstats']['intelligence']
result = sorted(hero_dict.items(), key=lambda x: int(x[1]), reverse=True)

pprint(f'Cамый умный супергерой - {result[0][0]}')

