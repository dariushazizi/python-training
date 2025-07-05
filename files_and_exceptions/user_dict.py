from pathlib import Path
import json

def exit_loop(exit_name):
    return exit_name == 'q'

def save_json(user_dict):
    """saving a specific value in a json file"""
    path = Path('user_dict_info.json')
    content = json.dumps(user_dict)
    path.write_text(content)
    
def load_json():
    path = Path('user_dict_info.json')
    content = path.read_text()
    info = json.loads(content)
    return info

def get_user_info():
    """asking for extra info from user and store that as a dictionary"""
    user_dict = {}
    while True:
        user_key = input('***whats the title of info you want to add?(type "q" for exit) ')
        if exit_loop(user_key):
            break
        user_value = input('*** whats the value of that? ')
        user_dict[user_key] = user_value
        print(f'the {user_value} added as {user_key} to your information.')
    save_json(user_dict)
    
def prepare_info(path):
    if path.exists():
        available_info = load_json()
    else:
        get_user_info()
        available_info = load_json()
    return available_info
def verify_user(saved_dict):
    dict_key_list = list(saved_dict.keys())
    dict_value_list = list(saved_dict.values())
    user_answer = input(f'whats your {dict_key_list[0]}?')
    if user_answer != dict_value_list[0]:
        print('you are not recognized! lets create your own dict')
        get_user_info()

def showing_info():
    path = Path('user_dict_info.json')
    saved_dict = prepare_info(path)   
    verify_user(saved_dict)
    for item in saved_dict:
        print(f'the {item} is {saved_dict[item]}.')
            
showing_info()
