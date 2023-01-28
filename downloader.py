import os
import csv
import hashlib
import urllib.request
from urllib.parse import urlparse
import concurrent.futures
import tarfile
from tqdm import tqdm

# Create the 'files' directory if it doesn't exist
os.makedirs("files", exist_ok=True)


# Read the urls from the 'urls.txt' file
try:
    with open('urls.txt') as file:
        urls = file.readlines()
except FileNotFoundError:
    print("[ERROR]: urls.txt file not found!")
    exit()
except:
    print("[ERROR]: An error occured while reading urls.txt!")
    exit()

print("[INFO]: Downloading and Hashing files")
def download_file(url):
    # Strip the newline character from the url
    url = url.strip()
    # Get the filename and directory path from the url
    parsed_url = urlparse(url)
    dirpath = os.path.dirname(parsed_url.path)
    dirpath = ''.join(('./files',dirpath))
    filename = os.path.basename(parsed_url.path)
    # Create the directory if it doesn't exist
    os.makedirs(os.path.join(dirpath), exist_ok=True)
    filepath = os.path.join( dirpath, filename)
    # if file already exists, skip to the next one
    if os.path.isfile(filepath):
        print(f"[INFO]: File {filepath} already exists, skipping...")
        return
    try:
        # Download the file
        urllib.request.urlretrieve(url, filepath)
        # Create a SHA1 hash of the file
        with open(filepath, "rb") as f:
            bytes = f.read()
            readable_hash = hashlib.sha1(bytes).hexdigest()
        # Write the filename and hash to the 'hashes.csv' file
        with open('hashes.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([os.path.join(dirpath, filename), readable_hash])
    except Exception as e:
        print(f"[ERROR]: Error occurred while downloading {filepath} : {e}")

# Use concurrent.futures to download multiple files at a time
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Use tqdm to display a progress bar
    for _ in tqdm(executor.map(download_file, urls), total=len(urls)):
        pass

print("[INFO]: Compressing")
# Tar the entire contents of the 'files' directory with highest compression
try:
    with tarfile.open('./files.tar.gz', mode='w:gz', compresslevel=9) as tar:
        tar.add('./files')
        print("[INFO]: Successfully created tar.gz file.")
except Exception as e:
    print(f"[ERROR]: Error occurred while creating tar file: {e}")
