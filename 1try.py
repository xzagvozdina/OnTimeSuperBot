import requests

from time import sleep

url = "https://api.telegram.org/bot831628342:AAEATt8fIU8cb5uOeeL34_QrJqATDz7WybQ/"


def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
	
	
def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
           update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()	
	
#обнулять счётчик по требованию
#почитать документацию библиотеки requests
{
  "ok":true,
  "result":[{
    "update_id":523349956,
    "message":{
      "message_id":51,
      "from":{
        "id":303262877,
        "first_name":"YourName"
      },
      "chat":{
        "id":303262877,
        "first_name":"YourName",
        "type":"private"
      },
      "date":1486829360,
      "text":"Hello"
    }
  }]
}