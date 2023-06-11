from time import sleep
from validations import valid_number, generate_code
from send_sms import send_sms

users = {
      'Asik': {
            'phone': '+77777777777',
            'name': 'Asik',
            'cash': 0,
            'password': '12345'
            },
      'Asik2004' : {
            'phone' : '+77076003485',
            'name' : 'Asik2004',
            'cash' : 1,
            'password' : '12345'
            },
      }

user = None

while True:
      if user:
            print(f'      Добро пожаловать {user}!!!')
      a = input("""
      Введите 1 чтобы Зарегистрироваться 
      Введите 2 что бы Авторизоваться 
      Введите 4 список пользователей 
      Введите 5 для совершения перевода 
      Введите 6 Выход из аккаунта
      Введите 7 Информация
      Введите 3 для выхода
      >>>   """)

      if a == '1':
            login = input('Введите логин: ')
            name = input('Введите name: ')
            phone = input('Введите phone: \n >> +7 ')
            verifi = valid_number(phone)
            while not verifi['bool']:
                print(verifi['status'], verifi['description'])
                phone = input('Введите еще раз phone: \n >> +7 ')
                verifi = valid_number(phone)
            else:
                print('номер правильный! мы отправили вам код на номер')
            phone = "+7"+phone
            code = generate_code()
            send_sms(phone, code)
            confirm_numder = input('Введите  код из sms или 1 для переотправки: \n >>  ')
            if confirm_numder == '1':
                send_sms(phone, code)
            while code != confirm_numder:
                print('Код не совпадает!!!')
                confirm_numder = input('Введите  код из sms или 1 для переотправки: \n >>  ')
                if confirm_numder == '1':
                    send_sms(phone, code)

            password = input('Введите пароль длиннее 8 символов : ')
            password1 = input('Введите пароль1: ')
            while password != password1 or len(password) < 8:
                  password = input('Введите пароль длиннее 8 символов: ')
                  password1 = input('Введите пароль1: ')
            else:
                  users.update({
                        login :{
                              'phone': phone,
                              'name': name,
                              'cash': 0,
                              'password': password 
                              }
                        })
                  print('Регистрация успешна <<<')
                  user = login
      
      elif a == '2':
            print('логика Авторизации !!!')
            if user is None:
                  login = input('Введите логин: ')
                  password = input('Введите пароль : ')
                  if login in users:
                        if  password == users[login]['password']:
                              print('Вы успешно Авторизовались <<<')
                              user = login
                        else:
                              print('Неправильный пароль <<<')
                  else:
                        print('Такой пользователь не существует <<<')
            else:
                  print('Вы уже Авторизованы <<<')
      elif a == '3':
            print('Вы вышли !!!')
            break 
      elif a == '4':
            print('логика Users !!!')
            print(users)

      elif a == '5':
            print('логика Перевода !!!')
            if user is not None:
                  login_recipient = input('Введите логин получателя: ')
                  summ= int(input('Введите сумму : ')) 
                  if login_recipient in users:
                        if summ < users[user]['cash']:
                              users[user]['cash'] -= summ
                              users[login_recipient]['cash'] += summ
                              print('Отправка произведена успешно !!!')
                        else:
                              print('недостаточно средств <<<')
                  else:
                        print('Не удалось найти получателя <<<') 
            else:
                  print('Для совершения перевода Авторизуйтесь <<<')
      elif a == '6':
            print('логика выхода из аккаунта !!!')
            user = None 
      elif a == '7':
            print('Логика личной информации !!!')
            if user is not None:
                  print(
                  f'''
      Ваши данныe
      Имя = {users[user]['name']}
      Логин = {user}
      номер = {users[user]['phone']}
      Счет = {users[user]['cash']}
                  '''
                  )
            else:
                  print('Для получения информации Авторизуйтесь !!!')
      
      else:       
            print('такой команды нет попробуйте еще раз ')


