from datetime import datetime

date_release = str(datetime.now().strftime('%d/%m/%y'))
print("Testing project for Git \n" + ' by Rodionov Sergei \n' + '\t' + date_release)

import json

with open('account.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print('Имя пользователя:' + '\t' + data['user_name'] + '\n'
      'Пароль:' + '\t' + data['password'])

print('Теперь грузим все на гитхаб')

print('Поробуем потестить Pull')
