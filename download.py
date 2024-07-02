import requests
import os

# GitHub repository details
owner = "samujjwaal"
repo = "Cranfield-Vector-Space-Model"
path = "cranfieldDocs"

# Local path to save files
local_path = "downloaded_files"

# Create the local directory if it doesn't exist
os.makedirs(local_path, exist_ok=True)

# GitHub API URL
api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

# Get the list of files
response = requests.get(api_url)
if response.status_code == 200:
    files = response.json()
    
    for file in files:
        if file['type'] == 'file':
            # Get the download URL
            download_url = file['download_url']
            
            # Download the file
            file_response = requests.get(download_url)
            if file_response.status_code == 200:
                # Save the file locally
                file_path = os.path.join(local_path, file['name'])
                with open(file_path, 'wb') as f:
                    f.write(file_response.content)
                print(f"Downloaded: {file['name']}")
            else:
                print(f"Failed to download: {file['name']}")
else:
    print("Failed to get file list from GitHub")