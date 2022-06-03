import json
import requests
from os import makedirs

# https://game-assets.brawlstarsgame.com
# https://game-assets.clashroyaleapp.com
# https://game-assets.clashofclans.com

def Download(file, url):

    fp = open(file, "r+")
    fp = json.load(fp)

    version = fp["version"]
    sha = fp["sha"]

    print(f"\nVersion {version}\nSHA {sha}\n")

    for file in fp["files"]:
        
        file = file["file"]
        request = requests.get(f"{url}/{sha}/{file}")

        folder = file.split("/", 1)[0]
        makedirs(f"{sha}/{folder}", exist_ok=True)

        f = open(f"{sha}/{file}", "w+")
        f.write(str(request.content))
        f.close

        print(f"Downloaded {file}")

file = input("Fingerprint File:\n")
url = input("Assets URL:\n")

Download(file, url)