import vk
import json
import time
import array
import select
import sys
import curses
from vk_my_auth import get_access_token
from vk_my_auth import auth

client_id = 5821652

session = vk.AuthSession(access_token = get_access_token())
vkapi = vk.API(session)

def searchForUser(user_list, ID):
    for user in user_list:
        user_obj = vkapi.users.get(user_ids = user)
        print(user_obj[0]['first_name'])
        time.sleep(0.4)
        if type(user) is int:
            continue

title_array = [];

def searchTitle(title_array, new_title):
    for title in title_array:
        if title == new_title:
            return False
    title_array.append(new_title)
    return True

myscreen = curses.initscr()
title = "ss"
while True: 
    myscreen.border(0) 
    myscreen.refresh() 
    curses.noecho()
    myscreen.addstr(title.decode("ascii") + "\n")
    print myscreen.getch()
    #myscreen.clear()
    curses.endwin()
    #print sys.stdin.read(1)
    #sys.stdout.flush()
    time.sleep(0.3);
    message_list = vkapi.messages.get(time_offset = 0, count = 200)
    for message in message_list:
        if not type(message) is int:
            if message['read_state'] != 1:
                #print(message)
                if  message['title'] == ' ... ':
                    time.sleep(0.3);
                    message_user = vkapi.users.get(user_ids = message['uid'])
                    title = message_user[0]['first_name'] + ' ' + message_user[0]['last_name'] 
                else:
                    title = message['title']

                if searchTitle(title_array, title):
                    print title
#                print message['title'].rjust(25), message_user[0]['first_name'].rjust(10), message_user[0]['last_name'].rjust(10)
#                print(message['body'])

#user_list = vkapi.friends.get(user_ids=client_id)
#searchForUser(user_list, "dsds")
