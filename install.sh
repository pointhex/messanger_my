#!/bin/bash

rm /usr/share/bash-completion/completions/vk
rm /usr/bin/vk_my_auth.py
rm /usr/bin/vk

mkdir /usr/vk

cp ./complete.sh /usr/share/bash-completion/completions/vk
cp ./vk_module.py /usr/bin/vk
cp ./vk_my_auth.py /usr/bin/vk_my_auth.py
cp ./users /usr/vk/users
cp ./token /usr/vk/token
