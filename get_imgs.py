import json
import requests
import os

def download(name,url):
    r = requests.get(url, stream=True)
    with open(name, 'wb') as fd:
        print(name,end=' : ')
        for chunk in r.iter_content(1024*500):
            print("=",end='')
            fd.write(chunk)
        print(">","compeleted")
    

if not os.path.exists("imgs"):os.makedirs("imgs")
f=open("books.json","r",encoding="utf-8").read()
books=eval(f)
i=1
for book in books:
    img=book['img']
    url=book['url']
    url=url[7:]
    img_name=url+".svg"
    print(i," : Downloading : ",img)
    download("imgs/"+img_name,img)
    i=i+1

print("done")