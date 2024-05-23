import requests

api_key = 'fd0ba085-8dc3-48e4-b180-1818c97600be'
word = 'potato'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)

