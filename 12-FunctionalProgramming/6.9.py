dic = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
print('Cities with positive temperatures:',' '.join([city for city,temp in dic.items() if temp>0]))
