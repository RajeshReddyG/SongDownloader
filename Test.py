import os
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "Bharat Ane Nenu Naasongs"
GURL = ""

for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
    GURL = j
print(GURL)

print(type(os.path.exists("DownLoadedSongs")))
    # print("Exists")
'''from googlesearch.googlesearch import GoogleSearch
response = GoogleSearch().search("something")
for result in response.results:
    print("Title: " + result.title)
    print("Content: " + result.getText())'''