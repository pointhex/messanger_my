#!/bin/bash
_my_command() { #объявляем функцию, которую будем привязывать к анализу
	COMPREPLY=() #пока что мы не знаем, что предложить пользователю, поэтому создадим пустой список.
	cur="${COMP_WORDS[COMP_CWORD]}" #получаем текущий вводимый аргумент
	subcommands_1="get send clear update"
	subcommands_2=$(cat /home/artem/my_proj/messanger/users) #массив подкоманд первого уровня - см. синтаксическое дерево в начале поста.
	if [[ ${COMP_CWORD} == 1 ]] ; then #если вводится первый аргумент, то попробуем его дополнить
		COMPREPLY=( $(compgen -W "${subcommands_1}" -- ${cur}) ) #some magic
		return 0 #COMPREPLY заполнен, можно выходить
	fi
	if [ ${COMP_WORDS[1]} == 'send' ] || [ ${COMP_WORDS[1]} == 'clear' ] ; then
		if [[ ${COMP_CWORD} == 2 ]] ; then #если вводится первый аргумент, то попробуем его дополнить
			COMPREPLY=( $(compgen -W "${subcommands_2}" -- ${cur}) ) #some magic
			return 0 #COMPREPLY заполнен, можно выходить
		fi
	fi
}
complete -F _my_command vk_module.py

