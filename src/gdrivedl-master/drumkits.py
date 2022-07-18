# This program downloads drumkits from reddit.com/r/drumkits
# It is limited to google drive link
# Requirements: gdown

from get_time import right_now
from urllib.request import urlopen
import random
import json
import gdrivedl
import os
import gdown
import re

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

#Random request to avoid getting blocked by reddit
# obfuscate_list = ['sports', 'funny', 'leagueoflegends', 'new', 'MadeMeSmile', 'canada', 'AskReddit', 'entertainment', 'space', 'technology', 'nodejs', 'gaming', 'unexpected', 'politics', 'PublicFreakout', 'movies', 'nba']
# fake_url = 'https://reddit.com/r/' + random.choice(obfuscate_list) + '/.json'
# print('pinged: ' +fake_url)
# fake_ping = urlopen(fake_url)


# Get r/Drumkits json data
url = "https://www.reddit.com/r/Drumkits/.json"
response = urlopen(url)
data_json = json.loads(response.read())


# json data --> Print and make data structures
def find_drumkits(kit):
    return kit

map_drumkits = map(find_drumkits, data_json['data']['children'])
count = 1
url_list = []
title_list = []
index_list = []
for x in map_drumkits:
    if x['data']['domain'] == 'drive.google.com': #filter only gdrive links
        print("["+str(count)+"] "+x['data']['title'])
        title_list.append(x['data']['title'])
        url_list.append(x['data']['url'])
        index_list.append(count)
        count += 1

# Create dictionaries for downloading with selected key
title_dict = {key:value for (key, value) in zip(index_list, title_list)}
url_dict = {key:value for (key, value) in zip(index_list, url_list)}

# Print selection input
to_download_str = input('Enter drumkits you want to download:\n')

selected_list = to_download_str.split(", ")

# download function
print('Now downloading ' + str(len(selected_list)) + ' drumkits. Check back in a 5 minutes.')

for x in selected_list:
    if 'folder' in url_dict[int(x)]:
        print('Downloading [' + x + ']: ' + title_dict[int(x)])
        filtered_title = re.sub(r'[^\w]', ' ', title_dict[int(x)])
        output = './Drumkits/' + filtered_title.replace(' ', '_')
        # command = 'py gdrivedl.py ' + url + ' -P ' + title #windows
        command = 'python3 gdrivedl.py ' + url_dict[int(x)] + ' -P ' + output #linux
        os.system(command)

    elif 'file' in url_dict[int(x)]:
        print('Downloading [' + x + ']: ' + title_dict[int(x)])
        output = './Drumkits/' + title_dict[int(x)] + '.zip'
        gdown.download(url=url_dict[int(x)], output=output, quiet=False, fuzzy=True)

    else: 
        print('The url for [' + x + ']: '+ url_dict[int(x)] + ' is messed up.')





                                                                      
print(r"""
██████   ██████  ██     ██ ███    ██ ██       ██████   █████  ██████  
██   ██ ██    ██ ██     ██ ████   ██ ██      ██    ██ ██   ██ ██   ██ 
██   ██ ██    ██ ██  █  ██ ██ ██  ██ ██      ██    ██ ███████ ██   ██ 
██   ██ ██    ██ ██ ███ ██ ██  ██ ██ ██      ██    ██ ██   ██ ██   ██ 
██████   ██████   ███ ███  ██   ████ ███████  ██████  ██   ██ ██████  


 ██████  ██████  ███    ███ ██████  ██      ███████ ████████ ███████ 
██      ██    ██ ████  ████ ██   ██ ██      ██         ██    ██      
██      ██    ██ ██ ████ ██ ██████  ██      █████      ██    █████   
██      ██    ██ ██  ██  ██ ██      ██      ██         ██    ██      
 ██████  ██████  ██      ██ ██      ███████ ███████    ██    ███████ 
                                                                     
                                                                     
You may close this window.
""")                             


