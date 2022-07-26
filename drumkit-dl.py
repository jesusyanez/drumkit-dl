# This program downloads drumkits from reddit.com/r/drumkits
# It is limited to google drive link
# Requirements: gdown

import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
import termcolor
import gdrivedl
import pathlib
import zipfile

print(termcolor.colored(r"""
██████  ██████  ██    ██ ███    ███ ██   ██ ██ ████████ ██████  ██      
██   ██ ██   ██ ██    ██ ████  ████ ██  ██  ██    ██    ██   ██ ██      
██   ██ ██████  ██    ██ ██ ████ ██ █████   ██    ██    ██   ██ ██      
██   ██ ██   ██ ██    ██ ██  ██  ██ ██  ██  ██    ██    ██   ██ ██      
██████  ██   ██  ██████  ██      ██ ██   ██ ██    ██    ██████  ███████ 
                                                                                                                                                                                     
""", "green"))

print('                             Version 1.0                 ')
print('███████████████████████████████████████████████████████████████████████')

# Get r/Drumkits json data
main_url = "https://www.reddit.com/r/Drumkits/.json"
response = urlopen(main_url)
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

def download_folder(url, output_folder, filename=None):
    dl = gdrivedl.GDriveDL(quiet=False, overwrite=False, mtimes=False)
    dl.process_url(url, output_folder, filename=None)

def download_file(url, output_folder, filename):
    dl = gdrivedl.GDriveDL(quiet=False, overwrite=False, mtimes=False)
    dl.process_url(url, output_folder, filename)

def get_title(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for title in soup.find_all('title'):
        return title.get_text()[:-15]

def compression_type(file_name):
    # function to return the file extension
    file_extension = pathlib.Path(file_name).suffix
    return file_extension

def unzip(zipped_file, unzipped_file):
    if compression_type(zipped_file) == '.zip':
        print('extracting now')
        zip_path = './Drumkits/' + zipped_file
        unzip_path = './Drumkits/' + unzipped_file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                zip_ref.close()
        os.remove(zip_path)
    return

for x in selected_list:
    if 'folder' in url_dict[int(x)]:
        print('Downloading [' + x + ']: ' + title_dict[int(x)])
        output = get_title(url_dict[int(x)])
        output_path = './Drumkits/' + output
        download_folder(url_dict[int(x)], output_path)

    elif 'file' in url_dict[int(x)]:
        print('Downloading [' + x + ']: ' + title_dict[int(x)])
        temp_output = get_title(url_dict[int(x)])
        output = temp_output.split('.', 1)[0]
        download_file(url_dict[int(x)], './Drumkits', temp_output)
        unzip(temp_output, output)

    else: 
        print('The url for [' + x + ']: '+ url_dict[int(x)] + ' is not supported, sorry.')
                                                                 
print(termcolor.colored(r"""
███████████████████████████████████████████████████████████████████████ 



 ██████  ██████  ███    ███ ██████  ██      ███████ ████████ ███████ 
██      ██    ██ ████  ████ ██   ██ ██      ██         ██    ██      
██      ██    ██ ██ ████ ██ ██████  ██      █████      ██    █████   
██      ██    ██ ██  ██  ██ ██      ██      ██         ██    ██      
 ██████  ██████  ██      ██ ██      ███████ ███████    ██    ███████ 
                                                                     
                                                                     
You may close this window.
""", "green"))