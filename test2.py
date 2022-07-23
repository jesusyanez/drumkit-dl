import os
import zipfile


dir_name = './Drumkits/temp'
extension = ".zip"



for item in os.listdir(dir_name): # loop through items in dir
    try:
        if item.endswith(extension): # check for ".zip" extension
            file_name = dir_name + "/" + item
            # file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(dir_name) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
    except zipfile.BadZipFile:
        print("Extract failed:", item)
