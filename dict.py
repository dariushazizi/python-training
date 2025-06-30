shahrokh = {
    'name' : 'amir reza',
    'last name' : 'shahrokhshahi',
    'favorite food' : 'meat',
    'favorite activity' : 'racing',
    'favorite car' : '206',
    'gf' : 'sogand',
    'worst gf' : 'sogand',
}

for item in shahrokh:
    print(f' shahrokh {item} is {shahrokh[item]}')

for value in sorted(set(shahrokh.values())):
    print(f'\nshahrokh related to {value}')
    
list = [] 
alphabet = ['a','b','c','d','e','f','g']
for num in range(len(alphabet)):
        alphabetic = alphabet[num]
        list.append(alphabetic)
        print(list)
        
        
dariush ={
    'shahrokh' : {
        'gf' : 'sanaz',
        'label' : 'driver'
    },
    'mokhtar' : {
        'gf' : 'single',
        'label' : 'pashm'
    },
    'sogand' : {
        'gf' : 'amir reza',
        'label' : 'blue girl'
    }
    
}

for name,info in dariush.items():
    print(f'\n{name} has the info below:')
    print(f'the gf is {info['gf']} and the label is {info['label']}')
    for key, value in info.items():
        print(key, ':' ,value)