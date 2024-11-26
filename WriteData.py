import json

def InsertData(words):
    try:
        with open('BlockedList.json', 'r') as file:
            try:
                data = json.load(file)
                if not isinstance(data, dict):
                    data = {}
            except json.JSONDecodeError:
                data = {}
    except FileNotFoundError:
        data = {}

    if 'BlockedList' not in data or not isinstance(data['BlockedList'], list):
        data['BlockedList'] = []


    with open('BlockedList.json', 'w') as file:
        json.dump(data, file, indent=4)

