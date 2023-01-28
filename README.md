# url_downloader

This script reads a list of file URLs from a file called `urls.txt` and downloads them to a directory called `files`. It also creates a SHA1 hash of each file and writes the file name and hash to a CSV file called `hashes.csv`. After all files have been downloaded, the script compresses the entire files directory into a `files.tar.gz` file.
## Usage

1. Create a file called urls.txt and add the URLs of the files you want to download, one per line.
2. Run the script with python script.py
3. The files will be downloaded to the files directory and a hashes.csv file will be created with the file name and SHA1 hash of each file.
4. The entire files directory will be compressed into a files.tar.gz file.

## Dependencies

This script requires the following modules to be installed:

* `os`
* `csv`
* `hashlib`
* `urllib`
* `concurrent.futures`
* `tqdm`
* `tarfile`

## Error Handling

    If the `urls.txt` file is not found, the script will exit and print an error message.
    If there is an error while reading the `urls.txt` file, the script will exit and print an error message.
    If there is an error while downloading a file, the script will print an error message but will continue to download the remaining files.
    If there is an error while creating the `files.tar.gz` file, the script will print an error message but will continue to execute.

## Additional Features

    If file already exists, it skips the download and continues to the next file.
    Use `concurrent.futures` to download multiple files at a time and tqdm to display a progress bar.
    Use `tarfile` to compress the entire `files` directory with highest compression level.

## Note

In case you want to change the directory or filename you can easily change it from the code. You may need to change the directory paths and filenames in the following lines of code:

```python
os.makedirs("files", exist_ok=True)
with open('urls.txt') as file:
with open('hashes.csv', 'a') as csv_file:
with tarfile.open('./files.tar.gz', mode='w:gz', compresslevel=9) as tar:
```
