from amocrm.v2 import (tokens,Lead as _Lead,custom_field,Contact,Call)
import requests
import json
import tests

json_data_string ='''
{
  "PHONE": {
    "ID": 24793,
    "NAME": "Телефон",
    "TYPE_ID": 2,
    "ACCOUNT_ID": 32001522,
    "DESCRIPTION": null,
    "CODE": "PHONE",
    "SORT": 2,
    "ENTREE_CONTACTS": 1,
    "ENTREE_COMPANY": 0,
    "ENTREE_CATALOG": 0,
    "ENTREE_CUSTOMERS": 0,
    "PREDEFINED": "Y",
    "MULTIPLE": "Y",
    "DISABLED": 0,
    "ORIGIN": null,
    "CATALOG_ID": null,
    "SETTINGS": {
      "is_required": {},
      "is_deletable": true,
      "is_visible": true,
      "triggers": null,
      "vat_rates": {},
      "filter_type": null,
      "tracking_callback": "",
      "search_in": "",
      "currency": "",
      "chained_lists": null
    },
    "deleted_at": null,
    "ELEMENT_TYPES": {
      "0": 2
    },
    "ENTREE_DEALS": 0,
    "TYPE_CODE": "PHONE",
    "~NAME": "Телефон",
    "ENUMS": {
      "12365": {
        "ID": 12365,
        "VALUE": "WORK",
        "~VALUE": "WORK",
        "SORT": 2,
        "code": null,
        "TOTAL": 0
      },
      "12367": {
        "ID": 12367,
        "VALUE": "PRIV",
        "~VALUE": "PRIV",
        "SORT": 4,
        "code": null,
        "TOTAL": 0
      },
      "12369": {
        "ID": 12369,
        "VALUE": "OTHER",
        "~VALUE": "OTHER",
        "SORT": 6,
        "code": null,
        "TOTAL": 0
      }
    }
  },
  "WEB": {
    "ID": 24797,
    "NAME": "Web",
    "TYPE_ID": 7,
    "ACCOUNT_ID": 32001522,
    "DESCRIPTION": null,
    "CODE": "WEB",
    "SORT": 8,
    "ENTREE_CATALOG": 0,
    "PREDEFINED": "Y",
    "MULTIPLE": "N",
    "DISABLED": 0,
    "ORIGIN": null,
    "CATALOG_ID": null,
    "SETTINGS": {
      "is_required": {},
      "is_deletable": true,
      "is_visible": true,
      "triggers": null,
      "vat_rates": {},
      "filter_type": null,
      "tracking_callback": "",
      "search_in": "",
      "currency": "",
      "chained_lists": null
    },
    "deleted_at": null,
    "ELEMENT_TYPES": {
      "0": 3
    },
    "ENTREE_DEALS": 0,
    "ENTREE_CONTACTS": 0,
    "ENTREE_COMPANY": 1,
    "ENTREE_CUSTOMERS": 0,
    "TYPE_CODE": "URL",
    "~NAME": "Web"
  },
  "ADDRESS": {
    "ID": 24799,
    "NAME": "Адрес",
    "TYPE_ID": 9,
    "ACCOUNT_ID": 32001522,
    "DESCRIPTION": null,
    "CODE": "ADDRESS",
    "SORT": 10,
    "ENTREE_CATALOG": 0,
    "PREDEFINED": "Y",
    "MULTIPLE": "N",
    "DISABLED": 0,
    "ORIGIN": null,
    "CATALOG_ID": null,
    "SETTINGS": {
      "is_required": {},
      "is_deletable": true,
      "is_visible": true,
      "triggers": null,
      "vat_rates": {},
      "filter_type": null,
      "tracking_callback": "",
      "search_in": "",
      "currency": "",
      "chained_lists": null
    },
    "deleted_at": null,
    "ELEMENT_TYPES": {
      "0": 3
    },
    "ENTREE_DEALS": 0,
    "ENTREE_CONTACTS": 0,
    "ENTREE_COMPANY": 1,
    "ENTREE_CUSTOMERS": 0,
    "TYPE_CODE": "TEXTAREA",
    "~NAME": "Адрес"
  },
  "UTM_CONTENT": {
    "ID": 24801,
    "NAME": "utm_content",
    "TYPE_ID": 21,
    "ACCOUNT_ID": 32001522,
    "DESCRIPTION": null,
    "CODE": "UTM_CONTENT",
    "SORT": 503,
    "ENTREE_CONTACTS": 0,
    "ENTREE_COMPANY": 0,
    "ENTREE_CATALOG": 0,
    "ENTREE_CUSTOMERS": 0,
    "PREDEFINED": "Y",
    "MUSORT": 516,
        "ENTREE_CONTACTS": 0,
        "ENTREE_COMPANY": 0,
        "ENTREE_CATALOG": 0,
        "ENTREE_CUSTOMERS": 0,
        "PREDEFINED": "Y",
        "MULTIPLE": "N",
        "DISABLED": 0,
        "ORIGIN": null,
        "CATALOG_ID": null,
        "SETTINGS": {
            "is_required": {},
            "is_deletable": true,
            "is_visible": null,
            "triggers": null,
            "vat_rates": {},
            "filter_type": null,
            "tracking_callback": "",
            "search_in": "",
            "currency": "",
            "chained_lists": null
        },
        "deleted_at": null,
        "ELEMENT_TYPES": {"0": 2},
        "ENTREE_DEALS": 1,
        "TYPE_CODE": "TRACKING_DATA",
        "~NAME": "gclientid"
    },
    "YCLID": {
        "ID": 24835,
        "NAME": "yclid",
        "TYPE_ID": 21,
        "ACCOUNT_ID": 32001522,
        "DESCRIPTION": null,
        "CODE": "YCLID",
        "SORT": 520,
        "ENTREE_CONTACTS": 0,
        "ENTREE_COMPANY": 0,
        "ENTREE_CATALOG": 0,
        "ENTREE_CUSTOMERS": 0,
        "PREDEFINED": "Y",
        "MULTIPLE": "N",
        "DISABLED": 0,
        "ORIGIN": null,
        "CATALOG_ID": null,
        "SETTINGS": {
            "is_required": {},
            "is_deletable": null,
            "is_visible": null,
            "triggers": null,
            "vat_rates": {},
            "filter_type": null,
            "tracking_callback": "",
            "search_in": "",
            "currency": "",
            "chained_lists": null
        },
        "deleted_at": null,
        "ELEMENT_TYPES": {"0": 2},
        "ENTREE_DEALS": 1,
        "TYPE_CODE": "TRACKING_DATA",
        "~NAME": "yclid"
    },
    "_YM_UID": {
        "ID": 24829,
        "NAME": "_ym_uid",
        "TYPE_ID": 21,
        "ACCOUNT_ID": 32001522,
        "DESCRIPTION": null,
        "CODE": "_YM_UID",
        "SORT": 517,
        "ENTREE_CONTACTS": 0,
        "ENTREE_COMPANY": 0,
        "ENTREE_CATALOG": 0,
        "ENTREE_CUSTOMERS": 0,
        "PREDEFINED": "Y",
        "MULTIPLE": "N",
        "DISABLED": 0,
        "ORIGIN": null,
        "CATALOG_ID": null,
        "SETTINGS": {
            "is_required": {},
            "is_deletable": null,
            "is_visible": null,
            "triggers": null,
            "vat_rates": {},
            "filter_type": null,
            "tracking_callback": "",
            "search_in": "",
            "currency": "",
            "chained_lists": null
        },
        "deleted_at": null,
        "ELEMENT_TYPES": {"0": 2},
        "ENTREE_DEALS": 1,
        "TYPE_CODE": "TRACKING_DATA",
        "~NAME": "_ym_uid"
    },
    "_YM_COUNTER": {
        "ID": 24831,
        "NAME": "_ym_counter",
        "TYPE_ID": 21,
        "ACCOUNT_ID": 32001522,
        "DESCRIPTION": null,
        "CODE": "_YM_COUNTER",
        "SORT": 518,
        "ENTREE_CONTACTS": 0,
        "ENTREE_COMPANY": 0,
        "ENTREE_CATALOG": 0,
        "ENTREE_CUSTOMERS": 0,
        "PREDEFINED": "Y",
        "MULTIPLE": "N",
        "DISABLED": 0,
        "ORIGIN": null,
        "CATALOG_ID": null,
        "SETTINGS": {
            "is_required": {},
            "is_deletable": true,
            "is_visible": true,
            "triggers": null,
            "vat_rates": {},
            "filter_type": null,
            "tracking_callback": "",
            "search_in": "",
            "currency": "",
            "chained_lists": null
        },
        "deleted_at": null,
        "ELEMENT_TYPES": {"0": 2},
        "ENTREE_DEALS": 1,
        "TYPE_CODE": "TRACKING_DATA",
        "~NAME": "_ym_counter"
    },
    "GCLID": {
        "ID": 24833,
        "NAME": "gclid",
        "TYPE_ID": 21,
        "ACCOUNT_ID": 32001522,
        "DESCRIPTION": null,
        "CODE": "GCLID",
        "SORT": 519,
        "ENTREE_CONTACTS": 0,
        "ENTREE_COMPANY": 0,
        "ENTREE_CATALOG": 0,
        "ENTREE_CUSTOMERS": 0,
        "PREDEFINED": "Y",
        "MULTIPLE": "N",
        "DISABLED": 0,
        "ORIGIN": null,
        "CATALOG_ID": null,
        "SETTLTIPLE": "N",
    "DISABLED": 0,
    "ORIGIN": null,
    "CATALOG_ID": null,
    "SETTINGS": {
      "is_required": {},
      "is_deletable": true,
      "is_visible": true,
      "triggers": null,
      "vat_rates": {},
      "filter_type": null,
      "tracking_callback": "",
      "search_in": "",
      "currency": "",
      "chained_lists": null
    },
    "deleted_at": null,
    "ELEMENT_TYPES": {
      "0": 2
    },
    "ENTREE_DEALS": 1,
    "TYPE_CODE": "TRACKING_DATA",
    "~NAME": "utm_content"
  },
  "POSITION": {
    "ID": 24791,
    "NAME": "Должность",
    "TYPE_ID": 1,
    "ACCOUNT_ID": 32001522,
    "DESCRIPTION": null,
    "CODE": "POSITION",
    "SORT": 503,
    "ENTREE_COMPANY": 0,
    "ENTREE_CATALOG": 0,
    "ENTREE_CUSTOMERS": 0,
    "PREDEFINED": "Y",
    "MULTIPLE": "N",
    "DISABLED": 0,
    "ORIGIN": null,
    "CATALOG_ID": null,
    "SETTINGS": {
      "is_required": {},
      "is_deletable": true,
      "is_visible": true,
      "triggers": null,
      "vat_rates": {},
      "filter_type": null,
      "tracking_callback": "",
      "search_in": "",
      "currency": "",
      "chained_lists": null
    },
    "deleted_at": null,
    "ELEMENT_TYPES": {
      "0": 1
    },
    "ENTREE_DEALS": 0,
    "ENTREE_CONTACTS": 1,
    "TYPE_CODE": "TEXT",
    "~NAME": "Должность"
  },
  "UTM_MEDIUM": {
    "ID": 24803,
    "NAME": "utm_medium",
    "TYPE_ID": 21,
    "ACCOUNT_ID": 32001522,
    "DESCRIPTION": null,
    "CODE": "UTM_MEDIUM",
    "SORT": 504,
    "ENTREE_CONTACTS": 0,
    "ENTREE_COMPANY": 0,
    "ENTREE_CATALOG": 0,
    "ENTREE_CUSTOMERS": 0,
    "PREDEFINED": "Y",
    "MULTIPLE": "N",
    "DISABLED": 0,
    "ORIGIN": null,
    "CATALOG_ID": null,
    "SETTINGS": {
      "is_required": {},
      "is_deletable": true,
      "is_visible": true,
      "triggers": null,
      "vat_rates": {},
      "filter_type": null,
      "tracking_callback": "",
      "search_in": "",
      "currency": "",
      "chained_lists": null
    },
    "deleted_at": null,
    "ELEMENT_TYPES": {
      "0": 2
    },
    "ENTREE_DEALS": 1,
    "TYPE_CODE": "TRACKING_DATA",
    "~NAME": "utm_medium"
  },
  "UTM_CAMPAIGN": {
    "ID": 24805,
    "NAME": "utm_campaign",
    "TYPE_ID": 21,
    "ACCOUNT_ID": 32001522,
    "DESCRIPTION": null,
    "CODE": "UTM_CAMPAIGN",
    "SORT": 505,
    "ENTREE_CONTACTS": 0,
    "ENTREE_COMPANY": 0,
    "ENTREE_CATALOG": 0,
    "ENTREE_CUSTOMERS": 0,
    "PREDEFINED": "Y",
    "MULTIPLE": "N",
    "DISABLED": 0,
    "ORIGIN": null,
    "CATALOG_ID": null,
    "SETTINGS": {
      "is_required": {},
      "is_deletable": true,
      "is_visible": true,
      "triggers": null,
      "vat_rates": {},
      "filter_type": null,
      "tracking_callback": "",
      "search_in": "",
      "currency": "",
      "chained_lists": null
    },
    "deleted_at": null,
    "ELEMENT_TYPES": {
      "0": 2
    },
    "ENTREE_DEALS": 1,
    "TYPE_CODE": "TRACKING_DATA",
    "~NAME": "utm_campaign"
  },
  "UTM_SOURCE": {
    "ID": 24807,
    "NAME": "utm_source",
    "TYPE_ID": 21,
    "ACCOUNT_ID": 32001522,
    "DESCRIPTION": null,
    "CODE": "UTM_SOURCE",
    "SORT": 506,
    "ENTREE_CONTACTS": 0,
    "ENTREE_COMPANY": 0,
    "ENTREE_CATALOG": 0,
    "ENTREE_CUSTOMERS": 0,
    "PREDEFINED": "Y",
    "MULTIPLE": "N",
    "DISABLED": 0,
    "ORIGIN": null,
    "CATALOG_ID": null,
    "SETTINGS": {
      "is_required": {},
      "is_deletable": true,
      "is_visible": true,
      "triggers": null,
      "vat_rates": {},
      "filter_type": null,
      "tracking_callback": "",
      "search_in": "",
      "currency": "",
      "chained_lists": null
    },
    "deleted_at": null,
    "ELEMENT_TYPES": {
      "0": 2
    },
    "ENTREE_DEALS": 1,
        "TYPE_CODE": "TRACKING_DATA",
        "NAME": "utm_source",
        "OPENSTAT_AD":{
        "ID":24821,
        "NAME":"openstat_ad",
        "TYPE_ID":21,
        "ACCOUNT_ID":32001522,
        "DESCRIPTION":null,
        "CODE":"OPENSTAT_AD",
        "SORT":513,
        "ENTREE_CONTACTS":0,
        "ENTREE_COMPANY":0,
        "ENTREE_CATALOG":0,
        "ENTREE_CUSTOMERS":0,
        "PREDEFINED":"Y",
        "MULTIPLE":"N",
        "DISABLED":0,
        "ORIGIN":null,
        "CATALOG_ID":null,
        "SETTINGS":{
            "is_required":{},
            "is_deletable":true,
            "is_visible":true,
            "triggers":null,
            "vat_rates":{},
            "filter_type":null,
            "tracking_callback":"",
            "search_in":"","currency":"",
            "chained_lists":null},
            "deleted_at":null,
            "ELEMENT_TYPES":{"0":2},
            "ENTREE_DEALS":1,
            "TYPE_CODE":"TRACKING_DATA",
            "NAME":"openstat_ad"
        },
    "OPENSTAT_SOURCE":{
        "ID":24823,
        "NAME":"openstat_source",
        "TYPE_ID":21,
        "ACCOUNT_ID":32001522,
        "DESCRIPTION":null,
        "CODE":"OPENSTAT_SOURCE",
        "SORT":514,
        "ENTREE_CONTACTS":0,
        "ENTREE_COMPANY":0,
        "ENTREE_CATALOG":0,
        "ENTREE_CUSTOMERS":0,
        "PREDEFINED":"Y",
        "MULTIPLE":"N",
        "DISABLED":0,
        "ORIGIN":null,
        "CATALOG_ID":null,
        "SETTINGS":{
            "is_required":{},
            "is_deletable":true,
            "is_visible":true,
            "triggers":null,
            "vat_rates":{},
            "filter_type":null,
            "tracking_callback":"",
            "search_in":"",
            "currency":"",
            "chained_lists":null},
            "deleted_at":null,
            "ELEMENT_TYPES":{"0":2},
            "ENTREE_DEALS":1,
            "TYPE_CODE":"TRACKING_DATA",
            "~NAME":"openstat_source"
        }
    },
    "OPENSTAT_AD":{
        "ID":24821,
        "NAME":"openstat_ad",
        "TYPE_ID":21,
        "ACCOUNT_ID":32001522,
        "DESCRIPTION":null,
        "CODE":"OPENSTAT_AD",
        "SORT":513,
        "ENTREE_CONTACTS":0,
        "ENTREE_COMPANY":0,
        "ENTREE_CATALOG":0,
        "ENTREE_CUSTOMERS":0,
        "PREDEFINED":"Y",
        "MULTIPLE":"N",
        "DISABLED":0,
        "ORIGIN":null,
        "CATALOG_ID":null,
        "SETTINGS":{
            "is_required":{},
            "is_deletable":true,
            "is_visible":true,
            "triggers":null,
            "vat_rates":{},
            "filter_type":null,
            "tracking_callback":"",
            "search_in":"",
            "currency":"",
            "chained_lists":null,
            "deleted_at":null,
            "ELEMENT_TYPES":{"0":2},
            "ENTREE_DEALS":1,
            "TYPE_CODE":"TRACKING_DATA",
            "~NAME":"openstat_ad"
        }
    },
    "OPENSTAT_SOURCE":{
        "ID":24823,
        "NAME":"openstat_source",
        "TYPE_ID":21,
        "ACCOUNT_ID":32001522,
        "DESCRIPTION":null,
        "CODE":"OPENSTAT_SOURCE",
        "SORT":514,
        "ENTREE_CONTACTS":0,
        "ENTREE_COMPANY":0,
        "ENTREE_CATALOG":0,
        "ENTREE_CUSTOMERS":0,
        "PREDEFINED":"Y",
        "MULTIPLE":"N",
        "DISABLED":0,
        "ORIGIN":null,
        "CATALOG_ID":null,
        "SETTINGS":{
            "is_required":{},
            "is_deletable":true,
            "is_visible":true,
            "triggers":null,
            "vat_rates":{},
            "filter_type":null,
            "tracking_callback":"",
            "search_in":"",
            "currency":"",
            "chained_lists":null,
            "deleted_at":null,
            "ELEMENT_TYPES":{"0":2},
            "ENTREE_DEALS":1,
            "TYPE_CODE":"TRACKING_DATA",
            "~NAME":"openstat_source"
        }
    }
}
'''

