import os
import time
import webbrowser

url_file_path = input("Enter the path of the URL file: ")

if not os.path.isfile(url_file_path):
    print("Invalid file path.")
    exit()

with open(url_file_path, 'r') as file:
    urls = file.readlines()

urls = [url.strip() for url in urls]

for url in urls:
    webbrowser.get('firefox').open(url)
    time.sleep(4)  # 4-second delay between each URL