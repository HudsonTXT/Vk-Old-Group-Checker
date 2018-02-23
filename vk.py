import requests as r
from datetime import datetime
from time import sleep

# https://oauth.vk.com/authorize?client_id=6383443&display=mobile&response_type=token&scope=262144
token = ''  # Enter your token!

groups = r.get('https://api.vk.com/method/groups.get?user_id=41540621&access_token={}'.format(token)).json()

for i in range(1, len(groups['response'])):
    group = groups['response'][i] * -1
    posts = r.get('https://api.vk.com/method/wall.get?owner_id={}&offset=0&access_token={}'.format(group, token)).json()
    try:
        last_post = datetime.fromtimestamp(posts['response'][2]['date']).strftime('%Y')
        if (int(last_post) < 2018):
            print('Последнее сообщение от {}, группа: https://vk.com/club{}'.format(last_post, (group * -1)))

    except:
        continue
    if (round(i / len(groups['response']) * 100)) % 5 == 0:
        print('Загрузка... {}%'.format(round(i / len(groups['response']) * 100)))
    if i % 8 == 0: # Limit per second
        sleep(1)
