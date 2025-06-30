article_dict = {
    'ML' : {
        'topic' : 'machine learning',
        'pages' : '42',
        'rate' : '5'
    },
    'LLM' : {
        'topic' : 'language model',
        'pages' : '60',
        'rate' : '4'
    },
    'HTML' : {
        'topic' : 'website',
        'pages' : '92',
        'rate' : '4.5'
    }
}

# adding info to article dict:
def article_import():
    '''adding info to article dict:'''
    while True:
        article = input('whats the article name? write done if you done. ')
        if article == 'done':
            break
        else:
            topic = input('add your topic: ')
            pages = input('add pages number: ')
            rate = input('add its rate: ')
            new_article_info = {
                'topic' : topic,
                'pages' : pages,
                'rate' : rate
            }
        article_dict[article] = new_article_info
    
best_choice = []
diff_list = []
num_message = 'please tell me how much you want to read? '
max_page = input(num_message)

for article,info in article_dict.items():
    diff = int(info['pages']) - int(max_page)
    diff = abs(diff)
    diff_list.append([article, diff])
    if best_choice == []:
        best_choice = [article, diff]
    elif best_choice[1] > diff:
        best_choice = [article, diff]

print(f' the {best_choice[0]} is the best for you with {best_choice[1]} pages difference.')    
    


    
