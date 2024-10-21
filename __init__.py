import  telebot
import requests
import json
import sqlite3
from amocrm.v2 import (tokens,Lead as _Lead,custom_field,Contact)
import datetime
import time

conn = sqlite3.connect('clients.db')  # Создаем базу данных clients.db
cursor = conn.cursor()
# Создаем таблицу для хранения данных клиентов
'''cursor.execute('''
        #CREATE TABLE info (
       #id INTEGER PRIMARY KEY ,
       #phone_number TEXT UNIQUE,
        #full_name TEXT
    #)
''')'''

#через id поля номер надо делать(+ доки)
class Lead(_Lead):
    test_text_field = custom_field.TextCustomField("test_text_field")
    delivery_type = custom_field.SelectCustomField("Способ доставки")
    address = custom_field.TextCustomField("Адрес")


bot=telebot.TeleBot("6802585445:AAGGmY8R5Af8RmMMIo5gm9F3XETfslb84sA")
# Настройки amoCRM
amo_client_id = "4421f483-c9e9-4608-94ef-a80a18772a14"
amo_client_secret = "HlpgFGOyzAKBJMXoTcFl6NwNB4JfetXQu18yCxsA8AwuscbhB1BanZAjvwG6tCdo"
amo_account_id = "11633530"  # ID аккаунта amoCRM
amo_api_url = f"https://{amo_account_id}.amocrm.ru/api/v4"
tokens.default_token_manager(
        client_id="4421f483-c9e9-4608-94ef-a80a18772a14",
        client_secret="HlpgFGOyzAKBJMXoTcFl6NwNB4JfetXQu18yCxsA8AwuscbhB1BanZAjvwG6tCdo",
        subdomain="svse343",
        redirect_url="https://t.me/grgsdfgujgsjBot",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage

    )
#tokens.default_token_manager.init(code="def5020002f7a251a7f31d861fd2fc90acaf28c3521b802b521041ba51c689a9fa6d07fd75750dc7c02007efaa8cc911b7fdad0b3342140cb8576d62cacfee0a68639fc7ea5bf531e18753c91ec02d3f8fc083a065e9b49c34effaedd89cd3a9ee4a3e6d1aa35f493364fc037a9b005593ba10745b86b5298d67d640e2941a7b219bb5f2e2c2c880845781a793783173a531b7cdc7da2977c18e8e90d09cf1586b5a364f5cd0035e876e33adb8d6496b27c85b9360fa46428d1655bc970c629e5f5449d05ffe37af3e97d123bdc18c3274b50f85c76f19fab4b38f3b8638182f20e81cb57f1827aedf2bd8bddf05371cc724c42810696a7150b93aa62d6b3d1761d30ec1ddbdb3f49d0695c8a538fc37e810d986b28472715396e3d842d49d4c4472ab8159c9562bf5f6e09221303ec688341339dfee916422c5efa3e19d8f312af05f0c5ee5e89979cb8eb7f18b44f5796ce4aa343e8373e7839d6df24fc36da544af6d17b348277b1f953e9a7b635071d4996c76578a131e67163bd6840f3f02e3080524ee7238b9a2431ff350bddc76a125e6709a5ff157ddb5795a4f453402e2d713cfe7b898d2d46028df62de38992b0593244cc926669aa0"
                                       #"4fa61fdef341d01abdd3bbee194e49c995d11e14a2c252bf3ba8f80bef80dbae10c48c48b0b2e7663e4da91f3a353e53eced56",skip_error=False)
print(1,"constants have")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Отправьте мне номер телефона и ФИО в формате: +7XXXXXXXXXX Иван Иванов")
    print(2,"func start ")


@bot.message_handler(commands=['sendinfo'])
def send_info(message):
    cursor.execute("SELECT id, phone_number, full_name FROM info")
    results = cursor.fetchall()
    output_string = ""
    for row in results:
        output_string += f"ID: {row[0]}, Номер: {row[1]}, ФИО: {row[2]}\n"
    bot.send_message(message.chat.id, output_string)  # Отправляем сообщение ботом
    print(2,"func send_info compl")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    try:
        parts = message.text.split(" ", 1)
        if len(parts) == 2:  # Проверяем, что есть две части (номер и ФИО)
            phone_number, full_name = parts
            cursor.execute("INSERT INTO info (phone_number, full_name) VALUES (?, ?)", (phone_number, full_name))
            conn.commit()
            bot.send_message(message.chat.id, "Данные успешно сохранены!")
        else:
            bot.send_message(message.chat.id, "Неверный формат ввода. Пожалуйста, отправьте данные в формате: +7XXXXXXXXXX Иван Иванов")
    except sqlite3.IntegrityError:
        bot.send_message(message.chat.id, "Этот номер телефона уже зарегистрирован.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
        print(e)
    finally:
        print(3,"func handle_message compl")
        conn.close()


def getStatus():
    cursor.execute("SELECT MAX(full_name) FROM info")
    last_updated = cursor.fetchone()[0]
    last_updated = last_updated
    if last_updated:
        return True

@bot.message_handler(func=lambda message: True)
def create_amo_contact():
    """Создает контакт в amoCRM, используя данные из базы данных."""
    '''cursor.execute("SELECT MAX(id) FROM info")
    last_processed_rowid = cursor.fetchone()[0]
    last_processed_rowid = last_processed_rowid
    query='SELECT full_name,phone_number FROM info WHERE last_processed_rowid=?'''
    rows = cursor.execute("SELECT full_name, phone_number FROM info").fetchall()
    for row in rows:
        first_name, last_name = row
        try:
            contact = Contact.objects.create(first_name=first_name, last_name=last_name,phone_number='79099481904')
            contact.save()
            print(f"Контакт '{first_name} {last_name}' создан успешно.")
        except Exception as e:
            print(f"Ошибка при создании контакта '{first_name} {last_name}': {e}")
    conn.close()
    print(5,'func create_amo_contact compl')

@bot.message_handler(func=lambda message: True)
def sendReq():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    clients=cursor.fetchall()
    for phone_number, full_name in clients:
        try:
            contact_data = {
                "add": [
                    {
                        "name": full_name,
                        "phone": [{"value": phone_number, "type": "WORK"}]

                    }
                ]
            }
            headers = {
                "Authorization": f"Bearer {amo_client_id}",
                "Content-Type": "application/json"
            }
            response = requests.post(amo_api_url + "/api/v4/contacts", headers=headers, data=json.dumps(contact_data))
            response.raise_for_status()
            print(f"Контакт {full_name} ({phone_number}) успешно создан в amoCRM.")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при создании контакта {full_name} ({phone_number}): {e}")
        except Exception as e:
            print(f"Ошибка: {e}")
    print(4,"func sendReq compl")


def get_contact_data_from_db(db_path: str) -> dict:
    """Извлекает данные контакта из базы данных (пример с SQLite)."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, phone_number FROM info")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"name": row[0], "phone": row[1]}
    else:
        return None
    print(5,'func get_contact_data_from_db compl')



if __name__ == "__main__":
    while True:
        bot.polling(create_amo_contact())
        create_amo_contact()