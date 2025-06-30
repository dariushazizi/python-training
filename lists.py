#part one: creating a list and calling values from that

names = ['feri', 'taher', 'atoo', 'dadoo', 'new']

i = 0
while i < len(names):
    print(f'hello user {names[i].title()}')
    i = i+1
    
#part two
shahrokh_gfs = ['sorour','sogand','mashahd','sanaz', 'ghermezeh']
i = 0
years = len(shahrokh_gfs)

while i<len(shahrokh_gfs):
    now_gf = shahrokh_gfs.pop()
    print(f"in {i} year {now_gf} is shahrokh's gf." )
    i = i+1
    
friends_list = ['shahrokh','mokhtar','faraji','sogand1','parham','sina']
inv_list = []
for i in friends_list:
    inv_list.append(i)
    print(inv_list)
rej_list = inv_list.pop()
print(f'{rej_list} rejected the invitation')
inv_list.insert(0,'206')
inv_list.remove('parham')
del inv_list[0]
print(inv_list)

#part three: sorting lists
visit_list = ['russia','armenia','india','turkey','saudi arabia']
print(visit_list)
print(sorted(visit_list))
print(visit_list)
visit_list.reverse()
print(visit_list)
visit_list.sort()
print(visit_list)
visit_list.sort(reverse=True)
print(visit_list)
print(len(visit_list))
print(visit_list[-1])
visit_list = ['russia','armenia','india','turkey','saudi arabia']
visit_list.reverse()
year = ['2008','2012','2014','2022','2024']
num = list(range(1,len(year)+1))
print(num)
i = 0
print('\n')
for country in visit_list:
    print(f"The {num[i]} country  I've visited is {country.title()} in {year[i]}.")
    i = i+1

train_list = [value**2 for value in range(0,10,2)]
print(train_list)