import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import login, password, chat_id, group_id
import random
import time

vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth()

vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)


def sender():
    for event in longpoll.listen():
        if event.from_chat and event.chat_id == chat_id:
            if event.message == '!random':
                print("RANDOM")
                s = []
                while len(s) == 0:
                    post_id = random.randint(0, 2000)
                    s = vk.wall.getById(posts=f'{group_id}_{post_id}')
                    if len(s) != 0:
                        if s[0]['post_type'] != 'post':
                            s = []
                print(vk.wall.getById(posts=f'{group_id}_{post_id}'))
                vk.messages.send(chat_id=chat_id, message='', random_id=random.randint(0, 10000), attachment=f'wall{group_id}_{post_id}')
            elif event.message == '!info':
                print('INFO')
                vk.messages.send(chat_id=chat_id, random_id=random.randint(0, 10000), message='Бот для отправки рандомных постов v1.0')



while True:
    try:
        print('START')
        sender()
    except Exception:
        print('REBOOT')
        time.sleep(5)
        continue
