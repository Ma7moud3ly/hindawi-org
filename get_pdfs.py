import json
import requests
import os

def download(name,url):
    r = requests.get(url, stream=True)
    with open(name, 'wb') as fd:
        print(name,end=' : ')
        for chunk in r.iter_content(1024*100):
            print("=",end='')
            fd.write(chunk)
        print(">","compeleted")
    


base_url='https://www.hindawi.org/books/'
if not os.path.exists("pdfs"):os.makedirs("pdfs")
f=open("books.json","r",encoding="utf-8").read()
books=eval(f)
for book in books:
    name=book['name']
    url=book['url']
    url=url[7:]
    pdf_name=url+".pdf"
    pdf_url=base_url+pdf_name
    print("Downloading : ",pdf_name,pdf_url)
    download("pdfs/"+pdf_name,pdf_url)

print("done")
