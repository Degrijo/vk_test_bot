import requests
import pprint
import bs4
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk import Session, API
from random import randint


TOKEN = '8de8005e3d701d2b1dc2ee870bff58227b314cf76d672ab7cf7b6945a245c7ea5179976d157b04bf8f334'
counter = 0


def write_msg(user_id, message):
    global counter
    vk.method('messages.send', {'user_id': user_id, 'random_id': counter, 'message': message})
    counter += 1


def get_friend_list(user_id):
    session = Session(access_token="43cceeb8506f5e63619914ac18aee451be826d70ea833e646fcf22440730aeb27ac8a865b0bfde7a0e776")
    vk_api = API(session, v="5.103")
    user = vk_api.users.get(user_id=280945440)
    # vk_session = VkApi("+375293164565", "1ron13branch37")
    # vk_session.auth()
    # api = vk_session.get_api()
    # print(api)
    print(user)
    return []


vk = VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            text = event.text.lower()
            if text == "ближайшее др":
                write_msg(event.user_id, "ближайшее др")
            elif text == "друзья":
                write_msg(event.user_id, ", ".join(get_friend_list(event.user_id)))
            else:
                write_msg(event.user_id, "я тут")
