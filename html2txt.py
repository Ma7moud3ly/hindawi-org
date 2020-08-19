from bs4 import BeautifulSoup
import os

def edit(text):
  t='\n\n\n\n\n\n\n\n'
  i=text.index(t)
  if(i==-1):return text
  j=len(t)
  text=text[i+j:]
  return text

def toText(book):
    html_path="htmls/%s.html"%book
    txt_path="txts/%s.txt"%book
    src=open(html_path,"r",encoding="utf-8").read()
    text = BeautifulSoup(src,features="html.parser").text
    text=edit(text)
    open(txt_path,"w",encoding="utf-8").write(text)


if not os.path.exists("txts"):os.makedirs("txts")
f=open("books.json","r",encoding="utf-8").read()
books=eval(f)
i=1
for book in books:
    url=book['url']
    book=url[7:]
    try:
        toText(book)
        print(i," : ",book)
    except:print('corrupted : ',i,url)
    i=i+1

print("done")
quit()