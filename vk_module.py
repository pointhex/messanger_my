import vk
import json
import time
#import vk_my_auth 
from vk_my_auth import get_access_token
from vk_my_auth import auth

client_id = 5821652

session = vk.AuthSession(access_token = get_access_token())
vkapi = vk.API(session)
#vkapi.wall.post(message="Hello, world")p

def searchForUser(user_list, ID):
    for user in user_list:
        user_obj = vkapi.users.get(user_ids = user)
        print(user_obj[0]['first_name'])
        time.sleep(0.3)
        if type(user) is int:
            continue

user_list = vkapi.friends.get(user_ids=client_id)
while True:
    time.sleep(1);
    message_list = vkapi.messages.get(time_offset = 0)
    for message in message_list:
        if not type(message) is int:
            if message['read_state'] != 1:
                print(message['body'])
#searchForUser(user_list, "dsds")
