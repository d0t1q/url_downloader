import urllib.parse

# open the file with the URLs
with open("urls.txt") as f:
    urls = f.readlines()

# remove the newline character from each URL
urls = [url.strip() for url in urls]

# open the file to write the encoded URLs
with open("urls_encoded.txt", "w") as f:
    for url in urls:
        encoded_url = urllib.parse.quote(url, safe=':/')
        f.write(encoded_url + "\n")
