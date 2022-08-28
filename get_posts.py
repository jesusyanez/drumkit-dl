import requests
import json
import html

url = "https://www.reddit.com/r/Drumkits/.json"

def fetch_json(url):
  payload={}
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  json_data = json.loads(response.text)

  return json_data


def format_data(json_data):
  def find_drumkits(kit):
    return kit

  map_drumkits = map(find_drumkits, json_data['data']['children'])

  acccepted_domains = ["drive.google.com", "dropbox.com", "mediafire.com"]
  drumkit_list = []

  for x in map_drumkits:
    item = x['data']
    if item['domain'] in acccepted_domains:
      temp_list = []
      temp_list.extend((html.unescape(item['title']), item['url'], item['author'], item['score']))
      drumkit_list.append(temp_list)

  return drumkit_list

def get_data():
  json_data = fetch_json(url)
  display_list = format_data(json_data)
  return display_list
