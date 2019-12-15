import requests
from bs4 import BeautifulSoup
import re
import xlwt

def get_article_source_list():
    for page in range(0,1005,15):
        # url = "http://search.cnki.com.cn/search.aspx?q=qw:森林水文学&cluster=all&val=&p="+str(page)
        # "http://search.cnki.com.cn/search.aspx?q=qw%3a%E6%A3%AE%E6%9E%97%E6%B0%B4%E6%96%87%E5%AD%A6&rank=relevant&cluster=zyk&val=CJFDTOTAL"
        url = "http://search.cnki.com.cn/Search.aspx?q=theme:天文学&rank=relevant&cluster=zyk&val=CJFDTOTAL&p="+str(page)
        	  # "http://search.cnki.com.cn/Search.aspx?q=theme%3a%E5%A4%A9%E6%96%87%E5%AD%A6&rank=relevant&cluster=zyk&val=CJFDTOTAL&p=1005"
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'lxml')
        items = bs.select(".year-count span")
        
        for item in items:
            with open('article.txt','a+',encoding = 'utf-8') as f:
                f.write(item.get_text()+"\n")
        

def parse_article_source():
    pattern = re.compile('《(.*?)》.*?')
    publishers = {}
    with open('./article.txt', 'r', encoding = 'utf-8') as f:
        content = f.read()
    results = re.findall(pattern,content)

    for item in results:
        print(item)
        if re.search(re.compile(r'论文|会议|第'),item):
            print(item)
            # pass
        else:
            if item in publishers:
                publishers[item] += 1
            else:
                publishers[item] = 1
        print('*'*100)
    result = sorted(publishers.items(), key = lambda x : x[1], reverse = True)
    return result

def save_to_excel(source):
    excel = xlwt.Workbook()
    sheet = excel.add_sheet('data')

    total = 0
    for index,item in enumerate(source):
        sheet.write(index, 0, item[0])
        sheet.write(index, 1, item[1])
        # if total > 523:
        #     total = 0
        # total += item[1]
        # sheet.write(index, 2, total)
    excel.save('data.xls')


if __name__ == '__main__':
    # get_article_source_list()
    # exit()
    result = parse_article_source()
    save_to_excel(result)