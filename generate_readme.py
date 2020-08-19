books=eval(open('mybooks.json','r',encoding='utf-8').read())

f=open('README.md','w+',encoding='utf-8')
f.truncate(0)
f.write('<div align="center">')
f.write('<h4>All books in <a href="https://hindawi.org">hindawi.org</a></h4><br>')

for i in range(len(books)):
  book=books[i]
  name=book['name']
  id=book['id']
  raw='https://raw.githubusercontent.com/Ma7moud3ly/hindawi-org/master'
  f.write('<a href="%s/txts/%s.txt">%s</a><br>'%(raw,id,name))

f.write('</div>')
f.close()
print('done')