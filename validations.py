from random import choice
#  +996 999191919

codes = ['707',
        '706',
        '747',
        '775',
        '776',
        '778',
        '701',
        '777',
        '708'
]


def valid_number(number):
    if number[:2] in codes and number.isdigit() and len(number) == 9:
        return {
            'status': 200,
            'description': 'success',
            'bool': True
           }
    if number[:2] not in codes:
        return {
            'status': 400,
            'description': 'не верный код оператора !!!',
            'bool': False
           }
    if  not number.isdigit():
        return {
            'status': 401,
            'description': 'номер телефона не может содержать буквы !!!',
            'bool': False
           }
    if len(number) > 8:
        return {
            'status': 402,
            'description': 'номер cлишком длинный !!!',
            'bool': False
           }
    if len(number) < 8:
        return {
            'status': 403,
            'description': 'номер cлишком короткий !!!',
            'bool': False
           }
    return {
            'status': 404,
            'description': 'неизвестная ошибка !!!',
            'bool': False
           }


def generate_code():
    code = ""
    for i in range(6):
        code += choice('25096')
    return code