import ebooklib
from ebooklib import epub
import os

def toText(book):
    pub_path="pubs/%s.epub"%book
    txt_path="htmls/%s.html"%book
    b = epub.read_epub(pub_path)
    f=open(txt_path,"ab")
    f.truncate(0)
    i=0;
    for item in b.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        i=i+1
        if(i<5):continue
        f.write(item.content)
    
    f.close()

if not os.path.exists("htmls"):os.makedirs("htmls")
f=open("books.json","r",encoding="utf-8").read()
books=eval(f)

for i in range(966,len(books)+1,1):
    book=books[i]
    url=book['url']
    book=url[7:]
    print(i," : ",book)
    try:toText(book)
    except:print('corrupted',url)

print("done")
quit()
