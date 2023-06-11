from config import client, FROM_PHONE


def send_sms(user_phone, code):
    try:
        message = client.messages.create(
                              from_=FROM_PHONE,
                              body=f"Код от банковской системы  {code}",
                              to=user_phone
                              )
        return f'Код был успешно отправлен на номер {user_phone}!!!'
    except Exception as ex:
        if 'is not a valid phone number' in str(ex):
            return "Вы ввели не корректный номер телефона"
        return ex
