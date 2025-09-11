import os
import requests
from urllib.parse import urlparse
from uuid import uuid4

# Create directory if it doesn't exist
folder_name = "Fetched_Images"
os.makedirs(folder_name, exist_ok=True)

# Prompt user for image URL
url = input("Enter the image URL: ")

try:
    # Add headers to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Fetch the image with headers
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Raise error for bad status codes

    # Extract filename from URL or generate one
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename or '.' not in filename:
        filename = f"image_{uuid4().hex}.jpg"  # Fallback filename

    # Save image in binary mode
    filepath = os.path.join(folder_name, filename)
    with open(filepath, 'wb') as f:
        f.write(response.content)

    print(f"✅ Image saved successfully as '{filename}' in '{folder_name}'.")

except requests.exceptions.HTTPError as http_err:
    print(f"❌ HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError:
    print("❌ Connection error. Please check your internet or the URL.")
except requests.exceptions.Timeout:
    print("❌ Request timed out. Try again later.")
except Exception as err:
    print(f"❌ An unexpected error occurred: {err}")