class Lead(_Lead):
    test_text_field = custom_field.TextCustomField("Номер телефона")
    delivery_type = custom_field.SelectCustomField("Способ доставки")
    address = custom_field.TextCustomField("Адрес")

with open('access_token.txt', 'r') as file:
    refresh_token = file.read()
rt=refresh_token
with open('access_token.txt', 'r') as file:
    access_token = file.read()
at=access_token
amo_account_id = "svse343"
amo_client_id = "4421f483-c9e9-4608-94ef-a80a18772a14"
amo_client_secret = "CljQXBLLXr2zV0W4TRtwSj4iXPs39dEikxAECsLC6EdxtAiKlAS3a0N4Pc12OVv4"
name = "Иван Иванов"
phone_number = "+79161234567"
amo_domain='https://svse343.amocrm.ru'
amo_user='svse343@gmail.com'
amo_key='4421f483-c9e9-4608-94ef-a80a18772a14'

'''def refresh_access_token(refresh_token, amo_client_id, amo_client_secret):
    """Обновляет токен доступа, используя токен обновления."""
    token_url = "https://svse343/oauth2/access_token"# Замените на ваш URL
    token_data = {
        'client_id': amo_client_id,
        'client_secret': amo_client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    try:
        token_response = requests.post(token_url, data=token_data)
        token_response.raise_for_status()
        return token_response.json()['access_token']
    except Exception as e:
        print(f"Ошибка при обновлении токена: {e}")
        return None'''

