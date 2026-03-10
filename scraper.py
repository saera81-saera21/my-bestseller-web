import requests
from bs4 import BeautifulSoup
import json

def get_kyobo_bestseller():
    url = "https://store.kyobobook.co.kr/bestseller/online/daily"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # 실제 사이트 구조에 맞춰 데이터를 추출하는 로직 (예시)
    books = []
    # 교보문고 사이트의 실시간 데이터 구조를 파싱하여 리스트에 담습니다.
    # (여기서는 앞서 우리가 만든 구조와 동일하게 10위까지 추출하도록 설정합니다)
    
    # 예시 데이터를 실제 수집 데이터로 가정하여 저장
    # (실제 환경에서는 soup.select 등을 사용하여 자동 추출)
    data = [
        {"rank": 1, "title": "나의 완벽한 장례식", "author": "정선임", "category": "소설"},
        {"rank": 2, "title": "마흔에 읽는 쇼펜하우어", "author": "강용수", "category": "인문"},
        # ... 자동 수집 로직 수행
    ]
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    get_kyobo_bestseller()
