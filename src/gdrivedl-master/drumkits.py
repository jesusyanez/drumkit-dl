from get_time import right_now
from urllib.request import urlopen
import json

print(r"""
██████╗ ██████╗ ██╗   ██╗███╗   ███╗██╗  ██╗██╗████████╗███████╗      ██████╗ ██╗     
██╔══██╗██╔══██╗██║   ██║████╗ ████║██║ ██╔╝██║╚══██╔══╝██╔════╝      ██╔══██╗██║     
██║  ██║██████╔╝██║   ██║██╔████╔██║█████╔╝ ██║   ██║   ███████╗█████╗██║  ██║██║     
██║  ██║██╔══██╗██║   ██║██║╚██╔╝██║██╔═██╗ ██║   ██║   ╚════██║╚════╝██║  ██║██║     
██████╔╝██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██╗██║   ██║   ███████║      ██████╔╝███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝      ╚═════╝ ╚══════╝
                                                                                      


Created for r/drumkits by Aesap (https://twitter.com/_aesap)

""")
# print('Created for r/drumkits by Aesap (https://twitter.com/_aesap)\n')

# print('Last Update: ' + str(right_now()))
# print('Trending on https://reddit.com/r/drumkits at ' + right_now() +'\n\n')

# Get reddit json data
url = "https://www.reddit.com/r/Drumkits/.json"
response = urlopen(url)
data_json = json.loads(response.read())

def find_drumkits(kit):
    return kit

map_drumkits = map(find_drumkits, data_json['data']['children'])
# print(map_drumkits)
count = 1
url_list = []
title_list = []
for x in map_drumkits:
    if x['data']['domain'] == 'drive.google.com':
        print("["+str(count)+"] "+x['data']['title'])
        title_list.append(x['data']['title'])
        url_list.append(x['data']['url'])
        count += 1

# print(url_list)

# Print selection input
to_download_str = input('Enter drumkits you want to download:\n')

selected_list = to_download_str.split(", ")

for x in selected_list:
    print(x)
print (selected_list)
