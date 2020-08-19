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
    


base_url='https://www.hindawi.org/books/'
if not os.path.exists("pubs"):os.makedirs("pubs")
f=open("books.json","r",encoding="utf-8").read()
books=eval(f)
i=1
for book in books:
    name=book['name']
    url=book['url']
    url=url[7:]
    pdf_name=url+".epub"
    pdf_url=base_url+pdf_name
    print(i," : Downloading : ",pdf_name,pdf_url)
    download("pubs/"+pdf_name,pdf_url)
    i=i+1

print("done")
