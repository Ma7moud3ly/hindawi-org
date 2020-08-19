from bs4 import BeautifulSoup
import json as j

def getBook(li,to_str):
    book={}
    a=li.find('a')
    url=a['href']
    img=a.object['data']
    book['url']=url[:-1]
    book['img']=img

    name=''
    try:
        name=li.find('h2').a.contents
        if(type(name)==list):name=name[0].strip()
    except:pass    
    book['name']=name

    author=''
    try:
        author=li.find('div',class_="author").a.text
    except:pass    
    book['author']=author

    details=''
    try:
        details=li.find('div',class_="content").text
        details=details.strip()
    except:pass    
    book['details']=details

    if(to_str):return str(book).replace("'",'"')
    return book

def getBooks(src):
    soup = BeautifulSoup(src,features="html.parser")
    li = soup.findAll("li", {"class": "book"})
    return li

begin=1
ends=199

books=[]
json=open("books.json","w+",encoding="utf-8")
json.truncate(0)
json.write("[")
for i in range(begin,ends+1,1):
    page="pages/page%d.txt"%i
    print(page)
    f=open(page,"rb")
    src=f.read()
    f.close()
    lis=getBooks(src)
    n=len(lis)
    for j in range(n):
        li=lis[j]
        book=getBook(li,True)
        is_last_book = (i==ends and j==n-1)
        if(is_last_book==False):book+=","
        json.write(book)
        #books.append(book)
        


json.write("]")    
json.close()    
print("done")



quit()
