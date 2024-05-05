import os
import requests
import zipfile
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_file(url, dest_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raises an HTTPError if the request returned an unsuccessful status code

        with open(dest_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        logging.info(f"File downloaded successfully: {dest_path}")
        return dest_path
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request Exception: {e}")
    except Exception as e:
        logging.error(f"Error downloading file: {e}")
    return None

def extract_and_rename_zip(zip_file_path, extract_to, new_filename):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Rename the first file to the new filename and extract it
            zip_ref.filelist[0].filename = new_filename
            zip_ref.extract(zip_ref.filelist[0], path=extract_to)
        logging.info(f"File extracted and renamed successfully to: {new_filename}")
    except zipfile.BadZipFile as e:
        logging.error(f"Bad Zip File: {e}")
    except Exception as e:
        logging.error(f"Error extracting zip: {e}")

def main():
    url = 'https://ars.els-cdn.com/content/image/1-s2.0-S2352340920303048-mmc1.zip'
    zip_file_name = url.split('/')[-1]

    # Directory for extracted data, make sure it's relative to the current script path
    data_dir = 'data/'
    os.makedirs(data_dir, exist_ok=True)  # Ensure the data directory exists

    # The new filename should also include the path to the data directory
    new_filename = 'data_raw.csv'

    # Download the dataset
    download_path = download_file(url, zip_file_name)
    if download_path:
        # Extract and rename the file inside the zip
        extract_and_rename_zip(download_path, data_dir, new_filename)

        # Clean up the zip file
        os.remove(zip_file_name)
        logging.info(f"Removed zip file: {zip_file_name}")

if __name__ == '__main__':
    main()
