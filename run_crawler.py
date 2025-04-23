# run_crawler.py

from crawler.news_crawler import NaverFinanceCrawler, YonhapCrawler

naver_crawler = NaverFinanceCrawler()
yonhap_crawler = YonhapCrawler()

naver_news = naver_crawler.crawl()
yonhap_news = yonhap_crawler.crawl()

all_news = naver_news + yonhap_news

# 결과를 json 저장 (향후 분석용)
import json
from datetime import datetime

with open(f"data/news_{datetime.today().strftime('%Y%m%d')}.json", "w", encoding="utf-8") as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)