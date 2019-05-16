import requests
import html5lib
from bs4 import BeautifulSoup
import os
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# Query To Search
Name = input("Movie name: ")
query = str(Name) + " Naasongs"
GURL = ""

# Getting URL From Google
for tmpGURL in search(query, tld="co.in", num=1, stop=1, pause=2):
    GURL = tmpGURL
print(GURL)

r = requests.get(GURL)

soup = BeautifulSoup(r.content, 'html5lib')
# Checking For Directories
if(os.path.exists("DownLoadedSongs")):
    print("DownLoadedSongs Floder Already Exists")
else:
    os.system("mkdir DownLoadedSongs")
if(os.path.exists(Name)):
    print(str(Name)+" Floder Already Exists")
else:
    os.system("mkdir DownLoadedSongs/"+str(Name))

i = 0
hlink = ""
for link in soup.find_all('a'):
    hlink = link.get('href')
    # Checking all the hyperlinks for .mp3
    if ".mp3" in hlink:
        # print(hlink)
        i = i+1
        r = requests.get(hlink, stream=True)
        with open("DownLoadedSongs/"+str(Name) + "/" + str(Name) + "-" + str(i)+".mp3", "wb") as mp3:
            for chunk in r.iter_content(chunk_size=1024):
                # writing one chunk at a time to mp3 file
                if chunk:
                    mp3.write(chunk)


'''# Downloading .ZIP
    if ".zip" in hlink:
        print(hlink)
        i = i+1
        r = requests.get(hlink, stream=True)
        with open("DownLoadedSongs/"+str(Name) + "-" + str(i)+".zip", "wb") as zip:
            for chunk in r.iter_content(chunk_size=1024):
                # writing one chunk at a time to pdf file
                if chunk:
                    zip.write(chunk)
        break'''
