<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>교보문고 트렌드 대시보드</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Pretendard', sans-serif; max-width: 900px; margin: auto; padding: 20px; background: #f8f9fa; }
        .card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border-bottom: 1px solid #eee; padding: 12px; text-align: left; }
        th { background: #f4f4f4; }
        .tag { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; background: #e7f5ff; color: #1971c2; }
    </style>
</head>
<body>
    <div class="card">
        <h1>📈 오늘을 만든 키워드</h1>
        <canvas id="keywordChart" height="100"></canvas>
    </div>

    <div class="card">
        <h2>📚 일간 베스트셀러 TOP 10</h2>
        <table id="bookTable">
            <thead>
                <tr>
                    <th>순위</th><th>도서명</th><th>저자</th><th>분야</th>
                </tr>
            </thead>
            <tbody></tbody>
        </table>
    </div>

    <script>
        // data.json 파일을 불러와서 화면을 구성합니다.
        fetch('./data.json')
            .then(res => res.json())
            .then(data => {
                const tbody = document.querySelector('#bookTable tbody');
                const labels = [];
                const counts = [];

                data.forEach(book => {
                    // 테이블 생성
                    tbody.innerHTML += `<tr>
                        <td>${book.rank}</td>
                        <td><strong>${book.title}</strong></td>
                        <td>${book.author}</td>
                        <td><span class="tag">${book.category}</span></td>
                    </tr>`;
                    
                    // 차트 데이터 수집
                    labels.push(book.title.substring(0, 8) + "..");
                    counts.push(11 - book.rank); // 순위가 높을수록 높은 점수 부여
                });

                // Chart.js 시각화
                new Chart(document.getElementById('keywordChart'), {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{ label: '관심도 점수', data: counts, backgroundColor: '#339af0' }]
                    }
                });
            });
    </script>
</body>
</html>
[
  {"rank": 3, "title": "생각의 기원", "author": "마이클 토마셀로", "category": "인문"},
  {"rank": 4, "title": "불변의 법칙", "author": "모건 하우절", "category": "경제경영"},
  {"rank": 5, "title": "세이노의 가르침", "author": "세이노", "category": "자기계발"}
]
