import  telebot
import requests
import json
import sqlite3
import webbrowser

conn = sqlite3.connect('clients.db')  # Создаем базу данных clients.db
cursor = conn.cursor()
# Создаем таблицу для хранения данных клиентов
#cursor.execute('''
#        CREATE TABLE clients (
#       id INTEGER PRIMARY KEY ,
#       phone_number TEXT UNIQUE,
#        full_name TEXT
    #)
#''')


bot=telebot.TeleBot("6802585445:AAGGmY8R5Af8RmMMIo5gm9F3XETfslb84sA")
amo_api_url = "https://YOUR_AMO_SUBDOMAIN.amocrm.ru/api/v4"
amo_client_id = "32001522"  # ID аккаунта
amo_redirect_uri = "http://localhost:127.0.0.1:8000/redirect"
amo_client_secret = " 32001522" # access_token
amo_api_url = f"https://{amo_client_id}.amocrm.ru/leads/pipeline/?skip_filter=Y&typing=y"



print("1")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Отправьте мне номер телефона и ФИО в формате: +7XXXXXXXXXX Иван Иванов")
print("2")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    try:
        phone_number, full_name = message.text.split(" ", 1) # Разделяем сообщение на номер телефона и ФИО
        cursor.execute("INSERT INTO clients (phone_number, full_name) VALUES (?, ?)", (phone_number, full_name))
        conn.commit()
        bot.send_message(message.chat.id, "Данные успешно сохранены!")
    except ValueError:
        bot.send_message(message.chat.id, "Неверный формат ввода. Пожалуйста, отправьте данные в формате: +7XXXXXXXXXX Иван Иванов")
    except sqlite3.IntegrityError:
        bot.send_message(message.chat.id, "Этот номер телефона уже зарегистрирован.")
        bot.send_message(message.chat.id, "Перезапустите бота.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
    conn.close()
print("3")
a=True
def chesk():
    if a:
        return True

@bot.message_handler(commands=['sendinfo'])
def send_info(message):
    # Получаем курсор из глобальной переменной.  Это не лучший подход, но для простоты оставим так.
    cursor.execute("SELECT id, phone_number, full_name FROM clients")
    results = cursor.fetchall()
    output_string = ""
    for row in results:
        output_string += f"ID: {row[0]}, Номер: {row[1]}, ФИО: {row[2]}\n"
    bot.send_message(message.chat.id, output_string)  # Отправляем сообщение ботом
print("3.5")
if chesk():
    @bot.message_handler(commands=['send'])
    def send(message):
        user_data = {
            'name': cursor.execute("SELECT full_name FROM clients"),
            'phone': cursor.execute("SELECT phone_number FROM clients")
        }

        #https: // svse343.amocrm.ru / dashboard /?sel = all & period = week

        #response = requests.get(amo_api_url, headers={"Authorization": f"Bearer {YOUR_API_TOKEN}")
    print("quest is sended")

def create_amo_contact(user_data: object) -> object:
    required_fields = ['name', 'phone']
    missing_fields = [field for field in required_fields if field not in user_data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    contact_data = {
        "add": [
            {
                "name": user_data['name'],
                "custom_fields": [
                    {"id": 123, "values": [{"value": user_data.get('custom_field1', '')}]}
                ],
                "phone": [{"value": user_data['phone'], "type": "WORK"}],
                "email": [{"value": user_data.get('email', '')}],
            }
        ]
    }
    return contact_data

    contact_data = create_amo_contact(user_data)

    try:
        response = requests.post(f"{amo_api_url}/contacts", headers=headers, data=json.dumps(contact_data))
        response.raise_for_status()
        result = response.json()
        bot.send_message(message.chat.id, f"Контакт успешно создан. ID контакта: {result['add'][0]['id']}")
    except requests.exceptions.RequestException as e:
        bot.send_message(message.chat.id, f"Ошибка при отправке запроса: {e}")
        print(e)
    except json.JSONDecodeError as e:
        bot.send_message(message.chat.id, f"Ошибка при декодировании JSON-ответа: {e}")
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла непредвиденная ошибка: {e}")
        print(e)
    print("4")

bot.polling(none_stop=True)