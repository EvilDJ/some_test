import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    html = html.decode('utf-8')  # python3
    print(html)
    imglist = re.findall(imgre,html)
    x = 0
    print('+++++',imglist)
    for imgurl in imglist:
        print('---',imgurl)
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
        if x==10:
            break

html = getHtml("https://tieba.baidu.com/p/6068572632")
getImg(html)