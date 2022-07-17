from get_time import right_now
from urllib.request import urlopen
import json

print(r"""
 _______                                     __        __    __            ________  __                                                             
|       \                                   |  \      |  \  |  \          |        \|  \                                                            
| $$$$$$$\  ______   __    __  ______ ____  | $$   __  \$$ _| $$_         | $$$$$$$$ \$$ _______    ______    _______   _______   ______    ______  
| $$  | $$ /      \ |  \  |  \|      \    \ | $$  /  \|  \|   $$ \        | $$__    |  \|       \  /      \  /       \ /       \ /      \  /      \ 
| $$  | $$|  $$$$$$\| $$  | $$| $$$$$$\$$$$\| $$_/  $$| $$ \$$$$$$        | $$  \   | $$| $$$$$$$\|  $$$$$$\|  $$$$$$$|  $$$$$$$|  $$$$$$\|  $$$$$$\
| $$  | $$| $$   \$$| $$  | $$| $$ | $$ | $$| $$   $$ | $$  | $$ __       | $$$$$   | $$| $$  | $$| $$    $$ \$$    \  \$$    \ | $$    $$| $$   \$$
| $$__/ $$| $$      | $$__/ $$| $$ | $$ | $$| $$$$$$\ | $$  | $$|  \      | $$      | $$| $$  | $$| $$$$$$$$ _\$$$$$$\ _\$$$$$$\| $$$$$$$$| $$      
| $$    $$| $$       \$$    $$| $$ | $$ | $$| $$  \$$\| $$   \$$  $$      | $$      | $$| $$  | $$ \$$     \|       $$|       $$ \$$     \| $$      
 \$$$$$$$  \$$        \$$$$$$  \$$  \$$  \$$ \$$   \$$ \$$    \$$$$        \$$       \$$ \$$   \$$  \$$$$$$$ \$$$$$$$  \$$$$$$$   \$$$$$$$ \$$       
                                      


Created for r/drumkits by Aesap (https://twitter.com/_aesap)

""")
# print('Created for r/drumkits by Aesap (https://twitter.com/_aesap)\n')

# print('Last Update: ' + str(right_now()))
# print('Trending on https://reddit.com/r/drumkits at ' + right_now() +'\n\n')

# store the URL in url as 
# parameter for urlopen
url = "https://www.reddit.com/r/Drumkits/.json"
  
# store the response of URL
response = urlopen(url)

# storing the JSON response 
# from url in data
data_json = json.loads(response.read())


def find_drumkits(kit):
    return kit

map_drumkits = map(find_drumkits, data_json['data']['children'])
# print(map_drumkits)
count = 1
url_list = []
number_list = []
for x in map_drumkits:
    if x['data']['domain'] == 'drive.google.com':
        print("["+str(count)+"] "+x['data']['title'])
        url_list.append(x['data']['url'])
        number_list.append(count)
        count +=1

urls_for_download_dict = {key:value for (key, value) in zip(number_list, url_list)}
print("Using two lists: ", urls_for_download_dict)

# print(url_list)

# Print selection input
download_list = input('Enter drumkits you want to download:\n')
print(download_list)

# make a list from download_list

# create dictionary, key: count, value: url




# dk_title = data_json['data']['children'][2]['data']['title']
# dk_upvote = str(data_json['data']['children'][2]['data']['ups'])
# dk_domain = data_json['data']['children'][2]['data']['domain']
# dk_url = data_json['data']['children'][2]['data']['url']

# print(dk_title)
# print(dk_upvote)
# print(dk_domain)
# print(dk_url)

# print("[0]: " + dk_title + " Upvotes: " + dk_upvote)
