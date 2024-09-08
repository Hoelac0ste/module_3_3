
def send_email(message, recipient, sender = "university.help@gmail.com"):

    standard_sender = True # переменная для проверки флага стандартного отправителя
    messaging_yourself = False # переменная для проверки флага отправки письма самому себе
    adress_style_is_ok = True # переменная для проверки флага правильности почтового адреса
    
    if sender == "university.help@gmail.com":
        standard_sender = True # проверка на отправку письма со стандартного адреса
    else:
        standard_sender = False
    
    if recipient == sender:
        messaging_yourself = True # проверка на отправку письма себе
    
    if '@' in recipient:
        if recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'):
            adress_style_is_ok = True # проверка правильности адреса
            if sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
                adress_style_is_ok = True # проверка правильности адреса
            else:
                adress_style_is_ok = False
                
        else:
            adress_style_is_ok = False
    else:
        adress_style_is_ok = False

    if adress_style_is_ok == True and messaging_yourself == False and standard_sender == False:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    if adress_style_is_ok == True and messaging_yourself == False and standard_sender == True:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif adress_style_is_ok == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif messaging_yourself == True:
        print('Нельзя отправить письмо самому себе!')
   
    
send_email('Hello', "university.help@gmail.com", sender = 'rsity.help@gmail.con')