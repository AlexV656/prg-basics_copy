import random
countries_lst = ['Poland','China','Germany','Norway','USA']
countries = [{'name': country} for country in countries_lst]
for dict_c in countries:dict_c['population'] = random.randint(10000,1000000)
print(countries)