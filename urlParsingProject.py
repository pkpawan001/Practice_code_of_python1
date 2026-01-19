# https//www.google.com/image

url="https://www.google.com/image/pic/salman"
protocal=url[0 : url.find(':')]
d1=url.find('.')
d2=url.rfind('.')
doman=url[d1+1:d2]
p1=url.find('/',d2)
page=url[p1:]
print(protocal,doman,page)