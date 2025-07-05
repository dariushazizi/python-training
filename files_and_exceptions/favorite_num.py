from pathlib import Path
import json


def get_user_num(path):
    """achieving the favorite number of user and storing it"""
    fave_number = input('Whats your favorite number? ')
    content = json.dumps(fave_number)
    path.write_text(content)
    print('now i know your favorite number!\n')
    
def prepare_user_num(path):
    """prepare the favorite number of user which stored before for printing"""
    if path.exists():
        content = path.read_text()
        stored_number = json.loads(content)
        return stored_number
    else:
        get_user_num(path)
        
def show_number():
    """for showing the favorite number stored"""
    path = Path('fave_num.json')
    favorite_number = prepare_user_num(path)
    print(f'your favorite number is {favorite_number}\n\n')
    
show_number()