import os
import requests

def download_file(url, output_folder, filename=None):
    os.makedirs(output_folder, exist_ok=True)

    # Use last part of URL if filename not given
    if not filename:
        filename = url.split('/')[-1].split('?')[0]

    file_path = os.path.join(output_folder, filename)

    print(f"Downloading from: {url}")
    print(f"Saving to: {file_path}")

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print("Download complete.")

# Example usage
url = "https://drive.usercontent.google.com/download?id=10t4aGiP2gW7erDVXrrtzckPEZNnQIGwT&export=download&authuser=0&confirm=t&uuid=52898455-c8d8-4b73-b1c3-fba7c2bd7df8&at=AN8xHooQaYfp568kQK4C1zpR01pR%3A1750685844058"
output_folder = "downloads"       # Change to your desired path
