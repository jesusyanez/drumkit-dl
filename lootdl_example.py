import lootdl

URL1 = 'https://www.mediafire.com/file/6c7qc4virx61e9q/MORTHNVR+PHONK+KIT+VOL.+1.zip/file'
URL2 = 'https://www.mediafire.com/file/5dsd2hto30spysy/Kanye+West+%26+JAY-Z+-+Watch+The+Throne+%5BDrumkit%5D.zip'
URL3 = 'https://www.mediafire.com/file/m14lgmko672qmxx/#maknae2021.zip/file'

download_list = [URL1, URL2, URL3]

for url in download_list:
 lootdl.grab(url, './')