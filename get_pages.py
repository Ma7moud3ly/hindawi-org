import requests
import os
base_url="https://www.hindawi.org/books/"

def getSrc(url):
    while(True):
        request=requests.get(url)
        if(request.status_code==200):
            #request.encoding="utf-8"
            return request.content

def getPages(u,d,r):
    if not os.path.exists(d):
        os.makedirs(d)
    for i in range(r[0],r[1]+1,1):
        save_url="%s/page%s.txt"%(d,i)
        page_url=u+str(i)
        print(page_url)
        f=open(save_url,"wb")
        src=getSrc(page_url)
        f.write(src)
        f.close()
      

getPages(base_url,"pages",[1,199])

quit()