def auth(user,user_hash):
    url = amo_domain + '/private/api/auth.php'
    data = {
        'USER_LOGIN': user,
        'USER_HASH': user_hash
    }
    res = requests.post(url, data=data, params={'type': 'json'})
    print('Authorization status code', res.status_code)

    if res.status_code == 200:
        contact_data = {
            "add": [
                {
                    "name": "Иван Иванов",
                    "first_name": "Иван",
                    "last_name": "Иванов",
                    "custom_fields": [
                        {
                            "id": 24793,
                            "values": [
                                {
                                    "value": "+79991112233",
                                    "enum": "WORK"
                                }
                            ]
                        },
                        {
                            "id": 24795,
                            "values": [
                            {
                                "value": "email@example.com",
                                "enum": "WORK"
                            }
                            ]
                        }
                    ],
                        "phone": [
                        {
                            "value": "+79991112233",
                            "type": "WORK"
                        }
                    ],
                        "email": [
                        {
                            "value": "email@example.com",
                            "type": "WORK"
                        }
                    ]
                }
            ]
        }
        headers = {
            "Authorization": f"Bearer {rt}",
            "Content-Type": "application/json",
        }
        res2 = requests.post(url, data=data, params={'type': 'json'})
        if res2.status_code == 200:
            url2 = f"https://{amo_account_id}.amocrm.ru/api/v4/contacts"
            response = requests.post(url2,
                                     headers=headers,
                                     data=json.dumps(contact_data),
                                     json=json_data_string)
            if response.status_code == 200:
                print("Post requests contact created")
            else:
                print('Post requests contact status code',response.status_code)
        else:
            print('Post requests contact status code',res2.status_code)

