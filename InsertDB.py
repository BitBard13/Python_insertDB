from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re
conn = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock',
                        user='root', passwd='danang', db='scraping', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")
random.seed(datetime.datetime.now())
def store(question):
        cur.execute('INSERT INTO question (questtion) VALUES '
                '("%s")', (question))
        cur.connection.commit()

        # sdfsdfsdfsdfsdf
def getLinks():
        html = urlopen('https://stackoverflow.com/questions')
        bs = BeautifulSoup(html, 'html.parser')
        questionAll = bs.find_all('div', {'class':'summary'})
        for  question in questionAll :
                question1 = question.find('h3').find('a').get_text()
                print(question1)
                store(question1)
try:
                links = getLinks()
finally:
                cur.close()
                conn.close()
