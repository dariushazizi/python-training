from pathlib import Path
#opening a text file:
path = Path('py_text.txt')
content = path.read_text()
print(content)
print(len(content))
words = content.split()
words_number = len(words)
print(words_number)

lines = content.splitlines()
python_text = ''
for line in lines:
    python_text += line
    python_text += '\t'
    
print(python_text)
print(len(python_text))

#using replace method:
new_content = content.replace('python', 'C++')
print(new_content)
print(len(new_content))

for line in lines:
    new_line = line.replace('python', 'Rust')
    python_text += new_line
print(python_text)
print(len(python_text))

for line in content.splitlines():
    print(line)


    
#writing on files:
path = Path('guest.txt')
user_name = input('Hey! Whats your name? ')
path.write_text(user_name)
names = path.read_text()
print(names)

#creating a while loop:
path = Path('guest_book.txt')
names_list = []
name = ''
while True:
    guest_numbers = input('how many guests do you have?' )
    g_numbers = range(1, int(guest_numbers)+1)
    for guest_number in g_numbers:
        name = input(f'whats the name of guest number {guest_number}? ')
        names_list.append(name)
    break

name_content = ''
print('guest list is:')
for item in names_list:
    name_content += f'{item}\n'
    print(f'-{item}')
    
path.write_text(name_content)

# Addition for exceptions:
#quite the while def:
def quit_while(exit_name):
    return exit_name != 'q'

while True:
    number1 = input('add first number: (type q for quite) ')
    if not quit_while(number1):
        break
    number2 = input('add second number: (type q for quite) ')
    if not quit_while(number2):
        break
    try:
        check = int(number1) + int(number2)
    except:
        print('only numbers are accepted! you added a string!')
    else:
        number = ''
        number += number1
        number += number2
        print (number)
        
while True:
    active = ''
    while True:
        chosen_file = input('cats or dogs? (type "q" for exit)')
        if not quit_while(chosen_file):
            print('exiting the program.')
            active = 'q'
            break
        if chosen_file == 'dogs' or chosen_file == 'cats':
            break
        else:
            print('just write one of the words "cats" or "dogs"')
    if not quit_while(active):
        break
    path = Path(f'{chosen_file}.txt')
    try:
        content = path.read_text()
        print(content)
        break
    except FileNotFoundError:
        print(f'the {path} file does not exist!')
        continue
