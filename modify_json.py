f=open("books.json","r",encoding="utf-8").read()
json=open("mybooks.json","w",encoding="utf-8")

books=eval(f)
books2=[]
i=1
for book in books:
    url=book['url']
    id=url[7:]
    name=book['name']
    details=book['details']
    books2.append({"id":id,"name":name,"details":details})
    

json.write(str(books2).replace("'",'"'))
json.close()
print("done")
quit()
