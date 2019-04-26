import requests
from lxml import etree
import time
import MySQLdb

def get_mobile(n):
    url='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page='+str(2*n-1)
    headers = {'authority': 'search.jd.com',
            'method': 'GET',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=1&s=58&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie':'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
            }
    r = requests.get(url, headers=headers)
    r.encoding='utf-8'
    htmltext = etree.HTML(r.text)
    datas=htmltext.xpath('//li[contains(@class,"gl-item")]')
    mobile_list=[]
    for data in datas:
        conn=MySQLdb.connect(host='localhost',
                                 user='root',
                                 passwd='123456',
                                 db='blog',
                                 charset='utf8')
        cur=conn.cursor()
        array_jiage =data.xpath('./div/div[3]/strong/i/text()[1]')
        jiage = ",".join(map(str, array_jiage))
        array_jianjie =data.xpath('./div/div[4]/a/i/text()')
        jianjie = ",".join(map(str, array_jianjie))
        array_biaoti = data.xpath('./div/div[4]/a/em/text()')
        biaoti= ",".join(map(str, array_biaoti))
        mobile_list.append(biaoti)
        sql="INSERT INTO web_jingdong(biaoti,jiage,jianjie) VALUES('%s','%s','%s')"%(biaoti,jiage,jianjie)
        cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()
    return mobile_list 
if __name__=='__main__':
    for i in range(1,2):
        try:
            mobile_list1=get_mobile(i)
            print(mobile_list1)
        except Exception as e:
            print(e)