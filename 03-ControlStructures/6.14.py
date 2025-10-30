facebook = True
twitter = False
instagram = True
platform_count = 0
platform_dict = {'facebook':True,'twitter':False,'instagram':True}
for value in platform_dict.values():
    if value:
        platform_count+=1

if platform_count>=2:
    print('You are a good influencer!')