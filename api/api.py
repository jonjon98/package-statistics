"""Module api for abstraction of specific functions."""
# third party library imports
import gzip
import shutil
import os
from collections import defaultdict
import requests

def download_file(architecture) -> None:
    """download_file function to download the compressed Contents file"""
    print('Beginning file download with requests')
    url = 'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-' + architecture + '.gz'
    response = requests.get(url, timeout=120)

    if response.status_code != 200:
        return response.status_code

    with open('downloads/Contents-' + architecture + '.gz', 'wb') as file:
        file.write(response.content)

    # Retrieve HTTP meta-data
    print("Status Code: " + str(response.status_code))
    print("Content Type:" + response.headers['content-type'])
    return response.status_code

def decompress_file(architecture) -> None:
    """decompress_file function to decompress compressed Contents file"""
    with gzip.open('downloads/Contents-' + architecture + '.gz', 'rb') as f_in:
        with open('decompress/Contents-' + architecture + '.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def parsing(architecture) -> None:
    """parsing function to parse the Contents file"""
    package_stats = defaultdict(int)

    # Open the Contents file for reading
    with open('decompress/Contents-' + architecture + '.txt', encoding='utf-8') as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into two parts using the first whitespace character as the separator
            parts = line.split(None, 1)
            # Extract the file path and package name from the split line
            file_path = parts[0]
            package_name = parts[1].rstrip()  # Remove the trailing newline character

            if file_path == "EMPTY_PACKAGE":
                continue

            package_stats[package_name] += 1

    # Statistic analysis
    # Sort the dictionary by value and take the first 10 items
    top_10 = sorted(package_stats.items(), key=lambda x: x[1], reverse=True)[:10]

    print("-----Statistics for the top 10 packages-----")
    count = 1
    # Print the top 10 items
    for key, value in top_10:
        print(str(count) + f". {key}: {value}")
        count += 1

def cleanup(architecture) -> None:
    """cleanup function to deleted downloaded files"""
    # Specify the file path
    compressed_file_path = 'downloads/Contents-' + architecture + '.gz'
    decompressed_file_path = 'decompress/Contents-' + architecture + '.txt'

    # Check if the compressed file exists before attempting to delete it
    if os.path.exists(compressed_file_path):
        os.remove(compressed_file_path)
    else:
        print(f"The file {compressed_file_path} does not exist.")

    # Check if the decompressed file exists before attempting to delete it
    if os.path.exists(decompressed_file_path):
        os.remove(decompressed_file_path)
    else:
        print(f"The file {decompressed_file_path} does not exist.")
