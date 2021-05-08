from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus

baseUrl = 'https://kin.naver.com/qna/detail.nhn?d1id=3&dirId=302140101&docId=379047512&qb=7JWE7J207JygIOyCrOynhA==&enc=utf8&section=kin&rank=1&search_sort=0&spq=0'
#plusUrl = input('검색어 입력: ') 
#crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))
 
url = baseUrl  #+ quote_plus(plusUrl) # 한글 검색 자동 변환
html = urlopen(url)

soup = bs(html, "html.parser")

img = soup.find_all(class_='se-module-image-link __se_image_link __se_link')

 
n = 1
for i in img:
    print(n)
    b = str(i).split(',')
    imgUrl = b[1][10:-1]
    with urlopen(imgUrl) as f:
        with open('C:\\Users\\user\\Desktop\\img\\' + str(n)+'.jpg','wb') as h: # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
    
    
print('Image Crawling is done.')
