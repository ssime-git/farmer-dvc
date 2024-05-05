import os
import requests
import zipfile
import logging

# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# Download the zipped dataset
#url = 'https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/yshdbyj6zy-1.zip' # not working anymore
#url = 'https://ars.els-cdn.com/content/image/1-s2.0-S2352340920303048-mmc1.zip'
#zip_name = "data.zip"
#wget.download(url, zip_name)


url = 'https://ars.els-cdn.com/content/image/1-s2.0-S2352340920303048-mmc1.zip'
zip_file_name = url.split('/')[-1]

response = requests.get(url)
if response.status_code == 200:
    with open(zip_file_name, 'wb') as file:
        file.write(response.content)

## Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_file_name,"r") as zip_ref:
    zip_ref.filelist[0].filename = '../data/data_raw.csv'
    zip_ref.extract(zip_ref.filelist[0])

os.remove(zip_file_name)



