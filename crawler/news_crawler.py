# news_crawler.py

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
import time

# 최근 7일 날짜 리스트 생성 함수
def get_last_7_days():
    today = datetime.today()
    return [(today - timedelta(days=i)).strftime("%Y.%m.%d") for i in range(7)]


# 네이버 금융 뉴스 크롤러 클래스
class NaverFinanceCrawler:
    def __init__(self):
        self.base_url = "https://finance.naver.com/news/news_list.naver"

    def crawl(self):
        news_data = []
        for page in range(1, 6):  # 최근 뉴스 5페이지만 수집
            params = {'mode': 'RANK', 'page': page}
            response = requests.get(self.base_url, params=params)
icetomato1x4@gmail.com

            links = soup.select('dl > dt:not(.photo) > a')
            for link in links:
                title = link.get_text(strip=True)
                url = "https://finance.naver.com" + link['href']
                content = self.get_article_content(url)

                if content:
                    news_data.append({
                        'source': 'NaverFinance',
                        'title': title,
                        'url': url,
                        'content': content
                    })
                time.sleep(0.2)
        return news_data

    def get_article_content(self, url):
        # 기사 본문을 추출하는 함수
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'html.parser')
            article = soup.select_one('div#news_read')
            return article.get_text(strip=True) if article else ""
        except Exception as e:
            print(f"Error fetching article from {url}: {e}")
            return ""


# 연합뉴스 경제 뉴스 크롤러 클래스
class YonhapCrawler:
    def __init__(self):
        self.base_url = "https://www.yna.co.kr/economy/all"

    def crawl(self):
        news_data = []
        for page in range(1, 6):
            url = f"{self.base_url}?site=navi&page={page}"
            res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(res.text, 'html.parser')

            articles = soup.select('div.list-type038 a.tit-wrap')

            for a in articles:
                link = a['href']
                title = a.get_text(strip=True)
                content = self.get_article_content(link)

                if content:
                    news_data.append({
                        'source': 'YonhapNews',
                        'title': title,
                        'url': link,
                        'content': content
                    })
                time.sleep(0.2)
        return news_data

    def get_article_content(self, url):
        try:
            res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(res.text, 'html.parser')
            article = soup.select_one('div#articleWrap div.article')
            return article.get_text(strip=True) if article else ""
        except Exception as e:
            print(f"Error fetching Yonhap article: {e}")
            return ""