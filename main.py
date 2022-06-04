import json
import requests
import os
from os import makedirs

# https://game-assets.brawlstarsgame.com
# https://game-assets.clashroyaleapp.com
# https://game-assets.clashofclans.com

def Download(file, url):

    fp = json.load(open(file, "r+"))

    version = fp["version"]
    sha = fp["sha"]

    print(f"\nVersion {version}\nSHA {sha}\n")

    for file in fp["files"]:
        
        file = file["file"]
        request = requests.get(f"{url}/{sha}/{file}")

        if request.status_code == 200:
 
            folder = os.path.split(file)[0]

            makedirs(f"{sha}/{folder}", exist_ok = True)

            f = open(f"{sha}/{file}", "wb")
            f.write(request.content)
            f.close

            print(f"Downloaded {file}")
        
        else:
            
            print(f"{file} Status Code: {request.status_code}")
            break

file = input("Fingerprint File:\n")
url = input("Assets URL:\n")

Download(file, url)
