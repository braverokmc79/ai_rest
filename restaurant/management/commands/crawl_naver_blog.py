### 📁 파일 구성 (Django 모델과 연동된 크롤러) ###
# Jupyter 환경에서 실행 가능하도록 구성

# ✅ 1. 환경설정
import os
import django
import time
import random
import sys


# 1) __file__ → commands
# 2) → management
# 3) → restaurant
# 4) → ai_rest   ← 여기에 올라와야 'proj' 모듈을 찾을 수 있습니다.
BASE_DIR = os.path.dirname(  # level 4
    os.path.dirname(         # level 3
        os.path.dirname(     # level 2
            os.path.dirname( # level 1
                os.path.abspath(__file__)
            )
        )
    )
)
sys.path.insert(0, BASE_DIR)


# settings 모듈 지정 (프로젝트 폴더명이 'ai_rest'라면)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")




django.setup()  # 장고 앱 초기화

# ✅ 2. 크롤링 라이브러리
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import unicodedata
from restaurant.models import Article  # Django 모델 import

# ✅ 3. 전처리 함수
def clean_text(text):
    text = "".join(c for c in text if not unicodedata.category(c).startswith("C"))
    text = re.sub(r"[ \t\n\r\f\v]+", " ", text)
    return text.strip()

# ✅ 4. 개별 블로그 페이지 크롤링 함수
def crawl_naver_blog(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('user-agent=Mozilla/5.0')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    try:
        iframe = driver.find_element(By.ID, "mainFrame")
        driver.switch_to.frame(iframe)
        driver.find_element(By.ID, "post-area")
        res = driver.page_source
    except Exception:
        res = driver.page_source  # iframe 없는 경우도 대비

    driver.quit()

    soup = BeautifulSoup(res, "html.parser")
    content = soup.find("div", {"class": "se-main-container"}) or soup.find("div", {"id": "postViewArea"})
    if not content:
        return None, None

    # 제목 추출
    title_tag = soup.find("h3") or soup.find("div", class_=re.compile("se-title|se_textarea"))
    title = clean_text(title_tag.text if title_tag else "제목 없음")

    # 내용 추출
    span_tag = content.find("span", text=re.compile("블로그기자단"))
    if span_tag:
        span_tag.decompose()
    content_text = clean_text(content.text)

    return title, content_text

# ✅ 5. 검색 결과에서 블로그 링크 수집 후 저장
def crawl_naver_blogs(location="강남", keyword="맛집", max_count=10):
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # 화면 확인용으로 끄기
    chrome_options.add_argument('user-agent=Mozilla/5.0')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    search_query = f"{location} {keyword} 리뷰"
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_hty.top&query={search_query}"
    driver.get(url)

    time.sleep(3)

    with open("naver_result.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    blog_links = []
    for a_tag in soup.select("a.title_link"):  # 여기 수정
        link = a_tag.get("href")
        if link.startswith("https://blog.naver.com"):
            blog_links.append(link)

    ...

# ✅ 6. 실행 예시
crawl_naver_blogs(location="강남", keyword="맛집", max_count=10)  # 개발 테스트용 10개부터



# if __name__ == "__main__":
#     crawl_naver_blogs("강남", "맛집", max_count=100)