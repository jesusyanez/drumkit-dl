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
# import urllib library
from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://www.reddit.com/r/Drumkits/.json"
  
# store the response of URL
response = urlopen(url)

# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
# print(data_json['data']['children'])

# print(data_json['data']['children'][0]['data']['title'])

def find_drumkits(kit):
    return kit

map_drumkits = map(find_drumkits, data_json['data']['children'])
# print(map_drumkits)
count = 1
for x in map_drumkits:
    if x['data']['domain'] == 'drive.google.com':
        print("["+str(count)+"] "+x['data']['url'])
        count +=1

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
