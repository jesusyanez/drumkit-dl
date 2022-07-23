# This program downloads drumkits from reddit.com/r/drumkits
# It is limited to google drive link
# Requirements: gdown

from distutils.log import error
# from get_time import right_now
from urllib.request import urlopen
import json
import os
import termcolor
import gdown
import re
# import zipfile

print(termcolor.colored(r"""
██████  ██████  ██    ██ ███    ███ ██   ██ ██ ████████ ██████  ██      
██   ██ ██   ██ ██    ██ ████  ████ ██  ██  ██    ██    ██   ██ ██      
██   ██ ██████  ██    ██ ██ ████ ██ █████   ██    ██    ██   ██ ██      
██   ██ ██   ██ ██    ██ ██  ██  ██ ██  ██  ██    ██    ██   ██ ██      
██████  ██   ██  ██████  ██      ██ ██   ██ ██    ██    ██████  ███████ 
                                                                        
                                                                                     
                            
""", "green"))

print('                             Version 1.0.1                 ')

print('███████████████████████████████████████████████████████████████████████')

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


# def extract(zipped_file, unzipped_file):

#     print('extracting now')
#     with zipfile.ZipFile(zipped_file, 'r') as zip_ref:
#             zip_ref.extractall(unzipped_file)
#             zip_ref.close()

    
    # os.remove(zipped_file)

# import os, zipfile
# def extract_all_and_delete(self):
#     dir_name = './Drumkits/temp/'
#     extension = ".zip"

#     os.chdir(dir_name) # change directory from working dir to dir with files

#     for item in os.listdir(dir_name): # loop through items in dir
#         if item.endswith(extension): # check for ".zip" extension
#             file_name = os.path.abspath(item) # get full path of files
#             zip_ref = zipfile.ZipFile(file_name) # create zipfile object
#             zip_ref.extractall(dir_name) # extract file to dir
#             zip_ref.close() # close file
#             os.remove(file_name) # delete zipped file


for x in selected_list:
    if 'folder' in url_dict[int(x)]:
        print('Downloading [' + x + ']: ' + title_dict[int(x)])
        filtered_title = re.sub(r'[^\w]', ' ', title_dict[int(x)])
        output = './Drumkits/' + filtered_title.replace(' ', '_')
        # command = 'py gdrivedl.py ' + url + ' -P ' + title #windows
        command = 'python3 gdrivedl.py ' + url_dict[int(x)] + ' -P ' + output + ' -q' #linux
        os.system(command)

    elif 'file' in url_dict[int(x)]:
        print('Downloading [' + x + ']: ' + title_dict[int(x)])
        filtered_title = re.sub(r'[^\w]', ' ', title_dict[int(x)])
        output = './Drumkits/' + filtered_title.replace(' ', '_')
        temp_output = './Drumkits/temp/' + filtered_title.replace(' ', '_') + '.zip'
        print(output)
        gdown.download(url=url_dict[int(x)], output=temp_output, quiet=False, fuzzy=True)
        # extract(temp_output, output)
        # with zipfile.ZipFile(temp_output, 'r') as zip_ref:
        #     zip_ref.extractall(output)
        # os.remove(temp_output) 

    else: 
        print('The url for [' + x + ']: '+ url_dict[int(x)] + ' is messed up.')

# extract_all_and_delete(self)

                                                                      
print(r"""
███████████████████████████████████████████████████████████████████████ 



 ██████  ██████  ███    ███ ██████  ██      ███████ ████████ ███████ 
██      ██    ██ ████  ████ ██   ██ ██      ██         ██    ██      
██      ██    ██ ██ ████ ██ ██████  ██      █████      ██    █████   
██      ██    ██ ██  ██  ██ ██      ██      ██         ██    ██      
 ██████  ██████  ██      ██ ██      ███████ ███████    ██    ███████ 
                                                                     
                                                                     
You may close this window.
""")                             


