#!/usr/bin/python3.5
import vk
import json
import time
import array
import sys
import vk_my_auth

home_dir = '/usr/vk'

def get_access_token():
    regs = vk.AuthSession(vk_my_auth.m_client_id, vk_my_auth.m_email, vk_my_auth.m_password, scope = 'messages')
    return regs.get_access_token()

def login():
    try:
            f = open(home_dir+'token', 'r')
    except IOError as e:
            f = open(home_dir+'token', 'w')
            f.close()
            f = open(home_dir+'token', 'r')
    if f.read == '':
        session = vk.AuthSession(access_token = f.read())
        f.close();
    else:
        f.close()
        f = open(home_dir+'token', 'w')
        token = get_access_token();
        f.write(token)
        session = vk.AuthSession(access_token = token)
    return vk.API(session, v='5.68')

def update_user_list(user_list):
    f = open(home_dir+'users', 'w')
    for user in user_list["items"]:
        user_obj = vkapi.users.get(user_ids = user)
        print(user_obj[0]['first_name'] + '_' + user_obj[0]['last_name'] + ' ')
        f.write(user_obj[0]['first_name'] + '_' + user_obj[0]['last_name'] + '_' + \
                str(user_obj[0]['id']) + ' ')
        f.write(user_obj[0]['last_name'] + '_' + user_obj[0]['first_name'] + '_' + \
                str(user_obj[0]['id']) + ' ')
        time.sleep(0.3)
    f.close()

def find_user_name(message):
    f = open(home_dir+'users', 'r')
    new_id = ''
    if message['title'] == '':
        user_obj = vkapi.users.get(user_ids = message['user_id'])
        new_id = user_obj[0]['id']
    else :
        new_id = message['chat_id']

    for user_name in f.read().split(' '):
        if user_name != '':
            if user_name.split('_')[2] == str(new_id):
                return
    f.close()
    if message['title'] != '':
        f = open(home_dir+'users', 'a')
        f.write( 'Group_' + message['title'].replace(' ', '').replace('_', '') \
                + '_' + str(2000000000 + message['chat_id']) + ' ')
        f.write( message['title'].replace(' ', '').replace('_', '') + '_Group' \
                + '_' + str(2000000000 + message['chat_id']) + ' ')

        f.close()
        return

    f = open(home_dir+'users', 'a')
    f.write(user_obj[0]['first_name'] + '_' + user_obj[0]['last_name'] + '_' + \
                str(user_obj[0]['id']) + ' ')
    f.write(user_obj[0]['last_name'] + '_' + user_obj[0]['first_name'] + '_' + \
                str(user_obj[0]['id']) + ' ')
    f.close()
    print("User was added")

def get_messages():
    time.sleep(0.3);
    message_list = vkapi.messages.get(time_offset = 0, count = 200)
    for message in message_list["items"]:
        if not type(message) is int:
            if message['read_state'] != 1:
                time.sleep(0.3);
                message_user = vkapi.users.get(user_ids = message['user_id'])
                find_user_name(message)
                title = message['title'].ljust(20) +  '|' +\
                    message_user[0]['first_name'].ljust(10) + ' ' +\
                    message_user[0]['last_name'].ljust(15)
                print(time.strftime("%D %H:%M", time.localtime(int(message['date']))), title, '|', message['body'])

vkapi = login()

if (len(sys.argv) > 1):
    if (sys.argv[1] == 'get'):
        get_messages()

    if (sys.argv[1] == 'init'):
        user_list = vkapi.friends.get(user_ids=vk_my_auth.m_client_id)
        update_user_list(user_list)

    if (sys.argv[1] == 'send'):
        vkapi.messages.send(peer_id=sys.argv[2].split('_')[2], message = sys.argv[3])
        vkapi.messages.markAsRead(peer_id=sys.argv[2].split('_')[2], answered=1)

    if (sys.argv[1] == 'clear'):
        vkapi.messages.markAsRead(peer_id=sys.argv[2].split('_')[2], answered=1)

    if (sys.argv[1] == 'change'):
        f = open(home_dir+'users', 'a')
        if (len (sys.argv[3].split('_')) == 1):
            f.write(sys.argv[3] + '__' + sys.argv[2].split('_')[2])
        elif (len(sys.argv[3].split('_')) == 2):
            f.write(sys.argv[3] + '_' + sys.argv[2].split('_')[2])
        else:
            print('Enter less _')

        f.close()
else :
    print('Enter a command!')
    print('update : Update friend list for hints')
    print('get    : Get list of messages')
    print('send  <friend name> <"ur message">: Send ur message')
    print('clear <friend name>: Make messages as read')