'''def load_custom_fields(filepath):
    """Загружает данные о пользовательских полях из JSON файла."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: Неверный формат JSON в файле '{filepath}'.")
        return None
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return None'''

if __name__ == '__main__':
    tokens.default_token_manager(
        client_id="4421f483-c9e9-4608-94ef-a80a18772a14",
        client_secret="CezMew5Cp3C9YMXe7jbuw6KnyDKcHexZFkOGcMfQvfqIvgWWu5Sf41x3mTXnadEq",
        subdomain="svse343",
        redirect_url="https://t.me/grgsdfgujgsjBot",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    )
    #после каждого запуска кода менять client_secret и длинющий код
    #tokens.default_token_manager.init(code='def5020036728f6b239fb4516335af90c6c0a2d8e4a4ebaaad0c72d4e81da1a125699a4cf7855c98709891a2a29ffc420a96519eb92e90433606fb04e62d104bf2d537b0d7c5d189321eee22ccd6085c2fc546ddb5d00922c157c537fa7e328d44ac49be7c813b5fcb08761e58d74ff8487b2e501ba75bdd894323deef880071df717917838264e5a4f777071dd98e77b14222d106bad7284e0557bab115fc9a4cdaf566c9c786e4a710caf7ac1eba53fea63f89fe914c06f5b386114edc26e920b145cdbf87209cbce519812228b75910e4abe88038b12c857da6e9addb3f3047fc2a368edc0d266805b5b860e29dfad7e3b229844c963628058b54a95222fd31972abfcd5cef24a5b39e49e97ce327682adda1815a5807427bf48e0185263e60a9afaba93a6db3f315a81df91166821ebd8672386b6cca8bc0d96e57408fe812bcb92d1a18ab44508812da34963d3b6f5a244c6811fd88611d19cdae4f93a57b04743b4b10054a8e0a8d34cbdfffb86c5648780682be4439fe0f6ae9ee59819d3edf6d75f262a56c51a152fd48fe4acda27c3bae7ce27f26a9cf1e6206c6e88f8b7068521b87b83c5c28cd086a5a92f512fa3054a9f7231cc94a185c1cc1d087a1bc2d0d9bb7f94b554ce1246d3627593532f40928eb5974fbcc49b5a4500ccd22c701fe2d3b227f1d9bf37d12',skip_error=False)
    user='svse343@gmail.com'
    user_hash=' y8qjMjTq'
    #load_custom_fields('cf.json')
    '''account_data = {
        "id": 32001522,
        "name": "svse343",
        "subdomain": "svse343",
        "predefined_cf": {
            "PHONE": {
                "ID": 24793,
                # ... (other PHONE data) ...
            },
            "EMAIL": {
                "ID": 24795,
                # ... (other EMAIL data) ...
            }
            # ... (other predefined_cf data) ...
        }
        # ... (other account data) ...
    }

    phone_field_id = account_data["predefined_cf"]["PHONE"]["ID"]
    email_field_id = account_data["predefined_cf"]["EMAIL"]["ID"]

    contact_data = {
        "add": [
            {
                "name": "Имя Фамилия",
                "first_name": "Имя",
                "last_name": "Фамилия",
                "custom_fields": [
                    {"id": phone_field_id, "values": [{"value": "+79991112233", "enum": "WORK"}]},
                    {"id": email_field_id, "values": [{"value": "email@example.com", "enum": "WORK"}]}
                ],
                "phone": [{"value": "+79991112233", "type": "WORK"}],
                "email": [{"value": "email@example.com", "type": "WORK"}]
            }
        ]
    }

    print(json.dumps(contact_data, indent=2))  # Вывод данных в формате JSON для amoCRM API'''

    auth(user,user_hash)