import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '+8801759072768',
  'message': 'Hello Arjun',
  'key': 'textbelt',
})
print(resp.json())